#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Add Back to Top button to all pages that don't have it
"""

import re
import os

# HTML for Back to Top button
BACK_TO_TOP_HTML = '''    <!-- Back to Top Button -->
    <button class="back-to-top" id="backToTop">
        <i class="fas fa-arrow-up"></i>
    </button>

'''

# CSS for Back to Top button
BACK_TO_TOP_CSS = '''    <style>
        /* Back to Top Button */
        .back-to-top {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 50px;
            height: 50px;
            display: none;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
            border: none;
            border-radius: 50%;
            color: #fff;
            font-size: 1.25rem;
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(212, 175, 55, 0.4);
            transition: all 0.3s;
            z-index: 9999;
        }

        .back-to-top.visible {
            display: flex;
        }

        .back-to-top:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 32px rgba(212, 175, 55, 0.5);
        }
    </style>

'''

# JavaScript for Back to Top button
BACK_TO_TOP_JS = '''    <script>
        // Back to Top Button Functionality
        (function() {
            const backToTopButton = document.getElementById('backToTop');
            
            if (backToTopButton) {
                // Show/hide button on scroll
                window.addEventListener('scroll', function() {
                    if (window.scrollY > 300) {
                        backToTopButton.classList.add('visible');
                    } else {
                        backToTopButton.classList.remove('visible');
                    }
                });
                
                // Scroll to top on click
                backToTopButton.addEventListener('click', function() {
                    window.scrollTo({
                        top: 0,
                        behavior: 'smooth'
                    });
                });
            }
        })();
    </script>

'''

# Pages to add back to top button
PAGES = [
    'about.html',
    'menu.html',
    'wine.html',
    'gallery.html',
    'contact.html',
    'terms.html',
    'privacy.html',
    'sitemap.html'
]

def add_back_to_top_to_page(file_path):
    """Add back to top button HTML, CSS and JavaScript to a page"""
    
    if not os.path.exists(file_path):
        print(f"✗ File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has back to top
    if 'back-to-top' in content or 'backToTop' in content:
        print(f"✓ {file_path} already has back-to-top button")
        return False
    
    # Find where to insert the button HTML (before closing body tag or cookie consent)
    # Look for common patterns before </body>
    insertion_patterns = [
        (r'(<!-- Cookie Consent Banner -->)', BACK_TO_TOP_HTML + r'\1'),
        (r'(<div class="cookie-consent")', BACK_TO_TOP_HTML + r'\1'),
        (r'(</body>)', BACK_TO_TOP_HTML + r'\1'),
    ]
    
    html_inserted = False
    for pattern, replacement in insertion_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            html_inserted = True
            print(f"  ✓ Inserted button HTML")
            break
    
    if not html_inserted:
        print(f"✗ Could not find insertion point for HTML in {file_path}")
        return False
    
    # Find where to insert CSS (before closing </head> or in last <style> section)
    # Look for last </style> tag before </head>
    css_patterns = [
        (r'(</head>)', BACK_TO_TOP_CSS + r'\1'),
    ]
    
    css_inserted = False
    for pattern, replacement in css_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            css_inserted = True
            print(f"  ✓ Inserted CSS")
            break
    
    if not css_inserted:
        print(f"✗ Could not find insertion point for CSS in {file_path}")
        return False
    
    # Find where to insert JavaScript (before closing </body> tag)
    js_patterns = [
        (r'(</body>)', BACK_TO_TOP_JS + r'\1'),
    ]
    
    js_inserted = False
    for pattern, replacement in js_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content, count=1)
            js_inserted = True
            print(f"  ✓ Inserted JavaScript")
            break
    
    if not js_inserted:
        print(f"✗ Could not find insertion point for JavaScript in {file_path}")
        return False
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    print("=" * 70)
    print("ADDING BACK TO TOP BUTTON TO ALL PAGES")
    print("=" * 70)
    
    success_count = 0
    skip_count = 0
    fail_count = 0
    
    for page in PAGES:
        print(f"\n📄 Processing {page}...")
        result = add_back_to_top_to_page(page)
        
        if result:
            success_count += 1
        elif os.path.exists(page) and ('back-to-top' in open(page, 'r', encoding='utf-8').read()):
            skip_count += 1
        else:
            fail_count += 1
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"✓ Successfully added: {success_count}")
    print(f"⊘ Already had button: {skip_count}")
    print(f"✗ Failed: {fail_count}")
    print(f"📊 Total processed: {len(PAGES)}")
    
    if success_count > 0:
        print("\n✨ Back to Top button successfully added to all missing pages!")
        print("\nThe button includes:")
        print("  • HTML button element with Font Awesome icon")
        print("  • CSS with golden gradient, smooth transitions, and hover effects")
        print("  • JavaScript for show/hide on scroll and smooth scroll to top")

if __name__ == '__main__':
    main()
