import re
import codecs

print("🔧 Уклањам СВЕ inline стилове из navbar-а и правим CSS...\n")

# CSS for navbar (desktop)
navbar_css = """
/* ===== NAVBAR CSS ===== */
.navbar {
    display: flex;
    align-items: center;
    background: linear-gradient(180deg, rgba(20,15,8,0.97) 0%, rgba(35,26,15,0.95) 50%, rgba(25,18,10,0.93) 100%);
    backdrop-filter: blur(30px) saturate(180%);
    border-bottom: 1px solid transparent;
    border-image: linear-gradient(90deg, transparent 0%, rgba(212,175,55,0.4) 30%, rgba(255,215,0,0.3) 50%, rgba(212,175,55,0.4) 70%, transparent 100%) 1;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4), 0 4px 16px rgba(212,175,55,0.08), inset 0 1px 0 rgba(255,255,255,0.06), inset 0 -1px 0 rgba(212,175,55,0.1);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    justify-content: center;
}

.nav-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1400px;
    width: 100%;
    padding: 0.5rem 1.5rem;
}

.nav-logo {
    display: flex;
    align-items: center;
    transition: transform 0.3s;
    margin-right: auto;
    padding-right: 3rem;
}

.logo-img {
    height: 68px;
    width: auto;
    filter: drop-shadow(0 2px 8px rgba(212,175,55,0.3));
}

.nav-menu {
    display: flex;
    align-items: center;
    gap: 1.4rem;
}

.nav-link {
    color: rgba(255,255,255,0.9);
    font-weight: 500;
    font-size: 0.9rem;
    letter-spacing: 0.3px;
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 0.7rem 1.3rem;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    text-decoration: none;
}

.nav-actions {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-left: auto;
    padding-left: 3rem;
}

.btn-reserve {
    background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
    color: #fff;
    font-weight: 600;
    font-size: 0.9rem;
    padding: 0.75rem 1.8rem;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 6px 20px rgba(212,175,55,0.4), inset 0 1px 0 rgba(255,255,255,0.3);
    letter-spacing: 0.5px;
}

.btn-reserve i {
    margin-right: 0.5rem;
}

.nav-toggle {
    display: none;
    margin-left: 0.5rem;
}

.nav-toggle span {
    display: block;
}
"""

files = ['blog.html'] + [f'blog-post-{i}.html' for i in range(1, 13)]

for filename in files:
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove ALL inline styles from navbar elements
        content = re.sub(r'(<nav class="navbar"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<div class="nav-container"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<a[^>]*class="nav-logo"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<img[^>]*class="logo-img"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<ul class="nav-menu"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<a[^>]*class="nav-link"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<div class="nav-actions"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<button class="btn-reserve"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<button class="nav-toggle"[^>]*) style="[^"]*"', r'\1', content)
        content = re.sub(r'(<i class="fas fa-calendar-check"[^>]*) style="[^"]*"', r'\1', content)
        
        # Add navbar CSS before </style> if not already there
        if '/* ===== NAVBAR CSS =====' not in content:
            content = content.replace('</style>', navbar_css + '\n</style>')
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Очишћен {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО!")
print("\nСви inline стилови уклоњени из navbar-а.")
print("CSS сада контролише изглед комплетно.")
print("mobile-nav.css ради за mobile (<1024px).")
