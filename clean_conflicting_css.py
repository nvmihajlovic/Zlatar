import re
import codecs

print("🔧 Уклањам конфликтне mobile nav стилове из <style> блока...\n")

# Process blog.html first
files = ['blog.html'] + [f'blog-post-{i}.html' for i in range(1, 13)]

for filename in files:
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove all @media (max-width: 1281px) blocks from <style> section
        # These conflict with mobile-nav.css
        content = re.sub(
            r'@media \(max-width: 1281px\) \{[^\}]*\.nav-menu[^\}]*\{[^\}]*\}[^\}]*\}',
            '',
            content,
            flags=re.DOTALL
        )
        
        content = re.sub(
            r'@media \(min-width: 1282px\) \{[^\}]*\.nav-toggle[^\}]*\}',
            '',
            content
        )
        
        # Remove duplicate @media blocks
        content = re.sub(
            r'(@media \(max-width: 1281px\).*?)\1+',
            r'\1',
            content,
            flags=re.DOTALL
        )
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Очишћен {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("\nУклоњени конфликтни стилови из <style> блока.")
print("mobile-nav.css сада контролише mobile menu.")
