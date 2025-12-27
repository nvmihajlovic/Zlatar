/**
 * Supabase Blog Statistics Client
 * Handles likes and views for blog posts using Supabase backend
 * 
 * Usage:
 * 1. Include Supabase client: <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 * 2. Include this file: <script src="js/blog-stats-supabase.js"></script>
 * 3. Call: await BlogStats.init('blog-post-1')
 */

const BlogStats = {
    supabase: null,
    currentPostId: null,
    userFingerprint: null,

    /**
     * Initialize Supabase connection
     * Replace with your actual Supabase credentials
     */
    initSupabase() {
        const SUPABASE_URL = 'https://your-project.supabase.co';
        const SUPABASE_ANON_KEY = 'your-anon-key-here';
        
        this.supabase = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    },

    /**
     * Generate unique user fingerprint
     * Uses browser/device info to create semi-persistent ID
     */
    async generateFingerprint() {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        ctx.textBaseline = 'top';
        ctx.font = '14px Arial';
        ctx.fillText('fingerprint', 2, 2);
        
        const fingerprint = [
            navigator.userAgent,
            navigator.language,
            screen.colorDepth,
            screen.width + 'x' + screen.height,
            new Date().getTimezoneOffset(),
            canvas.toDataURL()
        ].join('|');

        // Create hash
        const msgBuffer = new TextEncoder().encode(fingerprint);
        const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    },

    /**
     * Initialize for a specific blog post
     * @param {string} postId - Blog post ID (e.g., 'blog-post-1')
     */
    async init(postId) {
        this.currentPostId = postId;
        this.initSupabase();
        this.userFingerprint = await this.generateFingerprint();
        
        // Get current stats
        const stats = await this.getStats();
        
        // Register view (only once per session)
        await this.registerView();
        
        return stats;
    },

    /**
     * Get statistics for current post
     * @returns {Object} { likes, views, hasLiked }
     */
    async getStats() {
        try {
            // Get stats from blog_stats table
            const { data: stats, error: statsError } = await this.supabase
                .from('blog_stats')
                .select('likes, views')
                .eq('post_id', this.currentPostId)
                .single();

            if (statsError) throw statsError;

            // Check if user has liked this post
            const { data: likeData, error: likeError } = await this.supabase
                .from('blog_likes')
                .select('id')
                .eq('post_id', this.currentPostId)
                .eq('user_fingerprint', this.userFingerprint)
                .maybeSingle();

            return {
                likes: stats?.likes || 0,
                views: stats?.views || 0,
                hasLiked: !!likeData
            };
        } catch (error) {
            console.error('Error fetching stats:', error);
            return this.getFallbackStats();
        }
    },

    /**
     * Toggle like for current post
     * @returns {Object} { action, likes, views }
     */
    async toggleLike() {
        try {
            const stats = await this.getStats();
            
            if (stats.hasLiked) {
                // Unlike: Remove from blog_likes and decrement
                await this.supabase
                    .from('blog_likes')
                    .delete()
                    .eq('post_id', this.currentPostId)
                    .eq('user_fingerprint', this.userFingerprint);

                const { data, error } = await this.supabase
                    .from('blog_stats')
                    .update({ likes: Math.max(0, stats.likes - 1) })
                    .eq('post_id', this.currentPostId)
                    .select()
                    .single();

                if (error) throw error;

                return {
                    action: 'unliked',
                    likes: data.likes,
                    views: data.views
                };
            } else {
                // Like: Add to blog_likes and increment
                await this.supabase
                    .from('blog_likes')
                    .insert({
                        post_id: this.currentPostId,
                        user_fingerprint: this.userFingerprint
                    });

                const { data, error } = await this.supabase
                    .from('blog_stats')
                    .update({ likes: stats.likes + 1 })
                    .eq('post_id', this.currentPostId)
                    .select()
                    .single();

                if (error) throw error;

                return {
                    action: 'liked',
                    likes: data.likes,
                    views: data.views
                };
            }
        } catch (error) {
            console.error('Error toggling like:', error);
            return this.toggleLikeFallback();
        }
    },

    /**
     * Register view for current post (once per session)
     */
    async registerView() {
        const viewKey = `view_${this.currentPostId}`;
        
        // Check if already viewed this session
        if (sessionStorage.getItem(viewKey)) {
            return;
        }

        try {
            const stats = await this.getStats();
            
            await this.supabase
                .from('blog_stats')
                .update({ views: stats.views + 1 })
                .eq('post_id', this.currentPostId);

            sessionStorage.setItem(viewKey, 'true');
        } catch (error) {
            console.error('Error registering view:', error);
        }
    },

    /**
     * Subscribe to real-time updates for current post
     * @param {Function} callback - Called when stats change
     */
    subscribeToUpdates(callback) {
        return this.supabase
            .channel(`blog_stats:${this.currentPostId}`)
            .on(
                'postgres_changes',
                {
                    event: 'UPDATE',
                    schema: 'public',
                    table: 'blog_stats',
                    filter: `post_id=eq.${this.currentPostId}`
                },
                (payload) => {
                    callback({
                        likes: payload.new.likes,
                        views: payload.new.views
                    });
                }
            )
            .subscribe();
    },

    /**
     * Fallback: Get stats from localStorage
     */
    getFallbackStats() {
        const defaultLikes = {
            'blog-post-1': 42, 'blog-post-2': 38, 'blog-post-3': 45,
            'blog-post-4': 36, 'blog-post-5': 41, 'blog-post-6': 39,
            'blog-post-7': 43, 'blog-post-8': 37, 'blog-post-9': 44,
            'blog-post-10': 40, 'blog-post-11': 46, 'blog-post-12': 52
        };

        const likes = parseInt(localStorage.getItem(`likes_${this.currentPostId}`)) || defaultLikes[this.currentPostId] || 0;
        const views = parseInt(localStorage.getItem(`views_${this.currentPostId}`)) || 0;
        const hasLiked = localStorage.getItem(`hasLiked_${this.currentPostId}`) === 'true';

        return { likes, views, hasLiked };
    },

    /**
     * Fallback: Toggle like using localStorage
     */
    toggleLikeFallback() {
        const stats = this.getFallbackStats();
        const newLiked = !stats.hasLiked;
        const newLikes = newLiked ? stats.likes + 1 : Math.max(0, stats.likes - 1);

        localStorage.setItem(`likes_${this.currentPostId}`, newLikes);
        localStorage.setItem(`hasLiked_${this.currentPostId}`, newLiked);

        return {
            action: newLiked ? 'liked' : 'unliked',
            likes: newLikes,
            views: stats.views
        };
    }
};

// Auto-initialize if post ID is in data attribute
document.addEventListener('DOMContentLoaded', async () => {
    const postElement = document.querySelector('[data-post-id]');
    if (postElement) {
        const postId = postElement.getAttribute('data-post-id');
        await BlogStats.init(postId);
    }
});
