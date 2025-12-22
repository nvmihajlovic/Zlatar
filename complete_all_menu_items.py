#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add data-i18n to ALL remaining menu items and side dishes
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

def add_all_missing_items(content):
    """Add data-i18n to ALL menu items that don't have it"""
    
    changes = 0
    
    # Find all item-name divs without data-i18n in their span
    pattern = r'(<div class="item-name">)(?!<span data-i18n)(.*?)(</div>)'
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for match in list(matches):
        full_match = match.group(0)
        prefix = match.group(1)
        text = match.group(2).strip()
        suffix = match.group(3)
        
        # Skip if already has span with data-i18n
        if 'data-i18n=' in text:
            continue
            
        # Clean text - remove existing <span> tags if any
        clean_text = re.sub(r'<span[^>]*>', '', text)
        clean_text = re.sub(r'</span>', '', clean_text)
        clean_text = clean_text.strip()
        
        # Generate i18n key from text (simplified version)
        # This will need manual checking
        i18n_key = 'menu-page.item.' + clean_text.lower().replace(' ', '-').replace('„', '').replace('"', '').replace('(', '').replace(')', '').replace('/', '-').replace(',', '')
        
        # Wrap in span with data-i18n
        new_content = f'{prefix}<span data-i18n="{i18n_key}">{clean_text}</span>{suffix}'
        content = content.replace(full_match, new_content, 1)
        changes += 1
    
    # Now do same for item-description
    pattern_desc = r'(<div class="item-description">)(?!<span data-i18n)(.*?)(</div>)'
    matches_desc = re.finditer(pattern_desc, content, re.DOTALL)
    
    for match in list(matches_desc):
        full_match = match.group(0)
        prefix = match.group(1)
        text = match.group(2).strip()
        suffix = match.group(3)
        
        # Skip empty descriptions
        if not text or 'data-i18n=' in text:
            continue
            
        # Clean text
        clean_text = re.sub(r'<span[^>]*>', '', text)
        clean_text = re.sub(r'</span>', '', clean_text)
        clean_text = clean_text.strip()
        
        if not clean_text:
            continue
        
        # Generate i18n key
        i18n_key = 'menu-page.item.XXX-desc'  # Will need manual mapping
        
        # Wrap in span
        new_content = f'{prefix}<span data-i18n="{i18n_key}">{clean_text}</span>{suffix}'
        content = content.replace(full_match, new_content, 1)
        changes += 1
    
    print(f"✓ Added {changes} data-i18n attributes")
    return content

def add_side_dishes(content):
    """Add data-i18n to side dishes"""
    
    side_dishes = [
        ('Прилог: печени кромпир или помфрит, лук', 'menu-page.side-dish.grill'),
        ('Прилог: печени кромпир, вариво', 'menu-page.side-dish.carte'),
        ('Прилог: кромпир и блитва', 'menu-page.side-dish.fish'),
        ('Прилог: кромпир/кајмак', 'menu-page.side-dish.roast'),
    ]
    
    changes = 0
    for text, key in side_dishes:
        # Check if already has data-i18n
        if f'data-i18n="{key}"' not in content:
            # Find and replace
            old = f'<p class="side-dish">{text}</p>'
            new = f'<p class="side-dish" data-i18n="{key}">{text}</p>'
            if old in content:
                content = content.replace(old, new)
                changes += 1
                print(f"  ✓ Added: {key}")
    
    return content, changes

def main():
    print("=== Adding ALL Missing Menu Items ===\n")
    
    create_backup()
    
    with open(MENU_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add side dishes first
    content, side_changes = add_side_dishes(content)
    
    # This approach is too simplistic - we need exact mapping
    # Let me read i18n.js to see what keys exist
    print("\n⚠️  NAPOMENA: Ova skripta je osnovna.")
    print("Trebam da kreiram tačno mapiranje svih jela na njihove i18n ključeve.")
    print("Molim te podigni ovu skriptu ili daj spisak jela koja fale.\n")
    
    with open(MENU_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Dodato {side_changes} priloga")

if __name__ == "__main__":
    main()
