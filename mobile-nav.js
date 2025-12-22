// Mobilni Navbar - Jednostavan JavaScript

(function() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    let navBlur = document.querySelector('.nav-blur');
    
    // Kreiraj blur element ako ne postoji
    if (!navBlur) {
        navBlur = document.createElement('div');
        navBlur.className = 'nav-blur';
        document.body.appendChild(navBlur);
    }
    
    // Toggle meni
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            navBlur.classList.toggle('active');
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });
    }
    
    // Zatvori meni klikom na blur
    navBlur.addEventListener('click', function() {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
        navBlur.classList.remove('active');
        document.body.style.overflow = '';
    });
    
    // Zatvori meni klikom na link
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
            navBlur.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
    
    // Zatvori meni klikom na logo
    const navLogo = document.querySelector('.nav-logo');
    if (navLogo) {
        navLogo.addEventListener('click', function() {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
            navBlur.classList.remove('active');
            document.body.style.overflow = '';
        });
    }
})();
