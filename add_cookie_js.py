#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add cookie consent JavaScript to all pages that have cookie consent HTML
"""

import re

# Read index.html to extract cookie consent JS
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract cookie consent JavaScript
cookie_js_match = re.search(r'(<script>\s*// Cookie Consent Logic.*?function initializeScripts\(prefs\) \{.*?\}\s*\}\s*\}\);.*?</script>)', index_content, re.DOTALL)
if cookie_js_match:
    cookie_js = cookie_js_match.group(1)
    print("✓ Cookie consent JavaScript extracted from index.html")
else:
    print("✗ Failed to extract cookie consent JavaScript")
    exit(1)

pages = ['about.html', 'menu.html', 'wine.html', 'gallery.html', 'contact.html', 'terms.html', 'privacy.html', 'sitemap.html']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if cookie consent JavaScript already exists
        if 'Cookie Consent Logic' in content:
            print(f"⚠ {page} - Cookie consent JavaScript already exists")
            continue
        
        # Check if cookie consent HTML exists
        if 'Cookie Consent Banner' not in content:
            print(f"⚠ {page} - Cookie consent HTML not found, skipping")
            continue
        
        # Find the Modal JavaScript section and insert before it
        modal_js_pos = content.find('    <!-- Modal JavaScript -->')
        if modal_js_pos != -1:
            # Insert cookie JS before Modal JavaScript
            content = content[:modal_js_pos] + '\n    ' + cookie_js + '\n\n' + content[modal_js_pos:]
            
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {page} - Cookie consent JavaScript added")
        else:
            print(f"⚠ {page} - Modal JavaScript comment not found")
    except Exception as e:
        print(f"✗ {page} - Error: {e}")

print("\n✓✓✓ Cookie consent JavaScript added to all pages!")
