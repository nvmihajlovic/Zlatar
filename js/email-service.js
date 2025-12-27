/**
 * EmailJS Integration for Forms
 * Sends automatic confirmation emails + admin notifications
 * 
 * Supports:
 * - Reservation form (резервација)
 * - Contact form (контакт)
 * - Newsletter subscription
 * 
 * Setup: https://www.emailjs.com/
 * Free tier: 200 emails/month
 */

const EmailService = {
    // EmailJS credentials (get from https://dashboard.emailjs.com)
    SERVICE_ID: 'your_service_id',
    USER_ID: 'your_user_id',
    
    // Template IDs (create in EmailJS dashboard)
    TEMPLATES: {
        RESERVATION_CONFIRMATION: 'template_reservation_confirmation',
        RESERVATION_ADMIN: 'template_reservation_admin',
        CONTACT_CONFIRMATION: 'template_contact_confirmation',
        CONTACT_ADMIN: 'template_contact_admin',
        NEWSLETTER_CONFIRMATION: 'template_newsletter_confirmation'
    },

    /**
     * Initialize EmailJS
     */
    init() {
        if (typeof emailjs === 'undefined') {
            console.error('EmailJS SDK not loaded. Add: <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>');
            return false;
        }
        emailjs.init(this.USER_ID);
        return true;
    },

    /**
     * Send reservation confirmation + admin notification
     */
    async sendReservationEmails(data) {
        try {
            // Prepare data for emails
            const emailData = {
                to_name: data.name,
                to_email: data.email,
                from_name: 'Ресторан Златар',
                reply_to: 'info@restoranzlatar.com',
                
                // Reservation details
                guest_name: data.name,
                guest_email: data.email,
                guest_phone: data.phone,
                reservation_date: data.date,
                reservation_time: data.time,
                number_of_guests: data.guests,
                special_requests: data.notes || 'Нема',
                
                // Admin email
                admin_email: 'restoranzlatar@gmail.com'
            };

            // Send confirmation to guest
            await emailjs.send(
                this.SERVICE_ID,
                this.TEMPLATES.RESERVATION_CONFIRMATION,
                emailData
            );

            // Send notification to admin
            await emailjs.send(
                this.SERVICE_ID,
                this.TEMPLATES.RESERVATION_ADMIN,
                emailData
            );

            return {
                success: true,
                message: 'Резервација је послата! Проверите ваш email за потврду.'
            };

        } catch (error) {
            console.error('Email sending error:', error);
            return {
                success: false,
                message: 'Резервација је примљена, али email потврда није послата.'
            };
        }
    },

    /**
     * Send contact form confirmation + admin notification
     */
    async sendContactEmails(data) {
        try {
            const emailData = {
                to_name: data.name,
                to_email: data.email,
                from_name: 'Ресторан Златар',
                reply_to: 'info@restoranzlatar.com',
                
                // Contact details
                guest_name: data.name,
                guest_email: data.email,
                guest_phone: data.phone || 'Није наведен',
                message_subject: data.subject || 'Општа порука',
                message_content: data.message,
                
                // Admin email
                admin_email: 'restoranzlatar@gmail.com'
            };

            // Send confirmation to sender
            await emailjs.send(
                this.SERVICE_ID,
                this.TEMPLATES.CONTACT_CONFIRMATION,
                emailData
            );

            // Send notification to admin
            await emailjs.send(
                this.SERVICE_ID,
                this.TEMPLATES.CONTACT_ADMIN,
                emailData
            );

            return {
                success: true,
                message: 'Порука је послата! Одговорићемо вам у најкраћем року.'
            };

        } catch (error) {
            console.error('Email sending error:', error);
            return {
                success: false,
                message: 'Дошло је до грешке. Молимо покушајте поново.'
            };
        }
    },

    /**
     * Send newsletter welcome email
     */
    async sendNewsletterEmail(data) {
        try {
            const emailData = {
                to_name: data.name || 'Пријатељу',
                to_email: data.email,
                from_name: 'Ресторан Златар',
                reply_to: 'info@restoranzlatar.com',
                subscriber_email: data.email,
                subscriber_name: data.name || ''
            };

            await emailjs.send(
                this.SERVICE_ID,
                this.TEMPLATES.NEWSLETTER_CONFIRMATION,
                emailData
            );

            return {
                success: true,
                message: 'Хвала на пријави! Проверите ваш email.'
            };

        } catch (error) {
            console.error('Email sending error:', error);
            return {
                success: false,
                message: 'Пријава је успешна, али confirmation email није послат.'
            };
        }
    },

    /**
     * Show success/error message in modal or toast
     */
    showMessage(message, isSuccess = true) {
        // Create toast notification
        const toast = document.createElement('div');
        toast.className = 'email-toast';
        toast.innerHTML = `
            <div style="display: flex; align-items: center; gap: 0.875rem;">
                <i class="fas ${isSuccess ? 'fa-check-circle' : 'fa-exclamation-circle'}" 
                   style="font-size: 1.75rem; color: ${isSuccess ? '#ffffff' : '#ffffff'}; flex-shrink: 0; text-shadow: 0 2px 8px rgba(0,0,0,0.2);"></i>
                <div style="flex: 1;">
                    <div style="font-weight: 700; margin-bottom: 0.375rem; font-size: 1rem; color: #ffffff; text-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                        ${isSuccess ? 'Успешно!' : 'Грешка'}
                    </div>
                    <div style="font-size: 0.9375rem; color: #ffffff; line-height: 1.5; font-weight: 500;">
                        ${message}
                    </div>
                </div>
            </div>
        `;
        
        toast.style.cssText = `
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: ${isSuccess ? 
                'linear-gradient(135deg, #2E7D32 0%, #388E3C 50%, #43A047 100%)' : 
                'linear-gradient(135deg, #C62828 0%, #D32F2F 50%, #E53935 100%)'};
            color: #ffffff;
            padding: 1.25rem 1.5rem;
            border-radius: 14px;
            box-shadow: ${isSuccess ? 
                '0 8px 32px rgba(46, 125, 50, 0.4), 0 4px 16px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.2)' : 
                '0 8px 32px rgba(198, 40, 40, 0.4), 0 4px 16px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.2)'};
            z-index: 10000;
            animation: slideInRight 0.3s ease-out;
            max-width: 420px;
            min-width: 320px;
            font-family: 'Montserrat', sans-serif;
            border: 1px solid ${isSuccess ? 'rgba(255,255,255,0.2)' : 'rgba(255,255,255,0.2)'};
            backdrop-filter: blur(10px);
        `;

        document.body.appendChild(toast);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            toast.style.animation = 'slideOutRight 0.3s ease-in';
            setTimeout(() => toast.remove(), 300);
        }, 5000);

        // Add animations if not already present
        if (!document.getElementById('toast-animations')) {
            const style = document.createElement('style');
            style.id = 'toast-animations';
            style.textContent = `
                @keyframes slideInRight {
                    from {
                        transform: translateX(400px);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
                @keyframes slideOutRight {
                    from {
                        transform: translateX(0);
                        opacity: 1;
                    }
                    to {
                        transform: translateX(400px);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }
};

// Initialize EmailJS when page loads
document.addEventListener('DOMContentLoaded', () => {
    EmailService.init();
});
