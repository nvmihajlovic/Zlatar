/**
 * Newsletter Subscription System with Supabase
 * Integrates with footer newsletter form
 * 
 * Features:
 * - Email validation
 * - Duplicate prevention
 * - User fingerprinting
 * - Success/error messages
 * - Fallback to localStorage
 */

const NewsletterSystem = {
    supabase: null,
    userFingerprint: null,

    /**
     * Initialize Supabase connection
     * Uses same credentials as blog stats
     */
    initSupabase() {
        const SUPABASE_URL = 'https://your-project.supabase.co';
        const SUPABASE_ANON_KEY = 'your-anon-key-here';
        
        this.supabase = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    },

    /**
     * Generate unique user fingerprint
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

        const msgBuffer = new TextEncoder().encode(fingerprint);
        const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    },

    /**
     * Validate email format
     */
    validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    },

    /**
     * Subscribe to newsletter
     * @param {string} email - User email
     * @param {string} name - User name (optional)
     * @returns {Object} { success, message }
     */
    async subscribe(email, name = null) {
        // Validate email
        if (!email || !this.validateEmail(email)) {
            return {
                success: false,
                message: 'Молимо унесите валидну email адресу'
            };
        }

        try {
            // Initialize if not already done
            if (!this.supabase) {
                this.initSupabase();
            }
            if (!this.userFingerprint) {
                this.userFingerprint = await this.generateFingerprint();
            }

            // Call Supabase function
            const { data, error } = await this.supabase
                .rpc('subscribe_newsletter', {
                    p_email: email.toLowerCase().trim(),
                    p_name: name?.trim() || null,
                    p_fingerprint: this.userFingerprint,
                    p_user_agent: navigator.userAgent
                });

            if (error) throw error;

            return data;

        } catch (error) {
            console.error('Newsletter subscription error:', error);
            
            // Fallback to localStorage
            return this.subscribeFallback(email, name);
        }
    },

    /**
     * Unsubscribe from newsletter
     * @param {string} email - User email
     */
    async unsubscribe(email) {
        if (!email || !this.validateEmail(email)) {
            return {
                success: false,
                message: 'Молимо унесите валидну email адресу'
            };
        }

        try {
            if (!this.supabase) {
                this.initSupabase();
            }

            const { data, error } = await this.supabase
                .rpc('unsubscribe_newsletter', {
                    p_email: email.toLowerCase().trim()
                });

            if (error) throw error;

            return data;

        } catch (error) {
            console.error('Newsletter unsubscribe error:', error);
            return {
                success: false,
                message: 'Грешка при одјављивању. Покушајте поново.'
            };
        }
    },

    /**
     * Fallback: Save to localStorage if Supabase fails
     */
    subscribeFallback(email, name) {
        const subscribers = JSON.parse(localStorage.getItem('newsletter_subscribers') || '[]');
        
        // Check if already subscribed
        if (subscribers.includes(email.toLowerCase())) {
            return {
                success: false,
                message: 'Већ сте пријављени за newsletter',
                already_subscribed: true
            };
        }

        // Add to local list
        subscribers.push(email.toLowerCase());
        localStorage.setItem('newsletter_subscribers', JSON.stringify(subscribers));

        return {
            success: true,
            message: 'Успешно сте се пријавили за newsletter!',
            fallback: true
        };
    },

    /**
     * Show success message in footer
     */
    showMessage(element, message, isSuccess = true) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'newsletter-message';
        messageDiv.textContent = message;
        messageDiv.style.cssText = `
            margin-top: 0.75rem;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            font-size: 0.875rem;
            font-family: 'Montserrat', sans-serif;
            text-align: center;
            animation: slideIn 0.3s ease-out;
            ${isSuccess 
                ? 'background: rgba(76, 175, 80, 0.2); border: 1px solid rgba(76, 175, 80, 0.4); color: #4CAF50;'
                : 'background: rgba(244, 67, 54, 0.2); border: 1px solid rgba(244, 67, 54, 0.4); color: #F44336;'
            }
        `;

        // Remove existing message if any
        const existingMessage = element.querySelector('.newsletter-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        element.appendChild(messageDiv);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            messageDiv.style.animation = 'slideOut 0.3s ease-in';
            setTimeout(() => messageDiv.remove(), 300);
        }, 5000);
    }
};

// Auto-initialize newsletter form when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const newsletterForm = document.getElementById('newsletterForm');
    
    if (!newsletterForm) return;

    newsletterForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const emailInput = newsletterForm.querySelector('input[type="email"]');
        const submitBtn = newsletterForm.querySelector('button[type="submit"]');
        const email = emailInput.value.trim();

        // Disable form during submission
        submitBtn.disabled = true;
        submitBtn.textContent = 'Слање...';

        try {
            // Subscribe
            const result = await NewsletterSystem.subscribe(email);

            // Show message
            NewsletterSystem.showMessage(
                newsletterForm,
                result.message,
                result.success
            );

            // Clear input on success
            if (result.success) {
                emailInput.value = '';
                
                // Track event (if you have analytics)
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'newsletter_signup', {
                        'event_category': 'engagement',
                        'event_label': 'footer_form'
                    });
                }
            }

        } catch (error) {
            NewsletterSystem.showMessage(
                newsletterForm,
                'Дошло је до грешке. Покушајте поново.',
                false
            );
        } finally {
            // Re-enable form
            submitBtn.disabled = false;
            submitBtn.textContent = 'Пријави се';
        }
    });

    // Add CSS animations
    if (!document.getElementById('newsletter-animations')) {
        const style = document.createElement('style');
        style.id = 'newsletter-animations';
        style.textContent = `
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateY(-10px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            @keyframes slideOut {
                from {
                    opacity: 1;
                    transform: translateY(0);
                }
                to {
                    opacity: 0;
                    transform: translateY(-10px);
                }
            }
        `;
        document.head.appendChild(style);
    }
});
