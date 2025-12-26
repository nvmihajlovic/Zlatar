import re
import codecs

print("🔧 Уклањам inline display стилове из navbar-а...\n")

for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find navbar section and remove inline display styles from nav-actions, language-switcher, and btn-reserve
        # But keep them on nav-toggle
        
        # Remove style="display: flex..." from nav-actions div
        content = re.sub(
            r'(<div class="nav-actions") style="display: flex;([^"]*)"',
            r'\1 style="\2"',
            content
        )
        
        # Remove style="display: flex..." from language-switcher div
        content = re.sub(
            r'(<div class="language-switcher") style="display: flex;([^"]*)"',
            r'\1 style="\2"',
            content
        )
        
        # Clean up empty style attributes
        content = re.sub(
            r' style=""',
            '',
            content
        )
        
        # Clean up style with only whitespace
        content = re.sub(
            r' style="\s*"',
            '',
            content
        )
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Уклоњени inline display стилови из {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ Готово!")
print("\nПромене:")
print("  ✓ Уклоњени inline display:flex стилови из nav-actions")
print("  ✓ Уклоњени inline display:flex стилови из language-switcher")
print("  ✓ CSS сада контролише приказивање на desktop и mobile")
