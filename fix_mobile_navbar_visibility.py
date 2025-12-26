import codecs
import re

# CSS који сакрива desktop navbar елементе на мобилном
hide_desktop_nav_css = '''
        @media (max-width: 1281px) {
            .nav-menu {
                display: none !important;
            }
            
            .nav-menu.mobile-active {
                display: flex !important;
                position: fixed !important;
                top: 200px !important;
                right: 0px !important;
                width: 320px !important;
                height: calc(100vh - 200px) !important;
                background: linear-gradient(180deg, rgba(20,15,8,0.98) 0%, rgba(35,26,15,0.97) 50%, rgba(25,18,10,0.96) 100%) !important;
                backdrop-filter: blur(40px) !important;
                padding: 2rem !important;
                flex-direction: column !important;
                gap: 0.5rem !important;
                z-index: 1000 !important;
                overflow-y: auto !important;
                box-shadow: -8px 0 32px rgba(0,0,0,0.5) !important;
            }
'''

# Ажурирај JavaScript да користи mobile-active класу
mobile_nav_js_updated = '''        // Mobile Menu Toggle
        const navToggle = document.getElementById('navToggle');
        const navMenu = document.getElementById('navMenu');
        const body = document.body;
        
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('mobile-active');
            body.classList.toggle('menu-open');
        });
        
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('mobile-active');
                body.classList.remove('menu-open');
            });
        });'''

# Процесуј све blog и blog-post странице
files = ['blog.html'] + [f'blog-post-{i}.html' for i in range(1, 13)]

for filename in files:
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # 1. Замени стари mobile nav CSS са новим
        # Тражи @media (max-width: 1281px) блок и замени га
        old_css_pattern = r'@media \(max-width: 1281px\) \{[\s\S]*?\.nav-toggle \{[\s\S]*?\}[\s\S]*?\.nav-toggle span \{[\s\S]*?\}[\s\S]*?\.nav-actions \{[\s\S]*?\}[\s\S]*?\.btn-reserve \{[\s\S]*?\}[\s\S]*?\.nav-toggle\.active span:nth-child\(1\)[\s\S]*?\}[\s\S]*?\.nav-toggle\.active span:nth-child\(2\)[\s\S]*?\}[\s\S]*?\.nav-toggle\.active span:nth-child\(3\)[\s\S]*?\}[\s\S]*?\.nav-link \{[\s\S]*?\}[\s\S]*?body\.menu-open \{[\s\S]*?\}[\s\S]*?body\.menu-open::before \{[\s\S]*?\}[\s\S]*?@keyframes fadeIn \{[\s\S]*?\}[\s\S]*?\.btn-reserve \{[\s\S]*?\}[\s\S]*?\.btn-reserve i \{[\s\S]*?\}[\s\S]*?\.btn-reserve span \{[\s\S]*?\}[\s\S]*?\}'
        
        if re.search(old_css_pattern, content):
            # Уклони стари блок
            content = re.sub(old_css_pattern, '', content)
            modified = True
        
        # 2. Додај нови CSS пре @media (min-width: 1282px)
        if '@media (min-width: 1282px)' in content and '.nav-menu.mobile-active' not in content:
            content = content.replace('@media (min-width: 1282px)', hide_desktop_nav_css + '\n        @media (min-width: 1282px)')
            print(f"✓ Додат нови mobile nav CSS у {filename}")
            modified = True
        
        # 3. Замени JavaScript да користи mobile-active класу
        old_js_pattern = r'// Mobile Menu Toggle[\s\S]*?navToggle\.addEventListener\([\s\S]*?\}\);[\s\S]*?navLinks\.forEach\([\s\S]*?\}\);'
        
        if re.search(old_js_pattern, content):
            content = re.sub(old_js_pattern, mobile_nav_js_updated, content)
            print(f"✓ Ажуриран mobile nav JavaScript у {filename}")
            modified = True
        
        if modified:
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {filename} ажуриран\n")
        else:
            print(f"⏭ {filename} - није требало мењати\n")
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\n🎉 ЗАВРШЕНО! Desktop navbar сакривен на мобилном, mobile menu користи mobile-active класу!")
