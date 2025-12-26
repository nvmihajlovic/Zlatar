import re
from pathlib import Path

# Poboljšani CSS stilovi sa !important za active state
improved_toc_link_css = """        .toc__link {
            color: rgba(255,255,255,0.65);
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
            transition: all 0.3s ease;
            display: block;
            padding: 0.75rem 1rem;
            border-left: 3px solid transparent;
            border-radius: 0 8px 8px 0;
            position: relative;
            overflow: hidden;
        }
        
        .toc__link::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            width: 0;
            height: 100%;
            background: linear-gradient(90deg, rgba(212,175,55,0.1) 0%, transparent 100%);
            transition: width 0.3s;
            z-index: -1;
        }
        
        .toc__link:hover,
        .toc__link.active {
            color: #FFD700 !important;
            border-left-color: #D4AF37 !important;
            transform: translateX(5px);
        }
        
        .toc__link:hover::before,
        .toc__link.active::before {
            width: 100%;
        }
        
        .toc__link.active {
            font-weight: 700 !important;
            background: rgba(212,175,55,0.08) !important;
            border-left-color: #FFD700 !important;
            box-shadow: inset 0 0 20px rgba(212,175,55,0.1);
        }
"""

def fix_toc_active_styles(file_path):
    """Popravlja active stilove za TOC linkove."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern koji pokriva .toc__link stilove
    pattern = r'(        \.toc__link \{[\s\S]*?)(        \.toc__link:hover \{[\s\S]*?\n        \})'
    
    new_content = re.sub(pattern, improved_toc_link_css, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Procesuj sve blog post fajlove osim blog-post-1.html (već ažuriran)
blog_posts = [p for p in Path('.').glob('blog-post-*.html') if p.name != 'blog-post-1.html']
success_count = 0

for post in sorted(blog_posts):
    if fix_toc_active_styles(post):
        success_count += 1
        print(f"✅ Popravljeni active stilovi u: {post.name}")
    else:
        print(f"⚠️  Pattern nije pronađen u: {post.name}")

print(f"\n✅ Završeno! Uspešno ažurirano {success_count}/{len(blog_posts)} stranica")
print("\n🎨 Refresh blog-post-1.html - sada bi active TOC link trebalo da se JASNO vidi!")
