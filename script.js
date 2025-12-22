// Popup Manager Class - Manages all popup modals
class PopupManager {
    constructor() {
        this.popups = {
            reservation: document.getElementById('reservation-modal'),
            newsletter: document.getElementById('newsletter-modal'),
            specialOffer: document.getElementById('special-offer-modal')
        };
        
        this.init();
    }
    
    init() {
        // Close buttons
        document.querySelectorAll('.modal-close, .modal-overlay').forEach(el => {
            el.addEventListener('click', () => this.hideAll());
        });
        
        // ESC key to close
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') this.hideAll();
        });
        
        // Prevent body scroll when modal is open
        Object.values(this.popups).forEach(popup => {
            const observer = new MutationObserver(() => {
                if (popup.classList.contains('active')) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = '';
                }
            });
            observer.observe(popup, { attributes: true, attributeFilter: ['class'] });
        });
    }
    
    show(popupName) {
        if (this.popups[popupName]) {
            // Check if already shown today
            if (this.checkCookie(popupName)) {
                return;
            }
            
            this.hideAll();
            this.popups[popupName].classList.add('active');
        }
    }
    
    hide(popupName) {
        if (this.popups[popupName]) {
            this.popups[popupName].classList.remove('active');
        }
    }
    
    hideAll() {
        Object.values(this.popups).forEach(popup => {
            popup.classList.remove('active');
        });
    }
    
    checkCookie(popupName) {
        const name = `popup_${popupName}_shown=`;
        const decodedCookie = decodeURIComponent(document.cookie);
        const ca = decodedCookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i].trim();
            if (c.indexOf(name) === 0) {
                return true;
            }
        }
        return false;
    }
    
    setCookie(popupName, days = 1) {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + d.toUTCString();
        document.cookie = `popup_${popupName}_shown=true;${expires};path=/`;
    }
}

// Initialize Popup Manager
const popupManager = new PopupManager();

// Navbar scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Mobile menu toggle
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    hamburger.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        hamburger.classList.remove('active');
    });
});

// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });
    
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Reservation modal triggers
document.getElementById('btn-reserve-nav').addEventListener('click', () => {
    popupManager.show('reservation');
});

document.getElementById('btn-reserve-hero').addEventListener('click', () => {
    popupManager.show('reservation');
});

// Newsletter modal trigger
document.getElementById('btn-newsletter').addEventListener('click', () => {
    popupManager.show('newsletter');
});

// Special offer modal trigger
document.getElementById('btn-special-offer').addEventListener('click', () => {
    popupManager.show('specialOffer');
});

// Auto-show newsletter popup after 5 seconds (first visit only)
setTimeout(() => {
    if (!popupManager.checkCookie('newsletter')) {
        popupManager.show('newsletter');
    }
}, 5000);

// Show special offer popup on scroll to 30% (first visit only)
let specialOfferShown = false;
window.addEventListener('scroll', () => {
    const scrollPercentage = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
    
    if (scrollPercentage >= 30 && !specialOfferShown && !popupManager.checkCookie('specialOffer')) {
        popupManager.show('specialOffer');
        specialOfferShown = true;
    }
});

// Form submissions
document.getElementById('reservation-form').addEventListener('submit', (e) => {
    e.preventDefault();
    showNotification('Резервација успешно послата! Контактираћемо вас ускоро.', 'success');
    popupManager.hide('reservation');
    popupManager.setCookie('reservation', 1);
    e.target.reset();
});

document.getElementById('newsletter-form').addEventListener('submit', (e) => {
    e.preventDefault();
    showNotification('Успешно сте се пријавили на Newsletter!', 'success');
    popupManager.hide('newsletter');
    popupManager.setCookie('newsletter', 7); // Don't show again for 7 days
    e.target.reset();
});

document.getElementById('contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;
    
    // Basic validation
    if (!name || !email || !message) {
        showNotification('Молимо попуните сва обавезна поља.', 'error');
        return;
    }
    
    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showNotification('Молимо унесите исправну е-mail адресу.', 'error');
        return;
    }
    
    showNotification('Порука успешно послата! Одговорићемо вам ускоро.', 'success');
    e.target.reset();
});

// Notification system
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
        <span>${message}</span>
    `;
    
    // Add styles if not already added
    if (!document.getElementById('notification-styles')) {
        const style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent = `
            .notification {
                position: fixed;
                top: 100px;
                right: 20px;
                background: white;
                padding: 20px 30px;
                border-radius: 10px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
                display: flex;
                align-items: center;
                gap: 15px;
                z-index: 10002;
                animation: slideInRight 0.3s ease-out;
                max-width: 400px;
            }
            
            .notification.success {
                border-left: 4px solid #D4AF37;
            }
            
            .notification.error {
                border-left: 4px solid #dc3545;
            }
            
            .notification i {
                font-size: 24px;
            }
            
            .notification.success i {
                color: #D4AF37;
            }
            
            .notification.error i {
                color: #dc3545;
            }
            
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
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Gallery Lightbox
const galleryItems = document.querySelectorAll('.gallery-item');
const lightbox = document.getElementById('lightbox');
const lightboxImage = document.getElementById('lightbox-image');
const lightboxClose = document.querySelector('.lightbox-close');
const lightboxPrev = document.querySelector('.lightbox-prev');
const lightboxNext = document.querySelector('.lightbox-next');

let currentImageIndex = 0;
const images = Array.from(galleryItems).map(item => item.querySelector('img').src);

galleryItems.forEach((item, index) => {
    item.addEventListener('click', () => {
        currentImageIndex = index;
        openLightbox();
    });
});

function openLightbox() {
    lightbox.classList.add('active');
    lightboxImage.src = images[currentImageIndex];
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
}

lightboxClose.addEventListener('click', closeLightbox);

lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
        closeLightbox();
    }
});

lightboxPrev.addEventListener('click', (e) => {
    e.stopPropagation();
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    lightboxImage.src = images[currentImageIndex];
});

lightboxNext.addEventListener('click', (e) => {
    e.stopPropagation();
    currentImageIndex = (currentImageIndex + 1) % images.length;
    lightboxImage.src = images[currentImageIndex];
});

// Keyboard navigation for lightbox
document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    
    if (e.key === 'ArrowLeft') {
        lightboxPrev.click();
    } else if (e.key === 'ArrowRight') {
        lightboxNext.click();
    } else if (e.key === 'Escape') {
        closeLightbox();
    }
});

// Smooth scroll with offset for fixed navbar
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#' || href === '') return;
        
        e.preventDefault();
        const target = document.querySelector(href);
        
        if (target) {
            const offsetTop = target.offsetTop - 80; // Navbar height
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Animate elements on scroll
document.querySelectorAll('.specialty-card, .schedule-card, .service-card, .gallery-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    observer.observe(el);
});

// Counter animation for hero stats
const statNumbers = document.querySelectorAll('.stat-number');
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const target = entry.target;
            const finalValue = parseInt(target.textContent);
            animateCounter(target, 0, finalValue, 2000);
            statsObserver.unobserve(target);
        }
    });
}, { threshold: 0.5 });

statNumbers.forEach(stat => statsObserver.observe(stat));

function animateCounter(element, start, end, duration) {
    const startTime = performance.now();
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        const current = Math.floor(start + (end - start) * easeOutQuart);
        
        element.textContent = current;
        
        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.textContent = end;
        }
    }
    
    requestAnimationFrame(update);
}

// Parallax effect for hero
let parallaxOffset = 0;
window.addEventListener('scroll', () => {
    parallaxOffset = window.scrollY * 0.5;
    document.querySelector('.hero-bg').style.transform = `translateY(${parallaxOffset}px)`;
});

// Button ripple effect
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');
        
        // Add ripple styles if not already added
        if (!document.getElementById('ripple-styles')) {
            const style = document.createElement('style');
            style.id = 'ripple-styles';
            style.textContent = `
                .btn {
                    position: relative;
                    overflow: hidden;
                }
                
                .ripple {
                    position: absolute;
                    border-radius: 50%;
                    background: rgba(255, 255, 255, 0.6);
                    transform: scale(0);
                    animation: rippleEffect 0.6s ease-out;
                    pointer-events: none;
                }
                
                @keyframes rippleEffect {
                    to {
                        transform: scale(4);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }
        
        this.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
});

// 3D tilt effect for cards
document.querySelectorAll('.specialty-card, .service-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 10;
        const rotateY = (centerX - x) / 10;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
});

// Set minimum date for reservation form
const today = new Date().toISOString().split('T')[0];
const dateInput = document.querySelector('#reservation-form input[type="date"]');
if (dateInput) {
    dateInput.setAttribute('min', today);
}

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimized scroll event
const optimizedScroll = debounce(() => {
    // Navbar scroll effect
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    
    // Active nav link
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (window.scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });
    
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}, 10);

window.addEventListener('scroll', optimizedScroll);

// Console welcome message
console.log('%c🌟 Добродошли у Ресторан Златар! 🌟', 'font-size: 20px; color: #D4AF37; font-weight: bold;');
console.log('%c40 година традиције | Од 1985.', 'font-size: 14px; color: #1a3a1a;');
console.log('%cИзрада сајта: Web Studio Link', 'font-size: 12px; color: #6c757d;');
