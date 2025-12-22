import re

# CSS za mobilni meni sa index.html (right side)
mobile_menu_css_right = """            .nav-toggle {
                display: flex !important;
                flex-direction: column !important;
                gap: 6px !important;
                background: rgba(255,255,255,0.08) !important;
                border: 1px solid rgba(255,255,255,0.12) !important;
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
            @keyframes slideInRight {
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
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
            .language-switcher {
                display: none !important;
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
            }"""

# CSS za left side (sve ostale stranice)
mobile_menu_css_left = mobile_menu_css_right.replace('right: -320px', 'left: -320px').replace('right: 0 !important;', 'left: 0 !important;').replace('slideInRight', 'slideInLeft').replace('translateX(30px)', 'translateX(-30px)').replace('box-shadow: -8px', 'box-shadow: 8px').replace('transition: right 0.4s ease-in-out, top 0.4s ease-in-out', 'transition: left 0.4s ease-in-out, top 0.4s ease-in-out')

# Dodaj i slideInLeft keyframes
mobile_menu_css_left = mobile_menu_css_left.replace('@keyframes slideInLeft {', '@keyframes slideInLeft {')

pages = ['about.html', 'contact.html', 'gallery.html', 'menu.html', 'wine.html', 'privacy.html', 'sitemap.html', 'terms.html']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pronađi poslednji @media (max-width: 768px) blok
        matches = list(re.finditer(r'@media \(max-width: 768px\) \{', content))
        if not matches:
            print(f"Nema @media bloka u {page}")
            continue
            
        last_match = matches[-1]
        start_pos = last_match.start()
        
        # Pronađi početak mobilnog meni CSS-a (.nav-toggle {)
        nav_toggle_match = re.search(r'\.nav-toggle \{', content[start_pos:])
        if not nav_toggle_match:
            print(f"Nema .nav-toggle u {page}")
            continue
        
        menu_start = start_pos + nav_toggle_match.start()
        
        # Pronađi kraj mobilnog meni CSS-a (pre sledećeg sekcijskog CSS-a ili kraja @media bloka)
        # Tražimo početak sledećeg CSS bloka koji nije deo menija
        rest_content = content[menu_start:]
        
        # Pronađi sve moguće krajeve (drugi veliki CSS blokovi ili kraj @media)
        hero_match = re.search(r'/\* Hero Section Mobile \*/', rest_content)
        
        if hero_match:
            menu_end = menu_start + hero_match.start()
        else:
            # Ako nema Hero Section komentara, traži samo prvi sledeći main CSS blok
            # Ali to je komplikovano, hajde da jednostavno pronađemo kraj .btn-reserve span bloka
            btn_span_match = re.search(r'\.btn-reserve span \{[^}]+\}', rest_content)
            if btn_span_match:
                menu_end = menu_start + btn_span_match.end() + 1
                # Dodaj dodatnih par linija za sigurnost
                while menu_end < len(content) and content[menu_end] in ['\n', ' ', '\r']:
                    menu_end += 1
            else:
                print(f"Ne mogu naći kraj mobilnog menija u {page}")
                continue
        
        # Zameni stari mobilni meni CSS sa novim
        new_content = content[:menu_start] + mobile_menu_css_left + '\n            \n            ' + content[menu_end:]
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ {page} - mobilni meni ažuriran")
        
    except Exception as e:
        print(f"✗ {page} - greška: {e}")

print("\nGotovo!")
