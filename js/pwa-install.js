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
                left: 50%;
                transform: translateX(-50%);
                background: rgba(20, 15, 8, 0.98);
                backdrop-filter: blur(20px) saturate(180%);
                color: #ffffff;
                padding: 1.5rem 2rem;
                border-radius: 20px;
                box-shadow: 
                    0 20px 60px rgba(0, 0, 0, 0.6),
                    0 8px 24px rgba(212, 175, 55, 0.3),
                    inset 0 1px 0 rgba(255, 255, 255, 0.1),
                    0 0 0 1px rgba(212, 175, 55, 0.2);
                cursor: pointer;
                z-index: 9998;
                font-family: 'Montserrat', sans-serif;
                display: flex;
                align-items: center;
                gap: 1.25rem;
                max-width: 420px;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                animation: slideInUp 0.6s ease-out;
                border: 1px solid rgba(212, 175, 55, 0.25);
            " onmouseover="this.style.transform='translateX(-50%) translateY(-5px)'; this.style.boxShadow='0 24px 72px rgba(0, 0, 0, 0.7), 0 12px 32px rgba(212, 175, 55, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 0 0 1px rgba(212, 175, 55, 0.35)'" onmouseout="this.style.transform='translateX(-50%) translateY(0)'; this.style.boxShadow='0 20px 60px rgba(0, 0, 0, 0.6), 0 8px 24px rgba(212, 175, 55, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 0 0 1px rgba(212, 175, 55, 0.2)'">
                <div style="
                    width: 56px;
                    height: 56px;
                    background: linear-gradient(135deg, #D4AF37 0%, #FFD700 50%, #B8860B 100%);
                    border-radius: 14px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-shrink: 0;
                    box-shadow: 0 4px 16px rgba(212, 175, 55, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.3);
                ">
                    <i class="fas fa-download" style="font-size: 1.5rem; color: #140f08;"></i>
                </div>
                <div style="display: flex; flex-direction: column; align-items: flex-start; flex: 1; min-width: 0;">
                    <span style="font-size: 0.8125rem; color: rgba(255, 255, 255, 0.7); margin-bottom: 0.25rem; font-weight: 500; letter-spacing: 0.3px;">Инсталирај апликацију</span>
                    <span style="font-size: 1.125rem; font-weight: 700; color: #FFD700; letter-spacing: 0.3px; text-shadow: 0 2px 8px rgba(255, 215, 0, 0.3);">Ресторан Златар</span>
                    <span style="font-size: 0.75rem; color: rgba(255, 255, 255, 0.5); margin-top: 0.25rem; font-weight: 400;">Брз приступ • Offline режим</span>
                </div>
                <button onclick="event.stopPropagation(); PWAInstall.hideInstallButton();" style="
                    width: 32px;
                    height: 32px;
                    background: rgba(255, 255, 255, 0.08);
                    border: 1px solid rgba(255, 255, 255, 0.12);
                    border-radius: 8px;
                    color: rgba(255, 255, 255, 0.6);
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-shrink: 0;
                    transition: all 0.3s ease;
                    font-size: 0.875rem;
                    padding: 0;
                " onmouseover="this.style.background='rgba(255, 255, 255, 0.15)'; this.style.color='rgba(255, 255, 255, 0.9)'" onmouseout="this.style.background='rgba(255, 255, 255, 0.08)'; this.style.color='rgba(255, 255, 255, 0.6)'">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        `;

        // Додај стилове за анимацију
        if (!document.getElementById('pwa-animations')) {
            const style = document.createElement('style');
            style.id = 'pwa-animations';
            style.textContent = `
                @keyframes slideInUp {
                    from {
                        transform: translateX(-50%) translateY(100px);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(-50%) translateY(0);
                        opacity: 1;
                    }
                }
                @keyframes slideOutDown {
                    from {
                        transform: translateX(-50%) translateY(0);
                        opacity: 1;
                    }
                    to {
                        transform: translateX(-50%) translateY(100px);
                        opacity: 0;
                    }
                }
                @keyframes fadeInScale {
                    from {
                        transform: translate(-50%, -50%) scale(0.8);
                        opacity: 0;
                    }
                    to {
                        transform: translate(-50%, -50%) scale(1);
                        opacity: 1;
                    }
                }
                @keyframes fadeOutScale {
                    from {
                        transform: translate(-50%, -50%) scale(1);
                        opacity: 1;
                    }
                    to {
                        transform: translate(-50%, -50%) scale(0.9);
                        opacity: 0;
                    }
                }
                @media (max-width: 768px) {
                    #pwa-install-button > div {
                        left: 1rem !important;
                        right: 1rem !important;
                        bottom: 1rem !important;
                        max-width: calc(100% - 2rem) !important;
                        transform: translateX(0) !important;
                        padding: 1.25rem 1.5rem !important;
                    }
                    #pwa-install-button > div:hover {
                        transform: translateX(0) translateY(-5px) !important;
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
            btn.style.animation = 'slideOutDown 0.4s ease-in';
            setTimeout(() => {
                this.installButton.remove();
                this.installButton = null;
            }, 400);
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
                background: linear-gradient(135deg, rgba(20, 15, 8, 0.98) 0%, rgba(35, 26, 15, 0.98) 100%);
                backdrop-filter: blur(30px) saturate(180%);
                color: #ffffff;
                padding: 2.5rem 3rem;
                border-radius: 24px;
                box-shadow: 
                    0 24px 80px rgba(0, 0, 0, 0.7),
                    0 12px 40px rgba(212, 175, 55, 0.3),
                    inset 0 1px 0 rgba(255, 255, 255, 0.15),
                    0 0 0 1px rgba(212, 175, 55, 0.3);
                z-index: 10001;
                text-align: center;
                animation: fadeInScale 0.5s cubic-bezier(0.4, 0, 0.2, 1);
                font-family: 'Montserrat', sans-serif;
                max-width: 480px;
                width: 90%;
                border: 1px solid rgba(212, 175, 55, 0.25);
            ">
                <div style="
                    width: 80px;
                    height: 80px;
                    background: linear-gradient(135deg, #D4AF37 0%, #FFD700 50%, #B8860B 100%);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1.5rem;
                    box-shadow: 
                        0 8px 24px rgba(212, 175, 55, 0.5),
                        inset 0 2px 0 rgba(255, 255, 255, 0.3),
                        inset 0 -2px 8px rgba(0, 0, 0, 0.2);
                ">
                    <i class="fas fa-check" style="font-size: 2.5rem; color: #140f08;"></i>
                </div>
                <h3 style="
                    margin: 0 0 0.75rem 0;
                    font-size: 1.75rem;
                    font-weight: 800;
                    color: #FFD700;
                    letter-spacing: 0.3px;
                    text-shadow: 0 2px 12px rgba(255, 215, 0, 0.4);
                ">Успешно инсталирано!</h3>
                <p style="
                    margin: 0;
                    font-size: 1rem;
                    color: rgba(255, 255, 255, 0.85);
                    font-weight: 500;
                    line-height: 1.6;
                ">Златар апликација је додата<br>на ваш Home Screen</p>
                <div style="
                    margin-top: 1.5rem;
                    padding-top: 1.5rem;
                    border-top: 1px solid rgba(212, 175, 55, 0.2);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 0.75rem;
                    font-size: 0.875rem;
                    color: rgba(255, 255, 255, 0.6);
                    font-weight: 500;
                ">
                    <i class="fas fa-mobile-alt" style="color: #D4AF37;"></i>
                    <span>Отворите са Home Screen-а</span>
                </div>
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
