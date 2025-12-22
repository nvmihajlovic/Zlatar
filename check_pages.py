import os
import re

pages = ['about.html', 'contact.html', 'gallery.html', 'menu.html', 'wine.html', 'privacy.html', 'sitemap.html', 'terms.html', 'index.html']

for page in pages:
    if not os.path.exists(page):
        print(f'{page} - NE POSTOJI')
        continue
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_css = 'mobile-nav.css' in content
    has_js = 'mobile-nav.js' in content
    has_old_css = '@media (max-width: 1281px)' in content or '@media (max-width: 1024px)' in content
    has_old_js = 'const navToggle = document.getElementById' in content
    
    print(f'{page:15} CSS:{has_css} JS:{has_js} StariCSS:{has_old_css} StariJS:{has_old_js}')
