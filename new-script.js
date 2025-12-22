// ====================================
// MODERN RESTAURANT WEBSITE - ZLATAR
// JavaScript with ES6+ Features
// ====================================

'use strict';

// ====================================
// LOADING SCREEN
// ====================================

window.addEventListener('load', () => {
    const loadingScreen = document.getElementById('loadingScreen');
    setTimeout(() => {
        loadingScreen.classList.add('hidden');
    }, 800);
});

// ====================================
// NAVIGATION
// ====================================

class Navigation {
    constructor() {
        this.navbar = document.getElementById('navbar');
        this.navMenu = document.getElementById('navMenu');
        this.navToggle = document.getElementById('navToggle');
        this.navLinks = document.querySelectorAll('.nav-link');
        this.navBlur = null;
        
        this.init();
    }
    
    init() {
        // Create blur background element
        this.createBlurElement();
        
        // Scroll effect
        window.addEventListener('scroll', () => this.handleScroll());
        
        // Mobile menu toggle
        this.navToggle.addEventListener('click', () => this.toggleMenu());
        
        // Close menu when clicking nav link
        this.navLinks.forEach(link => {
            link.addEventListener('click', () => {
                this.closeMenu();
                this.setActiveLink(link);
            });
        });
        
        // Close menu when clicking blur background
        if (this.navBlur) {
            this.navBlur.addEventListener('click', () => {
                this.closeMenu();
            });
        }
        
        // Close menu when clicking logo
        const navLogo = document.querySelector('.nav-logo');
        if (navLogo) {
            navLogo.addEventListener('click', (e) => {
                // Always force close menu if it's active
                if (this.navMenu && this.navMenu.classList.contains('active')) {
                    e.preventDefault();
                    this.closeMenu();
                    // Force scroll after menu is closed
                    setTimeout(() => {
                        const target = document.querySelector('#hero');
                        if (target) {
                            target.scrollIntoView({ behavior: 'smooth' });
                        }
                    }, 100);
                }
            });
        }
        
        // Close menu when clicking language button
        const langButtons = document.querySelectorAll('.lang-btn');
        langButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Close menu immediately for better UX
                if (this.navMenu.classList.contains('active')) {
                    this.closeMenu();
                }
            });
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!this.navMenu.contains(e.target) && 
                !this.navToggle.contains(e.target) &&
                !e.target.closest('.lang-btn')) {
                this.closeMenu();
            }
        });
        
        // Set active link on scroll
        this.setupScrollSpy();
    }
    
    createBlurElement() {
        // Check if blur element already exists
        this.navBlur = document.querySelector('.nav-blur');
        
        // Create blur element if it doesn't exist
        if (!this.navBlur) {
            this.navBlur = document.createElement('div');
            this.navBlur.className = 'nav-blur';
            this.navBlur.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.6);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                opacity: 0;
                pointer-events: none;
                transition: opacity 0.3s ease;
                z-index: 900;
            `;
            document.body.appendChild(this.navBlur);
        }
    }
    
    handleScroll() {
        if (window.scrollY > 100) {
            this.navbar.classList.add('scrolled');
        } else {
            this.navbar.classList.remove('scrolled');
        }
    }
    
    toggleMenu() {
        this.navMenu.classList.toggle('active');
        this.navToggle.classList.toggle('active');
        
        // Toggle blur background
        if (this.navBlur) {
            if (this.navMenu.classList.contains('active')) {
                this.navBlur.style.opacity = '1';
                this.navBlur.style.pointerEvents = 'all';
                this.navBlur.style.visibility = 'visible';
                document.body.style.overflow = 'hidden';
            } else {
                this.navBlur.style.opacity = '0';
                this.navBlur.style.pointerEvents = 'none';
                this.navBlur.style.visibility = 'hidden';
                document.body.style.overflow = '';
            }
        }
    }
    
    closeMenu() {
        this.navMenu.classList.remove('active');
        this.navToggle.classList.remove('active');
        
        // Hide blur background - force it multiple ways to ensure it's removed
        if (this.navBlur) {
            this.navBlur.style.opacity = '0';
            this.navBlur.style.pointerEvents = 'none';
            this.navBlur.style.visibility = 'hidden';
        }
        
        // Also check for any other blur elements
        const allBlurs = document.querySelectorAll('.nav-blur');
        allBlurs.forEach(blur => {
            blur.style.opacity = '0';
            blur.style.pointerEvents = 'none';
            blur.style.visibility = 'hidden';
        });
        
        document.body.style.overflow = '';
    }
    
    setActiveLink(clickedLink) {
        this.navLinks.forEach(link => link.classList.remove('active'));
        clickedLink.classList.add('active');
    }
    
    setupScrollSpy() {
        const sections = document.querySelectorAll('section[id]');
        
        window.addEventListener('scroll', () => {
            const scrollY = window.pageYOffset;
            
            sections.forEach(section => {
                const sectionHeight = section.offsetHeight;
                const sectionTop = section.offsetTop - 150;
                const sectionId = section.getAttribute('id');
                
                if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                    document.querySelector(`.nav-link[href="#${sectionId}"]`)?.classList.add('active');
                } else {
                    document.querySelector(`.nav-link[href="#${sectionId}"]`)?.classList.remove('active');
                }
            });
        });
    }
}

// ====================================
// HERO SLIDER
// ====================================

class HeroSlider {
    constructor() {
        this.slides = document.querySelectorAll('.hero-slide');
        this.currentSlide = 0;
        this.slideInterval = 5000; // 5 seconds
        
        this.init();
    }
    
    init() {
        if (this.slides.length > 1) {
            setInterval(() => this.nextSlide(), this.slideInterval);
        }
    }
    
    nextSlide() {
        this.slides[this.currentSlide].classList.remove('active');
        this.currentSlide = (this.currentSlide + 1) % this.slides.length;
        this.slides[this.currentSlide].classList.add('active');
    }
}

// ====================================
// RESERVATION MODAL
// ====================================

class ReservationModal {
    constructor() {
        this.modal = document.getElementById('reservationModal');
        this.modalOverlay = document.getElementById('modalOverlay');
        this.modalClose = document.getElementById('modalClose');
        this.btnReserve = document.getElementById('btnReserve');
        this.reservationForm = document.getElementById('reservationForm');
        
        this.init();
    }
    
    init() {
        // Open modal
        this.btnReserve?.addEventListener('click', () => this.openModal());
        
        // Close modal
        this.modalClose?.addEventListener('click', () => this.closeModal());
        this.modalOverlay?.addEventListener('click', () => this.closeModal());
        
        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.modal.classList.contains('active')) {
                this.closeModal();
            }
        });
        
        // Handle form submission
        this.reservationForm?.addEventListener('submit', (e) => this.handleSubmit(e));
    }
    
    openModal() {
        this.modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
    
    closeModal() {
        this.modal.classList.remove('active');
        document.body.style.overflow = '';
    }
    
    handleSubmit(e) {
        e.preventDefault();
        
        // Get form data
        const formData = {
            name: document.getElementById('resName').value,
            phone: document.getElementById('resPhone').value,
            date: document.getElementById('resDate').value,
            time: document.getElementById('resTime').value,
            guests: document.getElementById('resGuests').value,
            note: document.getElementById('resNote').value
        };
        
        // Show success message (you can integrate with backend here)
        this.showSuccessMessage();
        
        // Reset form
        this.reservationForm.reset();
        
        // Close modal
        setTimeout(() => this.closeModal(), 2000);
    }
    
    showSuccessMessage() {
        const message = document.createElement('div');
        message.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, #D4AF37, #CD853F);
            color: white;
            padding: 2rem 3rem;
            border-radius: 1rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            z-index: 10000;
            text-align: center;
            font-size: 1.25rem;
            font-weight: 600;
        `;
        message.innerHTML = `
            <i class="fas fa-check-circle" style="font-size: 3rem; margin-bottom: 1rem;"></i><br>
            Резервација послата!<br>
            <small style="font-size: 0.9rem; opacity: 0.9;">Контактираћемо вас ускоро.</small>
        `;
        
        document.body.appendChild(message);
        
        setTimeout(() => {
            message.style.transition = 'opacity 0.3s';
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 2000);
    }
}

// ====================================
// CONTACT FORM
// ====================================

class ContactForm {
    constructor() {
        this.form = document.getElementById('contactForm');
        this.init();
    }
    
    init() {
        this.form?.addEventListener('submit', (e) => this.handleSubmit(e));
    }
    
    handleSubmit(e) {
        e.preventDefault();
        
        // Get form data
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            message: document.getElementById('message').value
        };
        
        // Show success message
        this.showSuccessMessage();
        
        // Reset form
        this.form.reset();
    }
    
    showSuccessMessage() {
        const message = document.createElement('div');
        message.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, #D4AF37, #CD853F);
            color: white;
            padding: 2rem 3rem;
            border-radius: 1rem;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            z-index: 10000;
            text-align: center;
            font-size: 1.25rem;
            font-weight: 600;
        `;
        message.innerHTML = `
            <i class="fas fa-check-circle" style="font-size: 3rem; margin-bottom: 1rem;"></i><br>
            Порука послата!<br>
            <small style="font-size: 0.9rem; opacity: 0.9;">Одговорићемо вам у најкраћем року.</small>
        `;
        
        document.body.appendChild(message);
        
        setTimeout(() => {
            message.style.transition = 'opacity 0.3s';
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 2000);
    }
}

// ====================================
// BACK TO TOP BUTTON
// ====================================

class BackToTop {
    constructor() {
        this.button = document.getElementById('backToTop');
        this.init();
    }
    
    init() {
        window.addEventListener('scroll', () => this.handleScroll());
        this.button?.addEventListener('click', () => this.scrollToTop());
    }
    
    handleScroll() {
        if (window.scrollY > 300) {
            this.button.classList.add('visible');
        } else {
            this.button.classList.remove('visible');
        }
    }
    
    scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
}

// ====================================
// GALLERY LIGHTBOX
// ====================================

class Gallery {
    constructor() {
        this.galleryItems = document.querySelectorAll('.gallery-item');
        this.init();
    }
    
    init() {
        this.galleryItems.forEach(item => {
            item.addEventListener('click', () => {
                const img = item.querySelector('img');
                this.openLightbox(img.src, img.alt);
            });
        });
    }
    
    openLightbox(src, alt) {
        const lightbox = document.createElement('div');
        lightbox.style.cssText = `
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.95);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
            padding: 2rem;
            cursor: zoom-out;
        `;
        
        const img = document.createElement('img');
        img.src = src;
        img.alt = alt;
        img.style.cssText = `
            max-width: 100%;
            max-height: 100%;
            border-radius: 1rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        `;
        
        const closeBtn = document.createElement('button');
        closeBtn.innerHTML = '<i class="fas fa-times"></i>';
        closeBtn.style.cssText = `
            position: absolute;
            top: 2rem;
            right: 2rem;
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
            transition: all 0.3s;
        `;
        
        closeBtn.addEventListener('mouseenter', () => {
            closeBtn.style.background = '#D4AF37';
            closeBtn.style.transform = 'scale(1.1)';
        });
        
        closeBtn.addEventListener('mouseleave', () => {
            closeBtn.style.background = 'rgba(255, 255, 255, 0.1)';
            closeBtn.style.transform = 'scale(1)';
        });
        
        lightbox.appendChild(img);
        lightbox.appendChild(closeBtn);
        document.body.appendChild(lightbox);
        
        // Animate in
        setTimeout(() => {
            lightbox.style.opacity = '0';
            lightbox.style.transition = 'opacity 0.3s';
            lightbox.style.opacity = '1';
        }, 10);
        
        // Close handlers
        const closeLightbox = () => {
            lightbox.style.opacity = '0';
            setTimeout(() => lightbox.remove(), 300);
        };
        
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) closeLightbox();
        });
        
        closeBtn.addEventListener('click', closeLightbox);
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeLightbox();
        });
    }
}

// ====================================
// SMOOTH SCROLL
// ====================================

const setupSmoothScroll = () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href === '#' || !href) return;
            
            e.preventDefault();
            
            const target = document.querySelector(href);
            if (target) {
                const offsetTop = target.offsetTop - 80;
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
};

// ====================================
// ANIMATE ON SCROLL (Simple Implementation)
// ====================================

class ScrollAnimation {
    constructor() {
        this.elements = document.querySelectorAll('[data-aos]');
        this.init();
    }
    
    init() {
        this.observeElements();
    }
    
    observeElements() {
        const options = {
            threshold: 0.15,
            rootMargin: '0px 0px -100px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('aos-animate');
                }
            });
        }, options);
        
        this.elements.forEach(element => {
            observer.observe(element);
        });
    }
}

// ====================================
// ANNOUNCEMENT BAR ANIMATION
// ====================================

const setupAnnouncementBar = () => {
    const announcement = document.querySelector('.announcement-content');
    if (announcement) {
        // Clone content for infinite scroll
        const clone = announcement.cloneNode(true);
        announcement.parentElement.appendChild(clone);
    }
};

// ====================================
// PROMO BUTTON
// ====================================

const setupPromoButton = () => {
    const btnPromo = document.getElementById('btnPromo');
    
    btnPromo?.addEventListener('click', () => {
        const promoMessage = document.createElement('div');
        promoMessage.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, #5D4E37, #8B7355);
            color: white;
            padding: 3rem 2rem;
            border-radius: 1.5rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
            z-index: 10000;
            text-align: center;
            max-width: 90%;
            width: 400px;
        `;
        
        promoMessage.innerHTML = `
            <i class="fas fa-gift" style="font-size: 4rem; color: #D4AF37; margin-bottom: 1.5rem;"></i>
            <h3 style="font-size: 1.75rem; margin-bottom: 1rem; color: #D4AF37;">Специјална понуда!</h3>
            <p style="font-size: 1.125rem; margin-bottom: 2rem; opacity: 0.95;">
                Дегустација 3 врсте ракије + традиционално предјело<br>
                <strong style="font-size: 1.5rem; color: #D4AF37;">1500 РСД</strong>
            </p>
            <button id="closePromo" style="
                padding: 0.875rem 2rem;
                background: #D4AF37;
                color: white;
                border: none;
                border-radius: 50px;
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
                transition: all 0.3s;
            ">Затвори</button>
        `;
        
        document.body.appendChild(promoMessage);
        
        // Close button
        document.getElementById('closePromo').addEventListener('click', () => {
            promoMessage.style.transition = 'opacity 0.3s';
            promoMessage.style.opacity = '0';
            setTimeout(() => promoMessage.remove(), 300);
        });
        
        // Fade in
        setTimeout(() => {
            promoMessage.style.opacity = '0';
            promoMessage.style.transition = 'opacity 0.3s';
            promoMessage.style.opacity = '1';
        }, 10);
    });
};

// ====================================
// INITIALIZE ALL
// ====================================

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all components
    new Navigation();
    new HeroSlider();
    new ReservationModal();
    new ContactForm();
    new BackToTop();
    new Gallery();
    new ScrollAnimation();
    
    // Setup utilities
    setupSmoothScroll();
    setupAnnouncementBar();
    setupPromoButton();
    
    // Console greeting
    console.log('%c🍴 Ресторан Златар - 40 година традиције 🍴', 'font-size: 20px; color: #D4AF37; font-weight: bold;');
    console.log('%cWebsite developed by Web Studio Link', 'font-size: 12px; color: #8B7355;');
});

// ====================================
// PERFORMANCE OPTIMIZATION
// ====================================

// Lazy load images
if ('loading' in HTMLImageElement.prototype) {
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        img.src = img.dataset.src;
    });
} else {
    // Fallback for older browsers
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
    document.body.appendChild(script);
}

// ====================================
// ERROR HANDLING
// ====================================

window.addEventListener('error', (e) => {
    console.error('Error occurred:', e.message);
});

// ====================================
// EXPORT FOR TESTING (if needed)
// ====================================

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        Navigation,
        HeroSlider,
        ReservationModal,
        ContactForm,
        BackToTop,
        Gallery,
        ScrollAnimation
    };
}
