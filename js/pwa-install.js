/**
 * PWA Installation Manager
 * Управља install prompt-ом и PWA функционалношћу
 */

const PWAInstall = {
    deferredPrompt: null,
    installButton: null,

    /**
     * Иницијализуј PWA
     */
    init() {
        // Региструј Service Worker
        this.registerServiceWorker();
        
        // Слушај за install prompt
        this.setupInstallPrompt();
        
        // Провери да ли је већ инсталирано
        this.checkIfInstalled();
    },

    /**
     * Региструј Service Worker
     */
    async registerServiceWorker() {
        if ('serviceWorker' in navigator) {
            try {
                const registration = await navigator.serviceWorker.register('/service-worker.js');
                console.log('✅ PWA Service Worker registered:', registration);
                
                // Провери за ажурирања
                registration.addEventListener('updatefound', () => {
                    const newWorker = registration.installing;
                    newWorker.addEventListener('statechange', () => {
                        if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                            this.showUpdateNotification();
                        }
                    });
                });
            } catch (error) {
                console.error('❌ Service Worker registration failed:', error);
            }
        }
    },

    /**
     * Setup Install Prompt
     */
    setupInstallPrompt() {
        window.addEventListener('beforeinstallprompt', (e) => {
            // Спречи аутоматски prompt
            e.preventDefault();
            this.deferredPrompt = e;
            
            // Прикажи custom install button
            this.showInstallButton();
            
            console.log('📱 PWA Install prompt ready');
        });

        // Слушај за успешну инсталацију
        window.addEventListener('appinstalled', () => {
            console.log('✅ PWA installed successfully!');
            this.hideInstallButton();
            this.showInstalledMessage();
        });
    },

    /**
     * Прикажи Install Button
     */
    showInstallButton() {
        // Провери да ли button већ постоји
        if (this.installButton) return;

        // Креирај install button
        this.installButton = document.createElement('div');
        this.installButton.id = 'pwa-install-button';
        this.installButton.innerHTML = `
            <div style="
                position: fixed;
                bottom: 2rem;
                left: 2rem;
                background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
                color: white;
                padding: 1rem 1.5rem;
                border-radius: 14px;
                box-shadow: 0 8px 32px rgba(212,175,55,0.4), 0 4px 16px rgba(0,0,0,0.2);
                cursor: pointer;
                z-index: 9998;
                font-family: 'Montserrat', sans-serif;
                font-weight: 600;
                display: flex;
                align-items: center;
                gap: 0.75rem;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                animation: slideInLeft 0.5s ease-out;
                border: 1px solid rgba(255,255,255,0.2);
            " onmouseover="this.style.transform='translateY(-3px) scale(1.02)'; this.style.boxShadow='0 12px 40px rgba(212,175,55,0.5), 0 6px 20px rgba(0,0,0,0.25)'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 8px 32px rgba(212,175,55,0.4), 0 4px 16px rgba(0,0,0,0.2)'">
                <i class="fas fa-mobile-alt" style="font-size: 1.5rem;"></i>
                <div style="display: flex; flex-direction: column; align-items: flex-start;">
                    <span style="font-size: 0.875rem; opacity: 0.9; margin-bottom: 0.125rem;">Инсталирај апликацију</span>
                    <span style="font-size: 1.125rem; font-weight: 700;">Ресторан Златар</span>
                </div>
                <i class="fas fa-times" style="margin-left: 0.5rem; opacity: 0.7; font-size: 1rem;" onclick="event.stopPropagation(); PWAInstall.hideInstallButton();"></i>
            </div>
        `;

        // Додај стилове за анимацију
        if (!document.getElementById('pwa-animations')) {
            const style = document.createElement('style');
            style.id = 'pwa-animations';
            style.textContent = `
                @keyframes slideInLeft {
                    from {
                        transform: translateX(-400px);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
                @keyframes slideOutLeft {
                    from {
                        transform: translateX(0);
                        opacity: 1;
                    }
                    to {
                        transform: translateX(-400px);
                        opacity: 0;
                    }
                }
                @media (max-width: 768px) {
                    #pwa-install-button > div {
                        left: 1rem !important;
                        right: 1rem !important;
                        bottom: 1rem !important;
                        max-width: calc(100% - 2rem) !important;
                    }
                }
            `;
            document.head.appendChild(style);
        }

        // Додај click handler
        this.installButton.querySelector('div').addEventListener('click', () => {
            this.installApp();
        });

        document.body.appendChild(this.installButton);

        // Аутоматски сакриј после 15 секунди
        setTimeout(() => {
            if (this.installButton) {
                this.hideInstallButton();
            }
        }, 15000);
    },

    /**
     * Сакриј Install Button
     */
    hideInstallButton() {
        if (this.installButton) {
            const btn = this.installButton.querySelector('div');
            btn.style.animation = 'slideOutLeft 0.3s ease-in';
            setTimeout(() => {
                this.installButton.remove();
                this.installButton = null;
            }, 300);
        }
    },

    /**
     * Инсталирај апликацију
     */
    async installApp() {
        if (!this.deferredPrompt) {
            console.log('⚠️ Install prompt not available');
            return;
        }

        // Прикажи native install prompt
        this.deferredPrompt.prompt();

        // Сачекај корисников избор
        const { outcome } = await this.deferredPrompt.userChoice;
        console.log(`📱 User ${outcome === 'accepted' ? 'accepted' : 'dismissed'} the install prompt`);

        // Очисти prompt
        this.deferredPrompt = null;
        this.hideInstallButton();
    },

    /**
     * Провери да ли је апликација инсталирана
     */
    checkIfInstalled() {
        // Провери standalone mode
        if (window.matchMedia('(display-mode: standalone)').matches) {
            console.log('✅ Running as installed PWA');
            this.onInstalled();
        }

        // Провери iOS standalone
        if (window.navigator.standalone === true) {
            console.log('✅ Running as installed PWA (iOS)');
            this.onInstalled();
        }
    },

    /**
     * Акција када је апликација инсталирана
     */
    onInstalled() {
        // Додај класу на body
        document.body.classList.add('pwa-installed');
        
        // Можеш додати специјалне функције за инсталирану верзију
        console.log('🎉 PWA features enabled');
    },

    /**
     * Прикажи поруку о успешној инсталацији
     */
    showInstalledMessage() {
        const message = document.createElement('div');
        message.innerHTML = `
            <div style="
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: linear-gradient(135deg, rgba(46, 125, 50, 0.98), rgba(56, 142, 60, 0.95));
                color: white;
                padding: 2rem 2.5rem;
                border-radius: 16px;
                box-shadow: 0 12px 48px rgba(0,0,0,0.3);
                z-index: 10001;
                text-align: center;
                animation: fadeInScale 0.4s ease-out;
                font-family: 'Montserrat', sans-serif;
            ">
                <i class="fas fa-check-circle" style="font-size: 3rem; margin-bottom: 1rem; display: block;"></i>
                <h3 style="margin: 0 0 0.5rem 0; font-size: 1.5rem; font-weight: 700;">Успешно инсталирано!</h3>
                <p style="margin: 0; font-size: 1rem; opacity: 0.95;">Златар апликација је на вашем Home Screen-у</p>
            </div>
        `;

        document.body.appendChild(message);

        setTimeout(() => {
            message.style.animation = 'fadeOutScale 0.4s ease-in';
            setTimeout(() => message.remove(), 400);
        }, 3000);
    },

    /**
     * Прикажи notification о ажурирању
     */
    showUpdateNotification() {
        const notification = document.createElement('div');
        notification.innerHTML = `
            <div style="
                position: fixed;
                bottom: 2rem;
                left: 50%;
                transform: translateX(-50%);
                background: linear-gradient(135deg, #2196F3, #1976D2);
                color: white;
                padding: 1rem 1.5rem;
                border-radius: 12px;
                box-shadow: 0 8px 32px rgba(33, 150, 243, 0.4);
                z-index: 10000;
                font-family: 'Montserrat', sans-serif;
                display: flex;
                align-items: center;
                gap: 1rem;
            ">
                <i class="fas fa-sync-alt"></i>
                <span>Ново ажурирање је доступно!</span>
                <button onclick="location.reload()" style="
                    background: white;
                    color: #2196F3;
                    border: none;
                    padding: 0.5rem 1rem;
                    border-radius: 8px;
                    font-weight: 600;
                    cursor: pointer;
                ">Освежи</button>
            </div>
        `;

        document.body.appendChild(notification);
    }
};

// Аутоматски иницијализуј када се страница учита
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => PWAInstall.init());
} else {
    PWAInstall.init();
}
