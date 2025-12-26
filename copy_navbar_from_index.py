import re
import codecs

# Read navbar from index.html
with codecs.open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract navbar from index.html (from <!-- Navigation --> to </nav>)
navbar_pattern = r'(<!-- Navigation -->\s*<nav class="navbar".*?</nav>)'
navbar_match = re.search(navbar_pattern, index_content, re.DOTALL)

if not navbar_match:
    print("✗ Нисам пронашао navbar у index.html")
    exit(1)

navbar_html = navbar_match.group(1)

# Modify navbar for blog-post pages
# Change #hero to index.html in nav-logo href
navbar_html = navbar_html.replace('href="#hero" class="nav-logo"', 'href="index.html" class="nav-logo"')

# Change #hero to index.html in first nav-link (Почетна)
navbar_html = re.sub(
    r'(<li class="nav-item"><a href=")#hero(" class="nav-link active")',
    r'\1index.html\2',
    navbar_html
)

# Remove "active" class from Почетна link (it should not be active on blog-post pages)
navbar_html = navbar_html.replace('class="nav-link active"', 'class="nav-link"')

# Remove onclick from button and make it just id
navbar_html = re.sub(
    r'(<button class="btn btn-primary btn-lg" onclick=".*?")',
    r'<button class="btn btn-primary btn-lg"',
    navbar_html
)

print("✓ Извучен navbar из index.html")
print("\nНавбар садржи:")
print("  - Лого")
print("  - 7 navigation links")
print("  - Language switcher (RS, GB, RU)")
print("  - Резервација дугме")
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
            print(f"✓ Ажуриран navbar у {filename}")
        else:
            print(f"⚠ Navbar није промењен у {filename} (можда већ постоји исти)")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ Завршено!")
print("Navbar је копиран са index.html на све blog-post странице.")
print("Укључени су language switcher (RS, GB, RU) и сви елементи навбара.")
