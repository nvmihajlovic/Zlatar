import codecs
import re

clean_mobile_js = '''
        // Mobile Menu Toggle
        const navToggle = document.getElementById('navToggle');
        const navMenu = document.getElementById('navMenu');
        
        if (navToggle && navMenu) {
            let navBlur = document.querySelector('.nav-blur');
            if (!navBlur) {
                navBlur = document.createElement('div');
                navBlur.className = 'nav-blur';
                document.body.appendChild(navBlur);
            }
            
            navToggle.addEventListener('click', () => {
                navToggle.classList.toggle('active');
                navMenu.classList.toggle('active');
                navBlur.classList.toggle('active');
                document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
            });
            
            navBlur.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                navBlur.classList.remove('active');
                document.body.style.overflow = '';
            });
            
            document.querySelectorAll('.nav-link').forEach(link => {
                link.addEventListener('click', () => {
                    navToggle.classList.remove('active');
                    navMenu.classList.remove('active');
                    navBlur.classList.remove('active');
                    document.body.style.overflow = '';
                });
            });
        }'''

# Процесуј све blog-post странице
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Уклони све постојеће mobile nav JS (може бити дупликат)
        # Тражи Mobile Menu Toggle секције
        pattern = r'// Mobile Menu Toggle[\s\S]*?navToggle\.classList\.toggle\([\'"]active[\'"]\);[\s\S]*?\}\);[\s\S]*?\}\);[\s\S]*?\}\);[\s\S]*?\}'
        
        # Избриши све инстанце
        content = re.sub(pattern, '', content)
        
        # Сада додај чист код само једном - пре Reservation Modal JavaScript-а
        if '// Reservation Modal Functionality' in content:
            content = content.replace('// Reservation Modal Functionality', clean_mobile_js + '\n\n        // Reservation Modal Functionality')
            print(f"✓ Очишћен и додат mobile nav JS у {filename}")
        else:
            print(f"⚠ Није пронађена Reservation Modal секција у {filename}")
        
        # Запиши ажуриран садржај
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Mobile navigation JavaScript очишћен на свим blog-post страницама.")
