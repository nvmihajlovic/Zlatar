#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to:
1. Replace index.html modal with modal from other pages
2. Add cookie consent to all pages
3. Remove page-badge from all pages
4. Add breadcrumbs to gallery and contact pages
"""

import re

# Extract modal from about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

# Extract the modal HTML and CSS from about.html
modal_match = re.search(r'(<!-- Reservation Modal -->.*?</div>\s*</div>\s*\n\s*<style>.*?</style>)', about_content, re.DOTALL)
if modal_match:
    modal_code = modal_match.group(1)
    print("✓ Modal extracted from about.html")
else:
    print("✗ Failed to extract modal")
    exit(1)

# Extract cookie consent from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract cookie consent HTML and all related styles
cookie_match = re.search(r'(<!-- Cookie Consent Banner -->.*?</div>\s*\n\s*<style>.*?</style>)', index_content, re.DOTALL)
if cookie_match:
    cookie_code = cookie_match.group(1)
    print("✓ Cookie consent extracted from index.html")
else:
    print("✗ Failed to extract cookie consent")
    exit(1)

# Update index.html - replace old modal with new modal
index_old_modal = re.search(r'<!-- Reservation Modal -->.*?</div>\s*</div>\s*\n\s*<style>.*?</style>', index_content, re.DOTALL)
if index_old_modal:
    index_content = index_content.replace(index_old_modal.group(0), modal_code)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("✓ index.html - Modal replaced")
else:
    print("✗ index.html - Modal pattern not found")

# List of all pages to update (except index)
pages = ['about.html', 'menu.html', 'wine.html', 'gallery.html', 'contact.html', 'terms.html', 'privacy.html', 'sitemap.html']

# Add cookie consent to all pages
for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if cookie consent already exists
        if 'Cookie Consent Banner' in content:
            print(f"⚠ {page} - Cookie consent already exists")
            continue
        
        # Find the Back to Top button and insert cookie consent after it
        back_to_top = re.search(r'(<!-- Back to Top Button -->.*?</button>)', content, re.DOTALL)
        if back_to_top:
            insert_pos = content.find(back_to_top.group(0)) + len(back_to_top.group(0))
            content = content[:insert_pos] + '\n\n    ' + cookie_code + content[insert_pos:]
            
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {page} - Cookie consent added")
        else:
            print(f"⚠ {page} - Back to Top button not found")
    except Exception as e:
        print(f"✗ {page} - Error: {e}")

# Remove page-badge from all pages
all_pages = ['about.html', 'menu.html', 'wine.html', 'gallery.html', 'contact.html', 'terms.html', 'privacy.html', 'sitemap.html']

for page in all_pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove page-badge HTML
        content = re.sub(r'\s*<div class="page-badge">.*?</div>', '', content, flags=re.DOTALL)
        
        # Remove page-badge CSS
        content = re.sub(r'\s*\.page-badge\s*\{[^}]+\}', '', content)
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {page} - Page badge removed")
    except Exception as e:
        print(f"✗ {page} - Error: {e}")

# Add breadcrumbs to gallery and contact pages
breadcrumbs_gallery = '''            <nav class="breadcrumbs" style="margin-bottom: 1.5rem;">
                <a href="index.html" style="color: rgba(255, 255, 255, 0.7); text-decoration: none; font-family: 'Montserrat', sans-serif; font-size: 0.9rem; transition: color 0.3s;">
                    <i class="fas fa-home" style="margin-right: 0.5rem;"></i>Почетна
                </a>
                <span style="color: rgba(255, 255, 255, 0.4); margin: 0 0.75rem;">/</span>
                <span style="color: #D4AF37; font-family: 'Montserrat', sans-serif; font-size: 0.9rem;">Галерија</span>
            </nav>'''

breadcrumbs_contact = '''            <nav class="breadcrumbs" style="margin-bottom: 1.5rem;">
                <a href="index.html" style="color: rgba(255, 255, 255, 0.7); text-decoration: none; font-family: 'Montserrat', sans-serif; font-size: 0.9rem; transition: color 0.3s;">
                    <i class="fas fa-home" style="margin-right: 0.5rem;"></i>Почетна
                </a>
                <span style="color: rgba(255, 255, 255, 0.4); margin: 0 0.75rem;">/</span>
                <span style="color: #D4AF37; font-family: 'Montserrat', sans-serif; font-size: 0.9rem;">Контакт</span>
            </nav>'''

breadcrumbs_css = '''
        .breadcrumbs a:hover {
            color: #D4AF37;
        }'''

# Add breadcrumbs to gallery.html
try:
    with open('gallery.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the h1 with page-title and insert breadcrumbs before it
    title_match = re.search(r'(\s*)<h1 class="page-title">', content)
    if title_match:
        insert_pos = content.find(title_match.group(0))
        content = content[:insert_pos] + breadcrumbs_gallery + '\n' + content[insert_pos:]
        
        # Add breadcrumbs CSS
        style_end = content.rfind('</style>')
        if style_end != -1:
            content = content[:style_end] + breadcrumbs_css + '\n    ' + content[style_end:]
        
        with open('gallery.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ gallery.html - Breadcrumbs added")
    else:
        print("⚠ gallery.html - Page title not found")
except Exception as e:
    print(f"✗ gallery.html - Error: {e}")

# Add breadcrumbs to contact.html
try:
    with open('contact.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the h1 with page-title and insert breadcrumbs before it
    title_match = re.search(r'(\s*)<h1 class="page-title">', content)
    if title_match:
        insert_pos = content.find(title_match.group(0))
        content = content[:insert_pos] + breadcrumbs_contact + '\n' + content[insert_pos:]
        
        # Add breadcrumbs CSS
        style_end = content.rfind('</style>')
        if style_end != -1:
            content = content[:style_end] + breadcrumbs_css + '\n    ' + content[style_end:]
        
        with open('contact.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ contact.html - Breadcrumbs added")
    else:
        print("⚠ contact.html - Page title not found")
except Exception as e:
    print(f"✗ contact.html - Error: {e}")

print("\n✓✓✓ All updates completed!")
