import re
import codecs

print("🔧 Додајем mobile-nav.css и new-style.css на blog-post странице...\n")

for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if mobile-nav.css already exists
        if 'mobile-nav.css' in content:
            print(f"⚠ {filename} већ има mobile-nav.css")
            continue
        
        # Find the Google Fonts link and add our CSS after it
        pattern = r'(href="https://fonts\.googleapis\.com/css2\?family=Montserrat.*?" rel="stylesheet">)'
        replacement = r'\1\n    \n    <!-- Styles -->\n    <link rel="stylesheet" href="new-style.css">\n    <link rel="stylesheet" href="mobile-nav.css">'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Додати CSS linkови у {filename}")
        else:
            print(f"⚠ Није пронађен патерн у {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("\nДодати CSS фајлови:")
print("  ✓ new-style.css - главни стилови")
print("  ✓ mobile-nav.css - mobile navigation стилови")
