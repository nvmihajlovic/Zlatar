import re
import os

# List of all blog post files
blog_files = [
    'blog-post-1.html',
    'blog-post-3.html',
    'blog-post-4.html',
    'blog-post-5.html',
    'blog-post-6.html',
    'blog-post-7.html',
    'blog-post-8.html',
    'blog-post-9.html',
    'blog-post-10.html',
    'blog-post-11.html',
    'blog-post-12.html'
]

for blog_file in blog_files:
    if not os.path.exists(blog_file):
        print(f"⚠️  File {blog_file} not found, skipping...")
        continue
    
    with open(blog_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update modal max-width from 500px to 650px
    content = re.sub(
        r'max-width: 500px;',
        'max-width: 650px;',
        content
    )
    
    # Update grid from 2 columns to 3 columns
    content = re.sub(
        r'grid-template-columns: repeat\(2, 1fr\);',
        'grid-template-columns: repeat(3, 1fr);',
        content
    )
    
    # Write updated content
    with open(blog_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated {blog_file}")

print("\n🎉 All blog posts updated with wider modal and 3-column grid!")
