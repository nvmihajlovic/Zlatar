"""
Check if all pages have consistent calendar icon centering in both desktop and mobile.
"""

import os
import re

def check_icon_centering(file_path):
    """Check if page has proper icon centering CSS."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # Check for modal header icon centering
        modal_header_found = re.search(r'\.modal-header\s*\{[^}]*text-align:\s*center', content)
        modal_icon_found = re.search(r'\.modal-header\s+i\s*\{[^}]*font-size:\s*3rem[^}]*color:\s*#D4AF37', content)
        
        if not modal_header_found:
            issues.append("Missing modal-header centering")
        if not modal_icon_found:
            issues.append("Missing modal-header icon styling")
        
        # Check for mobile btn-reserve centering
        mobile_btn_reserve = re.search(
            r'@media.*768px.*\.btn-reserve\s*\{[^}]*display:\s*flex[^}]*align-items:\s*center[^}]*justify-content:\s*center',
            content,
            re.DOTALL
        )
        
        if not mobile_btn_reserve:
            issues.append("Missing mobile btn-reserve flex centering")
        
        # Check if btn-reserve icon has margin override on mobile
        mobile_icon_margin = re.search(
            r'@media.*768px.*\.btn-reserve\s+i\s*\{[^}]*margin-right:\s*0\s*!important',
            content,
            re.DOTALL
        )
        
        if not mobile_icon_margin:
            issues.append("Missing mobile btn-reserve icon margin reset")
        
        return issues
            
    except Exception as e:
        return [f"Error: {e}"]

def main():
    """Check all HTML files."""
    files_to_check = [
        'index.html',
        'blog.html',
        'blog-post-1.html', 'blog-post-2.html', 'blog-post-3.html',
        'blog-post-4.html', 'blog-post-5.html', 'blog-post-6.html',
        'blog-post-7.html', 'blog-post-8.html', 'blog-post-9.html',
        'blog-post-10.html', 'blog-post-11.html', 'blog-post-12.html',
        'wine.html', 'gallery.html', 'contact.html',
        'menu.html', 'about.html', 'privacy.html', 'terms.html', 'sitemap.html'
    ]
    
    print("🔍 Checking calendar icon centering across all pages...\\n")
    
    all_good = True
    
    for filename in files_to_check:
        if os.path.exists(filename):
            issues = check_icon_centering(filename)
            if issues:
                all_good = False
                print(f"⚠️  {filename}")
                for issue in issues:
                    print(f"   • {issue}")
            else:
                print(f"✅ {filename} - All icon centering looks good")
        else:
            print(f"⏭️  {filename} - File not found")
    
    if all_good:
        print(f"\\n✨ Perfect! All icons are properly centered on desktop and mobile")
    else:
        print(f"\\n⚠️  Some pages need icon centering fixes")

if __name__ == "__main__":
    main()
