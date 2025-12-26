import codecs
import re

# Комплетан mobile CSS који недостаје
additional_mobile_css = '''
            .nav-item {
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
            }'''

# Процесуј све blog-post странице
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Провери да ли већ има body.menu-open стил
        if 'body.menu-open' not in content:
            # Пронађи место где је @media (max-width: 1281px) и .nav-toggle.active
            # Додај нови CSS одмах после .nav-toggle.active span:nth-child(3)
            pattern = r'(\.nav-toggle\.active span:nth-child\(3\) \{[^}]+\})'
            
            if re.search(pattern, content):
                replacement = r'\1' + additional_mobile_css
                content = re.sub(pattern, replacement, content)
                
                print(f"✓ Додат mobile menu CSS у {filename}")
                
                # Запиши ажуриран садржај
                with codecs.open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                print(f"⚠ Није пронађена локација за CSS у {filename}")
        else:
            print(f"⏭ {filename} већ има body.menu-open CSS")
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Додат комплетан mobile menu CSS на све blog-post странице.")
