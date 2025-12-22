import os
import re

pages = ['about.html', 'contact.html', 'gallery.html', 'menu.html', 'wine.html', 'privacy.html', 'sitemap.html', 'terms.html', 'index.html']

for page in pages:
    if not os.path.exists(page):
        continue
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Dodaj mobile-nav.css ako nema
    if 'mobile-nav.css' not in content:
        content = content.replace(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">',
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n    \n    <!-- Mobile Navigation -->\n    <link rel="stylesheet" href="mobile-nav.css">'
        )
    
    # 2. Dodaj mobile-nav.js ako nema
    if 'mobile-nav.js' not in content:
        content = content.replace('</body>', '\n<!-- Mobile Navigation -->\n<script src="mobile-nav.js"></script>\n</body>')
    
    # 3. Obriši stari mobilni CSS blok (@media (max-width: 1281px) ... do zatvaranja })
    # Traži <style> blok koji sadrži @media (max-width: 1281px) ili 1024px
    style_pattern = r'<style>\s*@media\s*\(max-width:\s*12(81|24)px\).*?</style>'
    content = re.sub(style_pattern, '', content, flags=re.DOTALL)
    
    # 4. Obriši stari mobilni JavaScript (od const navToggle do kraja te funkcije)
    js_pattern = r'(//\s*Mobile.*?Toggle.*?\n.*?)?const navToggle = document\.getElementById.*?}\);.*?\n.*?}\);'
    content = re.sub(js_pattern, '', content, flags=re.DOTALL)
    
    # Dodatno čišćenje - obriši body.menu-open stilove ako postoje
    content = re.sub(r'body\.menu-open\s*\{.*?\}', '', content, flags=re.DOTALL)
    
    if content != original_content:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'{page} - OČIŠĆENO I AŽURIRANO')
    else:
        print(f'{page} - BEZ PROMENA')
