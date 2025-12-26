import re
import codecs

print("🔧 Уклањам inline стилове са nav-menu...\n")

files = ['blog.html'] + [f'blog-post-{i}.html' for i in range(1, 13)]

for filename in files:
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove inline style from nav-menu
        content = re.sub(
            r'(<ul class="nav-menu" id="navMenu") style="[^"]*"',
            r'\1',
            content
        )
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Уклоњен inline style из {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("\nmobile-nav.css сада контролише nav-menu комплетно.")
