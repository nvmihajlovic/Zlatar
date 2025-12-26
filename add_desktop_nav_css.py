import re
import codecs

# CSS for desktop to show nav-actions properly
desktop_nav_css = """
    /* Desktop Navigation Styles */
    @media (min-width: 1282px) {
        .navbar .nav-actions {
            display: flex !important;
        }
        
        .navbar .language-switcher {
            display: flex !important;
        }
        
        .navbar .btn-reserve {
            display: inline-flex !important;
        }
    }
"""

print("🔧 Додајем desktop CSS за navbar...\n")

for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if desktop CSS already exists
        if '.navbar .nav-actions {' in content and 'display: flex !important;' in content and '@media (min-width: 1282px)' in content:
            # Find the existing block and update it
            pattern = r'@media \(min-width: 1282px\) \{[^\}]*\.nav-toggle[^\}]*\}'
            replacement = """@media (min-width: 1282px) {
        .nav-toggle {
            display: none !important;
        }
        
        .navbar .nav-actions {
            display: flex !important;
        }
        
        .navbar .language-switcher {
            display: flex !important;
        }
        
        .navbar .btn-reserve {
            display: inline-flex !important;
        }
    }"""
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        else:
            # Add before the mobile media query
            pattern = r'(@media \(max-width: 1281px\) \{)'
            content = re.sub(pattern, desktop_nav_css + r'\n    \1', content)
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Додат desktop CSS у {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ Готово!")
print("\nПромене:")
print("  ✓ Додат CSS за приказ nav-actions на desktop-у")
print("  ✓ Language switcher и Резервација сада раде на desktop и mobile")
