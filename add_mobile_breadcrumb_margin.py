"""
Add margin-bottom to mobile breadcrumbs in blog-post pages.
"""

import os
import re

def add_mobile_breadcrumb_margin(file_path):
    """Add margin-bottom to mobile breadcrumbs."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Find mobile breadcrumbs block in blog posts and add margin-bottom if missing
        pattern = r'(\.breadcrumbs \{\s*)(padding: 0\.75rem 1rem !important;)'
        
        def add_margin(match):
            opening = match.group(1)
            padding = match.group(2)
            return f"{opening}margin-bottom: 1.5rem;\n                {padding}"
        
        # Check if margin-bottom already exists
        mobile_media_section = re.search(r'@media \(max-width: 768px\).*?\.breadcrumbs \{[^}]*\}', content, re.DOTALL)
        if mobile_media_section:
            breadcrumb_block = mobile_media_section.group()
            if 'margin-bottom:' not in breadcrumb_block and 'padding: 0.75rem 1rem !important;' in breadcrumb_block:
                content = re.sub(pattern, add_margin, content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
        
        return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Process all blog-post HTML files."""
    files_to_process = [
        'blog-post-1.html', 'blog-post-2.html', 'blog-post-3.html',
        'blog-post-4.html', 'blog-post-5.html', 'blog-post-6.html',
        'blog-post-7.html', 'blog-post-8.html', 'blog-post-9.html',
        'blog-post-10.html', 'blog-post-11.html', 'blog-post-12.html'
    ]
    
    print("🔧 Adding margin-bottom to mobile breadcrumbs in blog posts...\n")
    
    modified_count = 0
    
    for filename in files_to_process:
        if os.path.exists(filename):
            if add_mobile_breadcrumb_margin(filename):
                modified_count += 1
                print(f"✅ {filename} - Added margin-bottom: 1.5rem")
            else:
                print(f"⏭️  {filename} - Already has margin-bottom or no change needed")
        else:
            print(f"⚠️  {filename} - File not found")
    
    print(f"\n✨ Complete! Modified {modified_count} blog-post files")

if __name__ == "__main__":
    main()
