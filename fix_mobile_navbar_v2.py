import re
import codecs

# CSS to add - hide nav-actions on mobile in navbar, show in mobile menu
mobile_navbar_fix = """
    @media (max-width: 1281px) {
        /* Hide navbar nav-actions on mobile (they appear in mobile menu instead) */
        .navbar .nav-actions {
            position: fixed !important;
            right: 1rem !important;
            top: 1rem !important;
            padding: 0 !important;
            margin: 0 !important;
            width: auto !important;
            background: transparent !important;
        }
        
        .navbar .language-switcher,
        .navbar .btn-reserve {
            display: none !important;
        }
        
        .navbar .nav-toggle {
            display: flex !important;
            position: relative !important;
            z-index: 1001 !important;
        }
        
        .navbar .nav-logo {
            padding-right: 0 !important;
        }
        
        /* Show nav-actions inside mobile menu */
        .nav-menu.mobile-active .language-switcher,
        .nav-menu.mobile-active .btn-reserve {
            display: flex !important;
        }
    }
"""

print("🔧 Поправљам mobile navbar на blog-post страницама...\n")

for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the fix already exists
        if '.navbar .nav-actions {' in content and '@media (max-width: 1281px)' in content and 'position: fixed !important;' in content:
            print(f"⚠ {filename} већ има mobile navbar fix")
            continue
        
        # Simply add before </style>
        content = content.replace('    </style>', mobile_navbar_fix + '\n    </style>')
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Поправљен mobile navbar у {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ Готово!")
print("\nПромене:")
print("  ✓ Language switcher и Резервација дугме сакривени у navbar-у на мобилном")
print("  ✓ Приказују се само кроз hamburger мени")
print("  ✓ Hamburger икона сада видљива горе десно")
