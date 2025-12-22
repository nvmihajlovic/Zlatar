#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-add data-i18n attributes to menu.html based on existing translations in i18n.js
"""

import re
import os
from datetime import datetime

# File paths
MENU_FILE = r"c:\Users\WEB STUDIO LINK\OneDrive\Desktop\Restoran Zlatar Novi\menu.html"
BACKUP_DIR = r"c:\Users\WEB STUDIO LINK\OneDrive\Desktop\Restoran Zlatar Novi\backup_" + datetime.now().strftime("%Y-%m-%d_%H%M%S")

def create_backup():
    """Create backup of menu.html"""
    import shutil
    os.makedirs(BACKUP_DIR, exist_ok=True)
    shutil.copy2(MENU_FILE, os.path.join(BACKUP_DIR, "menu.html"))
    print(f"✓ Backup created: {BACKUP_DIR}")

def add_i18n_attributes(html_content):
    """Add data-i18n attributes to HTML elements"""
    
    # Counter
    changes = 0
    
    # Category buttons that don't have data-i18n yet
    category_mappings = [
        (r'(<button class="category-btn"[^>]*data-category="hot"[^>]*>.*?<i[^>]*></i>)(Топла предјела)(</button>)',
         r'\1<span data-i18n="menu-page.category.hot">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="mixed"[^>]*>.*?<i[^>]*></i>)(Комбинована)(</button>)',
         r'\1<span data-i18n="menu-page.category.mixed">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="soups"[^>]*>.*?<i[^>]*></i>)(Супе и чорбе)(</button>)',
         r'\1<span data-i18n="menu-page.category.soups">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="fish"[^>]*>.*?<i[^>]*></i>)(Риба)(</button>)',
         r'\1<span data-i18n="menu-page.category.fish">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="roast"[^>]*>.*?<i[^>]*></i>)(Печење)(</button>)',
         r'\1<span data-i18n="menu-page.category.roast">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="special"[^>]*>.*?<i[^>]*></i>)(Специјалитети)(</button>)',
         r'\1<span data-i18n="menu-page.category.special">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="grill"[^>]*>.*?<i[^>]*></i>)(Роштиљ)(</button>)',
         r'\1<span data-i18n="menu-page.category.grill">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="carte"[^>]*>.*?<i[^>]*></i>)(По поруџбини)(</button>)',
         r'\1<span data-i18n="menu-page.category.carte">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="vegetables"[^>]*>.*?<i[^>]*></i>)(Варива)(</button>)',
         r'\1<span data-i18n="menu-page.category.vegetables">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="salads"[^>]*>.*?<i[^>]*></i>)(Салате)(</button>)',
         r'\1<span data-i18n="menu-page.category.salads">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="desserts"[^>]*>.*?<i[^>]*></i>)(Посластице)(</button>)',
         r'\1<span data-i18n="menu-page.category.desserts">\2</span>\3'),
        (r'(<button class="category-btn"[^>]*data-category="rakije"[^>]*>.*?<i[^>]*></i>)(Ракије Златар)(</button>)',
         r'\1<span data-i18n="menu-page.category.rakije">\2</span>\3'),
    ]
    
    for pattern, replacement in category_mappings:
        if re.search(pattern, html_content, re.DOTALL):
            html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
            changes += 1
    
    print(f"✓ Added {changes} data-i18n attributes to category buttons")
    return html_content

def main():
    print("Starting i18n attribute addition...")
    
    # Create backup
    create_backup()
    
    # Read HTML
    with open(MENU_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add i18n attributes
    content = add_i18n_attributes(content)
    
    # Write back
    with open(MENU_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ menu.html updated successfully!")
    print("\nDone! Language switching should now work on menu.html")

if __name__ == "__main__":
    main()
