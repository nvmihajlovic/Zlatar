import re
from pathlib import Path

# Poboljšani CSS za sticky TOC
improved_sticky_css = """        
        .article__wrapper {
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: 4rem;
            max-width: 1400px;
            align-items: start;
        }
        
        /* Enhanced Table of Contents - Fixed Sticky */
        .toc {
            position: -webkit-sticky;
            position: sticky;
            top: 120px;
            align-self: start;
            height: fit-content;
            max-height: calc(100vh - 140px);
            overflow-y: auto;
            background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(212,175,55,0.15);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            z-index: 10;
        }
        
        .toc::-webkit-scrollbar {
            width: 4px;
        }
        
        .toc::-webkit-scrollbar-track {
            background: rgba(255,255,255,0.05);
            border-radius: 2px;
        }
        
        .toc::-webkit-scrollbar-thumb {
            background: rgba(212,175,55,0.5);
            border-radius: 2px;
        }
        
        .toc::-webkit-scrollbar-thumb:hover {
            background: rgba(212,175,55,0.7);
        }
"""

def fix_sticky_toc(file_path):
    """Popravlja sticky TOC dodavanjem align-items: start i drugih stilova."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Zameni .article__wrapper i .toc stilove
    pattern = r'(        \.article__wrapper \{\s+display: grid;\s+grid-template-columns: 250px 1fr;\s+gap: 4rem;\s+max-width: 1400px;\s+\})\s+(        /\* (?:Table of Contents|Enhanced Table of Contents)[^*]*\*/)(\s+        \.toc \{[^}]+\})'
    
    replacement = improved_sticky_css.rstrip() + '\n'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Procesuj sve blog post fajlove
blog_posts = list(Path('.').glob('blog-post-*.html'))
success_count = 0

for post in sorted(blog_posts):
    if fix_sticky_toc(post):
        success_count += 1
        print(f"✅ Popravljen sticky TOC u: {post.name}")
    else:
        print(f"⚠️  Pattern nije pronađen ili već ispravan u: {post.name}")

print(f"\n✅ Završeno! Uspešno ažurirano {success_count}/{len(blog_posts)} stranica")
