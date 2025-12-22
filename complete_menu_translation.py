#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete menu.html translation - add ALL missing data-i18n attributes
"""

import re
from datetime import datetime
import shutil
import os

MENU_FILE = r"c:\Users\WEB STUDIO LINK\OneDrive\Desktop\Restoran Zlatar Novi\menu.html"

def create_backup():
    backup_dir = r"c:\Users\WEB STUDIO LINK\OneDrive\Desktop\Restoran Zlatar Novi\backup_" + datetime.now().strftime("%Y-%m-%d_%H%M%S")
    os.makedirs(backup_dir, exist_ok=True)
    shutil.copy2(MENU_FILE, os.path.join(backup_dir, "menu.html"))
    print(f"✓ Backup: {backup_dir}")
    return backup_dir

def add_missing_i18n(content):
    """Add data-i18n to all remaining text elements"""
    changes = 0
    
    # Category section titles that don't have data-i18n
    category_titles = [
        # Format: (search_pattern, i18n_key)
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Хладна предјела)(</h2>)', 'menu-page.category.cold-appetizers'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Топла предјела)(</h2>)', 'menu-page.category.hot-appetizers'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Комбинована предјела)(</h2>)', 'menu-page.category.mixed-appetizers'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Супе и чорбе)(</h2>)', 'menu-page.category.soups'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Риба)(</h2>)', 'menu-page.category.fish'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Печење)(</h2>)', 'menu-page.category.roast'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Специјалитети „Златар")(</h2>)', 'menu-page.category.specialties'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Јела са роштиља на ћумур)(</h2>)', 'menu-page.category.grill'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Јела по поруџбини)(</h2>)', 'menu-page.category.a-la-carte'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Варива и кувана јела)(</h2>)', 'menu-page.category.vegetables'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Салате)(</h2>)', 'menu-page.category.salads'),
        (r'(<h2 class="category-title"[^>]*>.*?<i[^>]*></i>)(Посластице)(</h2>)', 'menu-page.category.desserts'),
    ]
    
    for pattern, i18n_key in category_titles:
        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            # Add data-i18n if not already present
            new_pattern = pattern.replace(r')(', rf')(<span data-i18n="{i18n_key}">')
            new_pattern = new_pattern.replace(r')(</h2>)', r'</span>\3')
            
            # Check if already has data-i18n
            if f'data-i18n="{i18n_key}"' not in content:
                replacement = r'\1<span data-i18n="' + i18n_key + r'">\2</span>\3'
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                changes += 1
                print(f"  ✓ Added: {i18n_key}")
    
    # Side dishes (prilozi)
    side_dishes = [
        (r'(Прилог: печени кромпир или помфрит, лук)', 'menu-page.side-dish.grill'),
        (r'(Прилог: печени кромпир, вариво)', 'menu-page.side-dish.carte'),
        (r'(Прилог: кромпир и блитва)', 'menu-page.side-dish.fish'),
        (r'(Прилог: кромпир/кајмак)', 'menu-page.side-dish.roast'),
    ]
    
    for text, i18n_key in side_dishes:
        if text in content and f'data-i18n="{i18n_key}"' not in content:
            # Wrap in span with data-i18n
            content = content.replace(
                f'<p class="side-dish">{text}</p>',
                f'<p class="side-dish" data-i18n="{i18n_key}">{text}</p>'
            )
            changes += 1
            print(f"  ✓ Added: {i18n_key}")
    
    print(f"\n✓ Total changes: {changes}")
    return content

def main():
    print("=== Complete Menu Translation ===\n")
    
    # Backup
    create_backup()
    
    # Read file
    with open(MENU_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add missing i18n
    content = add_missing_i18n(content)
    
    # Write back
    with open(MENU_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n✓ menu.html updated!")
    print("\nNAPOMENA: Većina prevoda već postoji u i18n.js")
    print("Samo su dodati data-i18n atributi na HTML elemente.")

if __name__ == "__main__":
    main()
