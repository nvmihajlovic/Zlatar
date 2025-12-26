#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob

# Navbar HTML sa index stranice
navbar_html = '''    <!-- Navigation -->
    <nav class="navbar" id="navbar" style="display: flex; align-items: center; background: linear-gradient(180deg, rgba(20,15,8,0.97) 0%, rgba(35,26,15,0.95) 50%, rgba(25,18,10,0.93) 100%); backdrop-filter: blur(30px) saturate(180%); border-bottom: 1px solid transparent; border-image: linear-gradient(90deg, transparent 0%, rgba(212,175,55,0.4) 30%, rgba(255,215,0,0.3) 50%, rgba(212,175,55,0.4) 70%, transparent 100%) 1; box-shadow: 0 8px 32px rgba(0,0,0,0.4), 0 4px 16px rgba(212,175,55,0.08), inset 0 1px 0 rgba(255,255,255,0.06), inset 0 -1px 0 rgba(212,175,55,0.1); position: fixed; top: 0; left: 0; right: 0; z-index: 1000; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); justify-content: center;">
        <div class="nav-container" style="display: flex; align-items: center; justify-content: space-between; max-width: 1400px; width: 100%; padding: 0.5rem 1.5rem;">
            <a href="index.html" class="nav-logo" style="display: flex; align-items: center; transition: transform 0.3s; margin-right: auto; padding-right: 3rem;">
                <img src="images/znak-restoran-zlatar-vektorski_clipped_rev_1.png" alt="Ресторан Златар" class="logo-img" style="height: 68px; width: auto; filter: drop-shadow(0 2px 8px rgba(212,175,55,0.3));">
            </a>
            
            <ul class="nav-menu" id="navMenu" style="display: flex; align-items: center; gap: 1.4rem;">
                <li class="nav-item"><a href="index.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span data-i18n="nav.home">Почетна</span></a></li>
                <li class="nav-item"><a href="about.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span data-i18n="nav.about">О нама</span></a></li>
                <li class="nav-item"><a href="menu.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span data-i18n="nav.menu">Јеловник</span></a></li>
                <li class="nav-item"><a href="wine.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span data-i18n="nav.wine">Винска карта</span></a></li>
                <li class="nav-item"><a href="blog.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span data-i18n="nav.blog">Блог</span></a></li>
                <li class="nav-item"><a href="gallery.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span data-i18n="nav.gallery">Галерија</span></a></li>
                <li class="nav-item"><a href="contact.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span data-i18n="nav.contact">Контакт</span></a></li>
            </ul>
            
            <div class="nav-actions" style="display: flex; align-items: center; gap: 1.5rem; margin-left: auto; padding-left: 3rem;">
                <div class="language-switcher" style="display: flex; align-items: center; gap: 0.5rem; background: rgba(255,255,255,0.08); backdrop-filter: blur(15px) saturate(150%); padding: 0.5rem 0.9rem; border-radius: 50px; border: 1px solid rgba(255,255,255,0.15); box-shadow: 0 4px 20px rgba(0,0,0,0.15), inset 0 1px 0 rgba(255,255,255,0.08);">
                    <button class="lang-btn active" data-lang="sr" style="background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.15)); border: 1px solid rgba(212,175,55,0.4); color: #FFD700; font-weight: 600; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: 'Montserrat', sans-serif; letter-spacing: 0.5px;" title="Српски">RS</button>
                    <button class="lang-btn" data-lang="en" style="background: transparent; border: 1px solid rgba(255,255,255,0.12); color: rgba(255,255,255,0.6); font-weight: 500; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: 'Montserrat', sans-serif; letter-spacing: 0.5px;" title="English">GB</button>
                    <button class="lang-btn" data-lang="ru" style="background: transparent; border: 1px solid rgba(255,255,255,0.12); color: rgba(255,255,255,0.6); font-weight: 500; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: 'Montserrat', sans-serif; letter-spacing: 0.5px;" title="Русский">RU</button>
                </div>
                <button class="btn-reserve" id="btnReserve" style="background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); color: #fff; font-weight: 600; font-size: 0.9rem; padding: 0.75rem 1.8rem; border: none; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 6px 20px rgba(212,175,55,0.4), inset 0 1px 0 rgba(255,255,255,0.3); letter-spacing: 0.5px;">
                    <i class="fas fa-calendar-check" style="margin-right: 0.5rem;"></i>
                    <span data-i18n="nav.reserve">Резервација</span>
                </button>
                <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" style="margin-left: 0.5rem;">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </nav>'''

# Dodatni CSS stilovi za mobilni navbar
additional_css = '''
            /* Mobile Navigation */
            .nav-menu .nav-link {
                color: rgba(255,255,255,0.9) !important;
                background: rgba(255,255,255,0.06) !important;
                border: 1px solid rgba(255,255,255,0.1) !important;
                padding: 1rem 1.5rem !important;
                border-radius: 12px !important;
                font-size: 1rem !important;
                font-weight: 500 !important;
                text-decoration: none !important;
                display: block !important;
                transition: all 0.3s ease !important;
                width: 100% !important;
            }

            .nav-menu .nav-link.active,
            .nav-menu .nav-link:hover {
                background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.15)) !important;
                border-color: rgba(212,175,55,0.4) !important;
                color: #FFD700 !important;
            }

            .nav-menu {
                position: fixed !important;
                display: flex !important;
                top: 0 !important;
                right: -320px !important;
                width: 320px !important;
                height: 100vh !important;
                background: linear-gradient(180deg, rgba(20,15,8,0.98) 0%, rgba(35,26,15,0.97) 50%, rgba(25,18,10,0.96) 100%) !important;
                backdrop-filter: blur(40px) !important;
                padding: 6rem 2rem 2rem 2rem !important;
                flex-direction: column !important;
                gap: 0.5rem !important;
                transition: right 0.4s ease-in-out, top 0.4s ease-in-out !important;
                z-index: 1000 !important;
                overflow-y: auto !important;
                box-shadow: -8px 0 32px rgba(0,0,0,0.5) !important;
            }

            .nav-menu.active {
                right: 0 !important;
                top: 130px !important;
                height: calc(100vh - 130px) !important;
            }

            .nav-menu .nav-item {
                width: 100%;
                opacity: 0;
                transform: translateX(30px);
            }

            .nav-menu.active .nav-item {
                animation: slideInRight 0.4s ease-out forwards;
            }

            .nav-menu.active .nav-item:nth-child(1) { animation-delay: 0.1s; }
            .nav-menu.active .nav-item:nth-child(2) { animation-delay: 0.15s; }
            .nav-menu.active .nav-item:nth-child(3) { animation-delay: 0.2s; }
            .nav-menu.active .nav-item:nth-child(4) { animation-delay: 0.25s; }
            .nav-menu.active .nav-item:nth-child(5) { animation-delay: 0.3s; }
            .nav-menu.active .nav-item:nth-child(6) { animation-delay: 0.35s; }
            .nav-menu.active .nav-item:nth-child(7) { animation-delay: 0.4s; }

            @keyframes slideInRight {
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
            '''

# CSS stilovi za nav-toggle unutar @media (max-width: 1281px)
nav_toggle_css = '''        /* Mobile Navigation Styles */
        @media (max-width: 1281px) {
            .nav-item .nav-link {
                display: block !important;
                width: 100% !important;
                padding: 1rem 1.5rem !important;
                font-size: 1.05rem !important;
            }

            .nav-toggle {
                display: flex !important;
                flex-direction: column;
                justify-content: space-around;
                width: 44px;
                height: 44px;
                background: rgba(255,255,255,0.08) !important;
                backdrop-filter: blur(10px) !important;
                border: 1px solid rgba(255,255,255,0.2) !important;
                border-radius: 12px !important;
                padding: 10px !important;
                cursor: pointer;
                z-index: 1001;
                position: fixed;
                right: 1.5rem;
                top: 1.75rem;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
                transition: all 0.3s ease !important;
            }

            .nav-toggle span {
                width: 24px;
                height: 2px;
                background: #D4AF37;
                border-radius: 2px;
                transition: all 0.3s;
                display: block;
            }

            .nav-toggle.active span:nth-child(1) {
                transform: rotate(45deg) translate(6px, 6px);
            }

            .nav-toggle.active span:nth-child(2) {
                opacity: 0;
            }

            .nav-toggle.active span:nth-child(3) {
                transform: rotate(-45deg) translate(6px, -6px);
            }

            .nav-actions {
                gap: 0 !important;
                padding-left: 0 !important;
            }

            .btn-reserve {
                position: fixed !important;
                right: 5.5rem !important;
                top: 1.5rem !important;
                z-index: 1001 !important;
                margin-left: 0 !important;
                font-size: 0 !important;
                padding: 0 !important;
                width: 48px !important;
                height: 48px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
            }

            .btn-reserve i {
                margin-right: 0 !important;
                font-size: 1.1rem !important;
            }

            .btn-reserve span {
                display: none !important;
            }

            body.menu-open {
                overflow: hidden;
            }
'''

# Dodatni CSS stilovi koji trebaju biti posle @media (max-width: 1281px) sekcije
hover_css = '''
        @media (min-width: 1282px) {
            .nav-toggle {
                display: none !important;
            }
        }
        
        .nav-link:hover {
            background: linear-gradient(135deg, rgba(212,175,55,0.25) 0%, rgba(212,175,55,0.15) 100%) !important;
            border-color: rgba(212,175,55,0.45) !important;
            color: #FFD700 !important;
            box-shadow: 0 8px 24px rgba(212,175,55,0.35), inset 0 1px 0 rgba(255,255,255,0.15) !important;
        }
        
        .nav-logo:hover {
            transform: scale(1.05) !important;
        }
        
        .lang-btn:hover {
            filter: grayscale(0) !important;
            opacity: 1 !important;
            transform: scale(1.2);
        }
        
        .lang-btn.active {
            filter: grayscale(0) !important;
            opacity: 1 !important;
            box-shadow: 0 0 20px rgba(212,175,55,0.5);
        }
        
        .btn-reserve:hover {
            transform: translateY(-2px) scale(1.03);
            box-shadow: 0 8px 30px rgba(212,175,55,0.6), inset 0 1px 0 rgba(255,255,255,0.4) !important;
            background: linear-gradient(135deg, #FFD700 0%, #D4AF37 100%) !important;
        }'''

# JavaScript kod za mobilni navbar
mobile_nav_js = '''    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const navToggle = document.getElementById('navToggle');
            const navMenu = document.getElementById('navMenu');
            const body = document.body;
            
            if (navToggle && navMenu) {
                navToggle.addEventListener('click', function() {
                    navToggle.classList.toggle('active');
                    body.classList.toggle('menu-open');
                    
                    if (window.innerWidth <= 1281) {
                        if (navToggle.classList.contains('active')) {
                            navMenu.style.right = '0px';
                        } else {
                            navMenu.style.right = '-320px';
                        }
                        
                        const langSwitcher = navMenu.querySelector('.language-switcher');
                        if (!langSwitcher && navToggle.classList.contains('active')) {
                            const desktopLangSwitcher = document.querySelector('.nav-actions .language-switcher');
                            if (desktopLangSwitcher) {
                                const langSwitcher = document.createElement('div');
                                langSwitcher.className = 'language-switcher';
                                langSwitcher.style.cssText = 'display: flex; align-items: center; gap: 0.5rem; background: rgba(255,255,255,0.08); backdrop-filter: blur(15px) saturate(150%); padding: 0.5rem 0.9rem; border-radius: 50px; border: 1px solid rgba(255,255,255,0.15); box-shadow: 0 4px 20px rgba(0,0,0,0.15), inset 0 1px 0 rgba(255,255,255,0.08); margin-top: 1rem; justify-content: center;';
                                
                                const btnSR = document.createElement('button');
                                btnSR.className = 'lang-btn' + (document.documentElement.lang === 'sr' ? ' active' : '');
                                btnSR.dataset.lang = 'sr';
                                btnSR.textContent = 'RS';
                                btnSR.style.cssText = document.documentElement.lang === 'sr' ? 
                                    'background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.15)); border: 1px solid rgba(212,175,55,0.4); color: #FFD700; font-weight: 600; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: \\'Montserrat\\', sans-serif; letter-spacing: 0.5px;' :
                                    'background: transparent; border: 1px solid rgba(255,255,255,0.12); color: rgba(255,255,255,0.6); font-weight: 500; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: \\'Montserrat\\', sans-serif; letter-spacing: 0.5px;';
                                
                                const btnEN = document.createElement('button');
                                btnEN.className = 'lang-btn' + (document.documentElement.lang === 'en' ? ' active' : '');
                                btnEN.dataset.lang = 'en';
                                btnEN.textContent = 'GB';
                                btnEN.style.cssText = document.documentElement.lang === 'en' ? 
                                    'background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.15)); border: 1px solid rgba(212,175,55,0.4); color: #FFD700; font-weight: 600; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: \\'Montserrat\\', sans-serif; letter-spacing: 0.5px;' :
                                    'background: transparent; border: 1px solid rgba(255,255,255,0.12); color: rgba(255,255,255,0.6); font-weight: 500; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: \\'Montserrat\\', sans-serif; letter-spacing: 0.5px;';
                                
                                const btnRU = document.createElement('button');
                                btnRU.className = 'lang-btn' + (document.documentElement.lang === 'ru' ? ' active' : '');
                                btnRU.dataset.lang = 'ru';
                                btnRU.textContent = 'RU';
                                btnRU.style.cssText = document.documentElement.lang === 'ru' ? 
                                    'background: linear-gradient(135deg, rgba(212,175,55,0.25), rgba(212,175,55,0.15)); border: 1px solid rgba(212,175,55,0.4); color: #FFD700; font-weight: 600; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: \\'Montserrat\\', sans-serif; letter-spacing: 0.5px;' :
                                    'background: transparent; border: 1px solid rgba(255,255,255,0.12); color: rgba(255,255,255,0.6); font-weight: 500; font-size: 0.8125rem; padding: 0.35rem 0.75rem; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: \\'Montserrat\\', sans-serif; letter-spacing: 0.5px;';
                                
                                btnSR.addEventListener('click', (e) => {
                                    e.preventDefault();
                                    if (typeof setLanguage === 'function') {
                                        setLanguage('sr');
                                    }
                                });
                                btnEN.addEventListener('click', (e) => {
                                    e.preventDefault();
                                    if (typeof setLanguage === 'function') {
                                        setLanguage('en');
                                    }
                                });
                                btnRU.addEventListener('click', (e) => {
                                    e.preventDefault();
                                    if (typeof setLanguage === 'function') {
                                        setLanguage('ru');
                                    }
                                });
                                
                                langSwitcher.appendChild(btnSR);
                                langSwitcher.appendChild(btnEN);
                                langSwitcher.appendChild(btnRU);
                                navMenu.appendChild(langSwitcher);
                            }
                        }
                        
                        navMenu.style.position = 'fixed';
                        navMenu.style.top = '200px';
                        navMenu.style.right = '0px';
                        navMenu.style.width = '320px';
                        navMenu.style.height = 'calc(100vh - 200px)';
                        navMenu.style.background = 'linear-gradient(180deg, rgba(20,15,8,0.98) 0%, rgba(35,26,15,0.97) 50%, rgba(25,18,10,0.96) 100%)';
                        navMenu.style.backdropFilter = 'blur(40px)';
                        navMenu.style.padding = '2rem';
                        navMenu.style.flexDirection = 'column';
                        navMenu.style.gap = '0.5rem';
                        navMenu.style.transition = 'right 0.4s ease-in-out';
                        navMenu.style.zIndex = '1000';
                        navMenu.style.overflowY = 'auto';
                        navMenu.style.boxShadow = '-8px 0 32px rgba(0,0,0,0.5)';
                        navMenu.style.display = 'flex';
                    }
                });
            }
            
            const navLinks = document.querySelectorAll('.nav-link');
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    navToggle.classList.remove('active');
                    body.classList.remove('menu-open');
                    if (window.innerWidth <= 1281) {
                        navMenu.style.right = '-320px';
                    }
                });
            });
        });
    </script>'''

def update_blog_post(filepath):
    """Ažurira blog post stranicu sa novim navbarom i stilovima"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Zameni navbar
        content = re.sub(
            r'<!-- Navigation -->.*?</nav>',
            navbar_html,
            content,
            flags=re.DOTALL
        )
        
        # Prvo, ukloni stare Mobile Navigation Styles sekcije ako postoje (bez @media upita)
        content = re.sub(
            r'/\* Mobile Navigation Styles \*/\s*\n\s*\.nav-item \.nav-link \{[\s\S]*?body\.menu-open \{\s*overflow: hidden;\s*\}',
            '',
            content
        )
        
        # Dodaj nov CSS za nav-toggle unutar @media (max-width: 1281px) pre zatvaranja @media (max-width: 768px)
        # Pronađi kraj @media (max-width: 768px) sekcije i dodaj nav-toggle stilove posle nje
        content = re.sub(
            r'(@media \(max-width: 768px\) \{[^}]*?\}\s*\})',
            r'\1\n\n' + nav_toggle_css,
            content
        )
        
        # Dodaj dodatne CSS stilove za mobilni meni u @media (max-width: 768px) - unutar Footer mobilni sekcije
        content = re.sub(
            r'(\s+/\* Footer mobilni \*/)',
            additional_css + r'\n\1',
            content
        )
        
        # Dodaj hover CSS stilove pre zatvaranja </style> taga
        content = re.sub(
            r'(\s+body\.menu-open \{[\s\S]*?\})\s+(</style>)',
            r'\1' + '\n            \n            body.menu-open::before {\n                content: \'\';\n                position: fixed;\n                top: 0;\n                left: 0;\n                width: 100%;\n                height: 100%;\n                background: rgba(0,0,0,0.7);\n                backdrop-filter: blur(4px);\n                z-index: 999;\n                animation: fadeIn 0.3s;\n            }\n            \n            @keyframes fadeIn {\n                from { opacity: 0; }\n                to { opacity: 1; }\n            }\n            \n            .nav-actions .language-switcher {\n                display: none !important;\n            }\n        }\n        ' + hover_css + '\n    ' + r'\2',
            content
        )
        
        # Zameni JavaScript kod za mobilni navbar
        content = re.sub(
            r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{[\s\S]*?// Reservation Modal',
            mobile_nav_js + '\n\n        // Reservation Modal',
            content
        )
        
        # Sačuvaj promene
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Ažuriran: {os.path.basename(filepath)}")
        return True
    except Exception as e:
        print(f"✗ Greška kod {os.path.basename(filepath)}: {str(e)}")
        return False

def main():
    # Pronađi sve blog post datoteke
    blog_posts = glob.glob('blog-post-*.html')
    
    if not blog_posts:
        print("Nisu pronađene blog post stranice!")
        return
    
    print(f"\n🔄 Pronađeno {len(blog_posts)} blog post stranica\n")
    
    success_count = 0
    for filepath in sorted(blog_posts):
        if update_blog_post(filepath):
            success_count += 1
    
    print(f"\n✅ Završeno! Uspešno ažurirano {success_count}/{len(blog_posts)} stranica\n")

if __name__ == '__main__':
    main()
