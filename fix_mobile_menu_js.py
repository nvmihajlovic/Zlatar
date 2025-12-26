import re
import codecs

print("🔧 Поправљам JavaScript за mobile menu...\n")

# Correct JavaScript for mobile menu
correct_js = """        // Mobile Menu Toggle
        const navToggle = document.getElementById('navToggle');
        const navMenu = document.getElementById('navMenu');
        const body = document.body;
        
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            body.classList.toggle('menu-open');
        });
        
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                body.classList.remove('menu-open');
            });
        });"""

for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace mobile menu toggle JavaScript
        old_pattern = r'// Mobile Menu Toggle\s+const navToggle.*?body\.classList\.remove\(\'menu-open\'\);\s+\}\);\s+\}\);'
        
        new_content = re.sub(old_pattern, correct_js, content, flags=re.DOTALL)
        
        if new_content != content:
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Поправљен JavaScript у {filename}")
        else:
            print(f"⚠ Није пронађен патерн у {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("\nПромене:")
print("  ✓ JavaScript сада користи .active класу (уместо .mobile-active)")
print("  ✓ Усклађено са mobile-nav.css")
