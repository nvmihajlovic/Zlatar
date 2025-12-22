#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add cookie consent to wine.html, gallery.html, and contact.html
"""

import re

# Read index.html to extract cookie consent
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract cookie consent HTML and CSS
cookie_match = re.search(r'(<!-- Cookie Consent Banner -->.*?</div>\s*\n\s*<style>.*?@media \(max-width: 768px\).*?\}\s*</style>)', index_content, re.DOTALL)
if cookie_match:
    cookie_code = cookie_match.group(1)
    print("✓ Cookie consent extracted from index.html")
else:
    print("✗ Failed to extract cookie consent")
    exit(1)

pages = ['wine.html', 'gallery.html', 'contact.html']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find where to insert cookie consent (before <!-- Modal JavaScript -->)
        modal_js_pos = content.find('    <!-- Modal JavaScript -->')
        if modal_js_pos != -1:
            # Insert cookie consent before Modal JavaScript
            content = content[:modal_js_pos] + '\n    ' + cookie_code + '\n\n' + content[modal_js_pos:]
            
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {page} - Cookie consent added")
        else:
            print(f"⚠ {page} - Modal JavaScript comment not found")
    except Exception as e:
        print(f"✗ {page} - Error: {e}")

print("\n✓✓✓ Cookie consent added to all remaining pages!")
