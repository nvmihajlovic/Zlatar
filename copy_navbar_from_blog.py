import re
import codecs

# Read navbar from blog.html
with codecs.open('blog.html', 'r', encoding='utf-8') as f:
    blog_content = f.read()

# Extract navbar (from <!-- Navigation --> to </nav>)
navbar_pattern = r'(<!-- Navigation -->\s*<nav class="navbar".*?</nav>)'
navbar_match = re.search(navbar_pattern, blog_content, re.DOTALL)

if not navbar_match:
    print("✗ Нисам пронашао navbar у blog.html")
    exit(1)

navbar_html = navbar_match.group(1)

print("✓ Извучен navbar из blog.html")
print("\nNavbar садржи:")
print("  - Лого")
print("  - 7 navigation links")
print("  - Резервација дугме (БЕЗ language switcher-а)")
print("  - Mobile nav toggle")

# Process all blog-post files
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace navbar (from <!-- Navigation --> or <nav to </nav>)
        old_navbar_pattern = r'(<!-- Navigation -->\s*)?<nav class="navbar".*?</nav>'
        new_content = re.sub(old_navbar_pattern, navbar_html, content, flags=re.DOTALL, count=1)
        
        if new_content != content:
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Копиран navbar у {filename}")
        else:
            print(f"⚠ Navbar није промењен у {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("Navbar са blog.html је копиран на све blog-post странице.")
print("БЕЗ language switcher-а, само резервација дугме и hamburger.")
