import os
import re

pages = ['about.html', 'contact.html', 'gallery.html', 'menu.html', 'wine.html', 'privacy.html', 'sitemap.html', 'terms.html']

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Pronađi i obriši kompletne <style> blokove koji sadrže @media
    in_style = False
    in_media = False
    style_start = None
    new_lines = []
    
    for i, line in enumerate(lines):
        if '<style>' in line and i > 100:  # Ignorši početne style tagove
            in_style = True
            style_start = i
            continue
        
        if in_style:
            if '@media' in line:
                in_media = True
            if '</style>' in line:
                if in_media:
                    # Preskoči ceo blok
                    in_style = False
                    in_media = False
                    style_start = None
                    continue
                else:
                    in_style = False
                    new_lines.append(line)
            continue
        
        new_lines.append(line)
    
    with open(page, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f'{page} - Obrisano {len(lines) - len(new_lines)} linija')
