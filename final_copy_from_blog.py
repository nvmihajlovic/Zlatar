import re
import codecs

print("🔧 Копирам head и navbar са blog.html на blog-post странице...\n")

# Read blog.html
with codecs.open('blog.html', 'r', encoding='utf-8') as f:
    blog_content = f.read()

# Extract the styles section (everything from <style> to </style>)
styles_pattern = r'(<style>.*?</style>)'
styles_match = re.search(styles_pattern, blog_content, re.DOTALL)

if not styles_match:
    print("✗ Нисам пронашао <style> у blog.html")
    exit(1)

blog_styles = styles_match.group(1)

# Extract navbar
navbar_pattern = r'(<!-- Navigation -->.*?</nav>)'
navbar_match = re.search(navbar_pattern, blog_content, re.DOTALL)

if not navbar_match:
    print("✗ Нисам пронашао navbar у blog.html")
    exit(1)

blog_navbar = navbar_match.group(1)

print("✓ Извучени стилови и navbar из blog.html\n")

# Now update each blog-post file
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire <style> section with blog.html styles
        content = re.sub(
            r'<style>.*?</style>',
            blog_styles,
            content,
            flags=re.DOTALL
        )
        
        # Replace navbar
        content = re.sub(
            r'(<!-- Navigation -->.*?</nav>)',
            blog_navbar,
            content,
            flags=re.DOTALL
        )
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Копирани стилови и navbar у {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("\nКопирано:")
print("  ✓ Комплетни <style> из blog.html")
print("  ✓ Комплетан navbar из blog.html")
print("  ✓ CSS линкови су исти (mobile-nav.css, new-style.css)")
