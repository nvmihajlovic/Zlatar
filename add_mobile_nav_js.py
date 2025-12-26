import codecs
import re

# JavaScript za mobile menu
mobile_nav_js = '''
        // Mobile Menu Toggle
        const navToggle = document.getElementById('navToggle');
        const navMenu = document.getElementById('navMenu');
        const body = document.body;
        
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            body.classList.toggle('menu-open');
            
            // Direktno manipulišemo stilovima na mobilnom
            if (window.innerWidth <= 1281) {
                if (navMenu.style.right === '0px') {
                    navMenu.style.right = '-320px';
                } else {
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
            }
        });
        
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                body.classList.remove('menu-open');
                if (window.innerWidth <= 1281) {
                    navMenu.style.right = '-320px';
                }
            });
        });'''

# CSS za mobile menu
mobile_nav_css = '''
        @media (max-width: 1281px) {
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
        }
        @media (min-width: 1282px) {
            .nav-toggle {
                display: none !important;
            }
        }'''

# Процесуј све blog-post странице
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Провери да ли већ има овај JavaScript
        if 'navToggle.addEventListener' not in content:
            # Пронађи крај JavaScript секције (пре затварајућег </script> тага на крају странице)
            # Тражи последњи </script> пре </body>
            last_script_pattern = r'(</script>\s*</body>)'
            if re.search(last_script_pattern, content):
                content = re.sub(last_script_pattern, mobile_nav_js + r'\n    </script>\n</body>', content)
                print(f"✓ Додат mobile nav JavaScript у {filename}")
            else:
                print(f"⚠ Није пронађена локација за JavaScript у {filename}")
        
        # Провери да ли већ има mobile CSS
        if '.nav-toggle.active span:nth-child(1)' not in content:
            # Пронађи последњи </style> пре краја
            style_pattern = r'(</style>\s*(?:</head>|<script))'
            if re.search(style_pattern, content):
                content = re.sub(style_pattern, mobile_nav_css + r'\n    </style>\n\n    <script', content, count=1)
                print(f"✓ Додат mobile nav CSS у {filename}")
            else:
                print(f"⚠ Није пронађена локација за CSS у {filename}")
        
        # Запиши ажуриран садржај
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Додат mobile navigation JavaScript и CSS на све blog-post странице.")
