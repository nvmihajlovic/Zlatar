/**
 * Blog Stats API Client
 * Frontend JavaScript за комуникацију са MySQL базом
 */

const BlogStatsAPI = {
    // Промени ово на твој домен када окачиш сајт
    apiUrl: '/api/blog-stats.php',
    
    /**
     * Добија статистику за пост
     * @param {string} postId - ID поста (нпр. 'blog-post-1')
     * @returns {Promise<Object>} - {likes, views, hasLiked}
     */
    async getStats(postId) {
        try {
            const response = await fetch(`${this.apiUrl}?action=get&post_id=${postId}`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            if (data.success) {
                return {
                    likes: data.likes,
                    views: data.views,
                    hasLiked: data.hasLiked
                };
            } else {
                throw new Error(data.error || 'Failed to get stats');
            }
        } catch (error) {
            console.error('Error getting stats:', error);
            // Fallback на localStorage ако API не ради
            return this.getFallbackStats(postId);
        }
    },
    
    /**
     * Тогглује лајк за пост
     * @param {string} postId - ID поста
     * @returns {Promise<Object>} - {action, likes, views}
     */
    async toggleLike(postId) {
        try {
            const response = await fetch(this.apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    action: 'like',
                    post_id: postId
                })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            if (data.success) {
                return {
                    action: data.action, // 'liked' ili 'unliked'
                    likes: data.likes,
                    views: data.views
                };
            } else {
                throw new Error(data.error || 'Failed to toggle like');
            }
        } catch (error) {
            console.error('Error toggling like:', error);
            // Fallback на localStorage
            return this.toggleLikeFallback(postId);
        }
    },
    
    /**
     * Региструје преглед
     * @param {string} postId - ID поста
     */
    async incrementView(postId) {
        try {
            // Провери localStorage да не региструјемо више пута у истој сесији
            const sessionKey = `blog_view_${postId}`;
            if (sessionStorage.getItem(sessionKey)) {
                return; // Већ смо регистрували овај преглед у овој сесији
            }
            
            const response = await fetch(this.apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    action: 'view',
                    post_id: postId
                })
            });
            
            if (response.ok) {
                // Означи да смо регистрували преглед
                sessionStorage.setItem(sessionKey, 'true');
            }
        } catch (error) {
            console.error('Error incrementing view:', error);
        }
    },
    
    // Fallback функције ако API не ради (offline режим)
    getFallbackStats(postId) {
        const defaultStats = {
            'blog-post-1': 42,
            'blog-post-2': 38,
            'blog-post-3': 45,
            'blog-post-4': 52,
            'blog-post-5': 36,
            'blog-post-6': 41,
            'blog-post-7': 48,
            'blog-post-8': 39,
            'blog-post-9': 44,
            'blog-post-10': 50,
            'blog-post-11': 37,
            'blog-post-12': 43
        };
        
        const likes = parseInt(localStorage.getItem(`blog_likes_${postId}`) || defaultStats[postId] || 0);
        const hasLiked = localStorage.getItem(`blog_like_${postId}`) === 'true';
        
        return {
            likes: likes,
            views: 0,
            hasLiked: hasLiked
        };
    },
    
    toggleLikeFallback(postId) {
        const hasLiked = localStorage.getItem(`blog_like_${postId}`) === 'true';
        const currentLikes = this.getFallbackStats(postId).likes;
        
        if (hasLiked) {
            localStorage.removeItem(`blog_like_${postId}`);
            const newLikes = Math.max(0, currentLikes - 1);
            localStorage.setItem(`blog_likes_${postId}`, newLikes);
            return {
                action: 'unliked',
                likes: newLikes,
                views: 0
            };
        } else {
            localStorage.setItem(`blog_like_${postId}`, 'true');
            const newLikes = currentLikes + 1;
            localStorage.setItem(`blog_likes_${postId}`, newLikes);
            return {
                action: 'liked',
                likes: newLikes,
                views: 0
            };
        }
    }
};

// Експортуј за употребу у другим скриптама
if (typeof module !== 'undefined' && module.exports) {
    module.exports = BlogStatsAPI;
}
