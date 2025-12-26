import codecs
import re

# Тачан navbar HTML са index.html (без language switcher)
navbar_html = '''    <!-- Navigation -->
    <nav class="navbar" id="navbar" style="display: flex; align-items: center; background: linear-gradient(180deg, rgba(20,15,8,0.97) 0%, rgba(35,26,15,0.95) 50%, rgba(25,18,10,0.93) 100%); backdrop-filter: blur(30px) saturate(180%); border-bottom: 1px solid transparent; border-image: linear-gradient(90deg, transparent 0%, rgba(212,175,55,0.4) 30%, rgba(255,215,0,0.3) 50%, rgba(212,175,55,0.4) 70%, transparent 100%) 1; box-shadow: 0 8px 32px rgba(0,0,0,0.4), 0 4px 16px rgba(212,175,55,0.08), inset 0 1px 0 rgba(255,255,255,0.06), inset 0 -1px 0 rgba(212,175,55,0.1); position: fixed; top: 0; left: 0; right: 0; z-index: 1000; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); justify-content: center;">
        <div class="nav-container" style="display: flex; align-items: center; justify-content: space-between; max-width: 1400px; width: 100%; padding: 0.5rem 1.5rem;">
            <a href="index.html" class="nav-logo" style="display: flex; align-items: center; transition: transform 0.3s; margin-right: auto; padding-right: 3rem;">
                <img src="images/znak-restoran-zlatar-vektorski_clipped_rev_1.png" alt="Ресторан Златар" class="logo-img" style="height: 68px; width: auto; filter: drop-shadow(0 2px 8px rgba(212,175,55,0.3));">
            </a>
            
            <ul class="nav-menu" id="navMenu" style="display: flex; align-items: center; gap: 1.4rem;">
                <li class="nav-item"><a href="index.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Почетна</span></a></li>
                <li class="nav-item"><a href="about.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>О нама</span></a></li>
                <li class="nav-item"><a href="menu.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Јеловник</span></a></li>
                <li class="nav-item"><a href="wine.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Винска карта</span></a></li>
                <li class="nav-item"><a href="blog.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Блог</span></a></li>
                <li class="nav-item"><a href="gallery.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Галерија</span></a></li>
                <li class="nav-item"><a href="contact.html" class="nav-link" style="color: rgba(255,255,255,0.9); font-weight: 500; font-size: 0.9rem; letter-spacing: 0.3px; background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 0.7rem 1.3rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);"><span>Контакт</span></a></li>
            </ul>
            
            <div class="nav-actions" style="display: flex; align-items: center; gap: 1.5rem; margin-left: auto; padding-left: 3rem;">
                <button class="btn-reserve" id="btnReserve" style="background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); color: #fff; font-weight: 600; font-size: 0.9rem; padding: 0.75rem 1.8rem; border: none; border-radius: 50px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 6px 20px rgba(212,175,55,0.4), inset 0 1px 0 rgba(255,255,255,0.3); letter-spacing: 0.5px;">
                    <i class="fas fa-calendar-check" style="margin-right: 0.5rem;"></i>
                    <span>Резервација</span>
                </button>
                <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" style="margin-left: 0.5rem;">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </nav>'''

# Процесуј све blog-post странице
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Замени navbar - тражи од <!-- Navigation --> или <nav до </nav>
        pattern = r'(<!-- Navigation -->[\s\S]*?<nav[\s\S]*?</nav>|<nav class="navbar"[\s\S]*?</nav>)'
        
        if re.search(pattern, content):
            content = re.sub(pattern, navbar_html, content, count=1)
            print(f"✓ Замењен navbar у {filename}")
            
            # Запиши ажуриран садржај
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {filename} ажуриран\n")
        else:
            print(f"⚠ Navbar није пронађен у {filename}\n")
            
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\n🎉 ЗАВРШЕНО! Navbar са index.html прекопиран на све blog-post странице!")
