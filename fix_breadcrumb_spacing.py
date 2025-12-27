"""
Fix inconsistent breadcrumb spacing across all pages.
Standardizes hero section padding and breadcrumb margins for both desktop and mobile.
"""

import os
import re

def fix_breadcrumb_spacing(file_path):
    """Fix breadcrumb and hero spacing in HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # 1. Standardize desktop breadcrumbs margin-bottom to 2rem for consistency
        # Find .breadcrumbs { ... margin-bottom: X; ... }
        breadcrumb_desktop_pattern = r'(\.breadcrumbs\s*\{[^}]*?margin-bottom:\s*)[\d.]+rem'
        if re.search(breadcrumb_desktop_pattern, content):
            content = re.sub(breadcrumb_desktop_pattern, r'\g<1>2rem', content)
            changes_made.append("Desktop breadcrumbs margin-bottom → 2rem")
        
        # 2. Add or update mobile breadcrumbs margin-bottom in @media (max-width: 768px)
        # Find mobile breadcrumbs section and ensure margin-bottom is set
        mobile_breadcrumb_pattern = r'(@media\s*\(max-width:\s*768px\)\s*\{[^}]*?)(\.breadcrumbs\s*\{[^}]*?\})'
        
        def update_mobile_breadcrumbs(match):
            media_start = match.group(1)
            breadcrumb_block = match.group(2)
            
            # Check if margin-bottom exists in the block
            if 'margin-bottom:' in breadcrumb_block:
                # Update existing margin-bottom
                breadcrumb_block = re.sub(r'margin-bottom:\s*[\d.]+rem', 'margin-bottom: 1.5rem', breadcrumb_block)
            else:
                # Add margin-bottom after the opening brace
                breadcrumb_block = re.sub(
                    r'(\.breadcrumbs\s*\{)',
                    r'\1\n                margin-bottom: 1.5rem;',
                    breadcrumb_block
                )
            changes_made.append("Mobile breadcrumbs margin-bottom → 1.5rem")
            return media_start + breadcrumb_block
        
        if re.search(mobile_breadcrumb_pattern, content, re.DOTALL):
            content = re.sub(mobile_breadcrumb_pattern, update_mobile_breadcrumbs, content, flags=re.DOTALL)
        
        # 3. Standardize hero section mobile padding to 7rem top for consistent navbar spacing
        # Blog post pages
        hero_blog_mobile_pattern = r'(\.hero-blog\s*\{[^}]*?padding:\s*)[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem'
        if re.search(hero_blog_mobile_pattern, content):
            # Check if we're in a mobile media query context
            mobile_hero_pattern = r'(@media\s*\(max-width:\s*768px\)[^@]*?\.hero-blog\s*\{[^}]*?padding:\s*)[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem'
            if re.search(mobile_hero_pattern, content, re.DOTALL):
                content = re.sub(mobile_hero_pattern, r'\g<1>7rem 1rem 3rem 1rem', content, flags=re.DOTALL)
                changes_made.append("Mobile .hero-blog padding → 7rem 1rem 3rem 1rem")
        
        # Wine, Gallery, Contact pages
        hero_variants = ['hero-wine', 'hero-gallery', 'hero-contact']
        for hero_class in hero_variants:
            pattern = r'(@media\s*\(max-width:\s*768px\)[^@]*?\.' + hero_class + r'\s*\{[^}]*?padding:\s*)[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem'
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, r'\g<1>7rem 1rem 3rem 1rem', content, flags=re.DOTALL)
                changes_made.append(f"Mobile .{hero_class} padding → 7rem 1rem 3rem 1rem")
        
        # 4. Ensure desktop hero padding is consistent
        desktop_hero_pattern = r'(\.hero(?:-blog|-wine|-gallery|-contact)?\s*\{[^}]*?padding:\s*)[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem'
        # Only update if not inside a media query
        lines = content.split('\n')
        in_media_query = False
        media_depth = 0
        
        for i, line in enumerate(lines):
            if '@media' in line:
                in_media_query = True
                media_depth = 0
            
            if in_media_query:
                media_depth += line.count('{') - line.count('}')
                if media_depth <= 0:
                    in_media_query = False
            
            # Only change desktop hero padding if not in media query
            if not in_media_query and re.search(r'\.hero(?:-blog|-wine|-gallery|-contact)?\s*\{', line):
                # Look ahead to find the padding line
                for j in range(i, min(i + 15, len(lines))):
                    if 'padding:' in lines[j] and 'rem' in lines[j]:
                        if re.search(r'padding:\s*[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem', lines[j]):
                            lines[j] = re.sub(
                                r'padding:\s*[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem\s+[\d.]+rem',
                                'padding: 8rem 2rem 4rem 2rem',
                                lines[j]
                            )
                            changes_made.append(f"Desktop hero padding → 8rem 2rem 4rem 2rem (line {j+1})")
                            break
        
        content = '\n'.join(lines)
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        else:
            return False, []
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []

def main():
    """Process all HTML files."""
    # Files to process
    files_to_process = [
        'blog.html',
        'blog-post-1.html', 'blog-post-2.html', 'blog-post-3.html',
        'blog-post-4.html', 'blog-post-5.html', 'blog-post-6.html',
        'blog-post-7.html', 'blog-post-8.html', 'blog-post-9.html',
        'blog-post-10.html', 'blog-post-11.html', 'blog-post-12.html',
        'wine.html', 'gallery.html', 'contact.html',
        'menu.html', 'about.html'
    ]
    
    print("🔧 Fixing breadcrumb and hero spacing consistency...\n")
    
    total_files = 0
    total_changes = 0
    
    for filename in files_to_process:
        if os.path.exists(filename):
            modified, changes = fix_breadcrumb_spacing(filename)
            if modified:
                total_files += 1
                total_changes += len(changes)
                print(f"✅ {filename}")
                for change in changes:
                    print(f"   • {change}")
            else:
                print(f"⏭️  {filename} - No changes needed")
        else:
            print(f"⚠️  {filename} - File not found")
    
    print(f"\n✨ Complete! Modified {total_files} files with {total_changes} changes")
    print("\n📋 Standardized spacing:")
    print("   Desktop breadcrumbs: margin-bottom: 2rem")
    print("   Mobile breadcrumbs: margin-bottom: 1.5rem")
    print("   Desktop hero: padding: 8rem 2rem 4rem 2rem")
    print("   Mobile hero: padding: 7rem 1rem 3rem 1rem")

if __name__ == "__main__":
    main()
