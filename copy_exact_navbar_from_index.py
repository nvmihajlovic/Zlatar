import codecs
import re

# Тачан navbar HTML са index.html (без language switcher)
navbar_html = '''    <nav class="navbar" id="navbar" style="display: flex; align-items: center; background: linear-gradient(180deg, rgba(20,15,8,0.97) 0%, rgba(35,26,15,0.95) 50%, rgba(25,18,10,0.93) 100%); backdrop-filter: blur(30px) saturate(180%); border-bottom: 1px solid transparent; border-image: linear-gradient(90deg, transparent 0%, rgba(212,175,55,0.4) 30%, rgba(255,215,0,0.3) 50%, rgba(212,175,55,0.4) 70%, transparent 100%) 1; box-shadow: 0 8px 32px rgba(0,0,0,0.4), 0 4px 16px rgba(212,175,55,0.08), inset 0 1px 0 rgba(255,255,255,0.06), inset 0 -1px 0 rgba(212,175,55,0.1); position: fixed; top: 0; left: 0; right: 0; z-index: 1000; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); justify-content: center;">
        <div class="nav-container" style="display: flex; align-items: center; justify-content: space-between; max-width: 1400px; width: 100%; padding: 0.5rem 1.5rem;">
            <a href="index.html" class="nav-logo" style="display: flex; align-items: center; transition: transform 0.3s; margin-right: auto; padding-right: 3rem;">
                <img src="images/znak-restoran-zlatar-vektorski_clipped_rev_1.png" alt="Ресторан Златар" class="logo-img" style="height: 68px; width: auto; filter: drop-shadow(0 2px 8px rgba(212,175,55,0.3));">
            </a>
            
            <ul class="nav-menu" id="navMenu" style="display: flex; align-items: center; gap: 1.4rem;">
                <li class="nav-item"><a href="index.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Почетна</span></a></li>
                <li class="nav-item"><a href="about.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>О нама</span></a></li>
                <li class="nav-item"><a href="menu.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Јеловник</span></a></li>
                <li class="nav-item"><a href="wine.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Винска карта</span></a></li>
                <li class="nav-item"><a href="blog.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Блог</span></a></li>
                <li class="nav-item"><a href="gallery.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Галерија</span></a></li>
                <li class="nav-item"><a href="contact.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Контакт</span></a></li>
            </ul>
            
            <div class="nav-actions" style="display: flex; align-items: center; gap: 1.5rem; margin-left: auto; padding-left: 3rem;">
                <button class="btn-reserve" id="btnReserve" style="background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); color: #fff; font-weight: 600; font-size: 0.9rem; padding: 0.75rem 1.8rem; border: none; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 6px 20px rgba(212,175,55,0.4), inset 0 1px 0 rgba(255,255,255,0.3); letter-spacing: 0.5px;">
                    <i class="fas fa-calendar-check" style="margin-right: 0.5rem;"></i>
                    <span>Резервација</span>
                </button>
                <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" style="margin-left: 0.5rem;">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </nav>'''

# Тачан JavaScript са index.html
mobile_nav_js = '''        // Mobile Menu Toggle
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

# Тачан CSS са index.html
mobile_nav_css = '''        @media (max-width: 1281px) {
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
            .nav-link {
                width: 100%;
                text-align: left;
                padding: 1rem 1.5rem !important;
                font-size: 1.05rem !important;
            }
            body.menu-open {
                overflow: hidden;
            }
            body.menu-open::before {
                content: '';
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.7);
                backdrop-filter: blur(4px);
                z-index: 999;
                animation: fadeIn 0.3s;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            .btn-reserve {
                font-size: 0 !important;
                padding: 0 !important;
                width: 48px;
                height: 48px;
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
        }
        @media (min-width: 1282px) {
            .nav-toggle {
                display: none !important;
            }
        }'''

# Листа фајлова
files = ['blog.html'] + [f'blog-post-{i}.html' for i in range(1, 13)]

for filename in files:
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Замени navbar HTML
        nav_pattern = r'<nav class="navbar".*?</nav>'
        content = re.sub(nav_pattern, navbar_html, content, flags=re.DOTALL)
        print(f"✓ Замењен navbar HTML у {filename}")
        
        # 2. Уклони сав постојећи mobile nav JavaScript
        old_js_pattern = r'// Mobile Menu Toggle[\s\S]*?navMenu\.style\.right = [\'"]-320px[\'"]; *\} *\}\); *\} *\}\);'
        content = re.sub(old_js_pattern, '', content)
        
        # 3. Додај нови JavaScript пре Reservation Modal или на крај script секције
        if '// Reservation Modal Functionality' in content:
            content = content.replace('// Reservation Modal Functionality', mobile_nav_js + '\n\n        // Reservation Modal Functionality')
        else:
            # Нађи последњи </script> пре </body> и додај тамо
            last_script = content.rfind('</script>')
            if last_script != -1:
                content = content[:last_script] + '\n' + mobile_nav_js + '\n    </script>' + content[last_script+9:]
        print(f"✓ Додат mobile nav JavaScript у {filename}")
        
        # 4. Уклони стари mobile nav CSS
        old_css_patterns = [
            r'@media \(max-width: 1281px\) \{[\s\S]*?\.nav-menu\.active \{[\s\S]*?\}[\s\S]*?\}',
            r'@media \(max-width: 1281px\) \{[\s\S]*?body\.menu-open \{[\s\S]*?\}[\s\S]*?\}',
            r'\.nav-blur[\s\S]*?\}'
        ]
        for pattern in old_css_patterns:
            content = re.sub(pattern, '', content)
        
        # 5. Додај нови CSS пре @media (min-width: 1282px) или пре </style>
        if '@media (min-width: 1282px)' in content:
            content = content.replace('@media (min-width: 1282px)', mobile_nav_css + '\n        @media (min-width: 1282px)')
        else:
            # Додај пре последњег </style>
            last_style = content.rfind('</style>')
            if last_style != -1:
                content = content[:last_style] + '\n' + mobile_nav_css + '\n    </style>' + content[last_style+8:]
        print(f"✓ Додат mobile nav CSS у {filename}")
        
        # Запиши ажуриран садржај
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {filename} комплетно ажуриран\n")
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\n🎉 ЗАВРШЕНО! Navbar, CSS и JavaScript идентични као на index.html!")
