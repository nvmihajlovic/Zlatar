import codecs
import re

# CSS за nav-menu на мобилном
mobile_nav_menu_css = '''
        @media (max-width: 1281px) {
            .nav-menu {
                position: fixed !important;
                top: 200px !important;
                right: -320px !important;
                width: 320px !important;
                height: calc(100vh - 200px) !important;
                background: linear-gradient(180deg, rgba(20,15,8,0.98) 0%, rgba(35,26,15,0.97) 50%, rgba(25,18,10,0.96) 100%) !important;
                backdrop-filter: blur(40px) !important;
                padding: 2rem !important;
                flex-direction: column !important;
                gap: 0.5rem !important;
                transition: right 0.4s ease-in-out !important;
                z-index: 1000 !important;
                overflow-y: auto !important;
                box-shadow: -8px 0 32px rgba(0,0,0,0.5) !important;
            }
            
            .nav-menu.active {
                right: 0px !important;
            }
        }
'''

# Ажурирај JavaScript да додаје .active класу уместо inline стилова
mobile_nav_js_updated = '''
        // Mobile Menu Toggle
        const navToggle = document.getElementById('navToggle');
        const navMenu = document.getElementById('navMenu');
        const body = document.body;
        
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            body.classList.toggle('menu-open');
        });
        
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                body.classList.remove('menu-open');
            });
        });'''

# Листа фајлова
files = ['blog.html'] + [f'blog-post-{i}.html' for i in range(1, 13)]

for filename in files:
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # 1. Додај CSS за .nav-menu.active ако га нема
        if '.nav-menu.active' not in content:
            # Пронађи где је @media (max-width: 1281px) и додај после .nav-toggle стилова
            pattern = r'(@media \(max-width: 1281px\) \{[^}]*\.nav-toggle \{[^}]+\})'
            if re.search(pattern, content, re.DOTALL):
                # Пронађи крај тог @media блока и додај нови CSS пре њега
                # Једноставније: додај пре @media (min-width: 1282px)
                if '@media (min-width: 1282px)' in content:
                    content = content.replace('@media (min-width: 1282px)', mobile_nav_menu_css + '\n        @media (min-width: 1282px)')
                    print(f"✓ Додат .nav-menu.active CSS у {filename}")
                    modified = True
        
        # 2. Замени стари JavaScript са новим
        old_js_pattern = r"navToggle\.addEventListener\('click', \(\) => \{[\s\S]*?if \(window\.innerWidth <= 1281\)[\s\S]*?\}\s*\}\);[\s\S]*?navLinks\.forEach\(link => \{[\s\S]*?\}\);"
        
        if re.search(old_js_pattern, content):
            content = re.sub(old_js_pattern, mobile_nav_js_updated, content)
            print(f"✓ Замењен mobile nav JavaScript у {filename}")
            modified = True
        
        if modified:
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"⏭ {filename} - није требало мењати или већ ажурирано")
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Mobile menu JavaScript и CSS ажурирани.")
