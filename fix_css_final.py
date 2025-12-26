import re
from pathlib import Path

def fix_blog_post_css(file_path):
    """Uklanja prazne zagrade i popravlja CSS strukturu."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pronađi gde se završava @media (max-width: 768px) i gde počinje body.menu-open::before
    # Između toga treba da stavimo @media (max-width: 1281px) sa stilovima za mobilni meni
    
    mobile_nav_css = """

        /* Mobile Navigation Styles */
        @media (max-width: 1281px) {
            .nav-item .nav-link {
                display: block !important;
                width: 100% !important;
                padding: 1rem 1.5rem !important;
                font-size: 1.05rem !important;
            }

            .nav-toggle {
                display: flex !important;
                flex-direction: column;
                justify-content: space-around;
                width: 44px;
                height: 44px;
                background: rgba(255,255,255,0.08) !important;
                backdrop-filter: blur(10px) !important;
                border: 1px solid rgba(255,255,255,0.2) !important;
                border-radius: 12px !important;
                padding: 10px !important;
                cursor: pointer;
                z-index: 1001;
                position: fixed;
                right: 1.5rem;
                top: 1.75rem;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
                transition: all 0.3s ease !important;
            }

            .nav-toggle span {
                width: 24px;
                height: 2px;
                background: #D4AF37;
                border-radius: 2px;
                transition: all 0.3s;
                display: block;
            }

            .nav-toggle.active span:nth-child(1) {
                transform: rotate(45deg) translate(6px, 6px);
            }

            .nav-toggle.active span:nth-child(2) {
                opacity: 0;
            }

            .nav-toggle.active span:nth-child(3) {
                transform: rotate(-45deg) translate(6px, -6px);
            }

            .nav-actions {
                gap: 0 !important;
                padding-left: 0 !important;
            }

            .btn-reserve {
                position: fixed !important;
                right: 5.5rem !important;
                top: 1.5rem !important;
                z-index: 1001 !important;
                margin-left: 0 !important;
                font-size: 0 !important;
                padding: 0 !important;
                width: 48px !important;
                height: 48px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
            }

            .btn-reserve i {
                margin-right: 0 !important;
                font-size: 1.1rem !important;
            }

            .btn-reserve span {
                display: none !important;
            }

            body.menu-open {
                overflow: hidden;
            }
"""
    
    # Pattern: od kraja @media (max-width: 768px) do body.menu-open::before
    pattern = r'(\.modal-header h2 \{\s*font-size: 1\.5rem;\s*\}\s*\})\s*[\s\S]*?(body\.menu-open::before \{)'
    
    replacement = r'\1' + mobile_nav_css + '\n            ' + r'\2'
    
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
    if fix_blog_post_css(post):
        success_count += 1
        print(f"✅ Popravljeno: {post.name}")
    else:
        print(f"⚠️  Nije pronađen pattern u: {post.name}")

print(f"\n✅ Završeno! Uspešno popravljeno {success_count}/{len(blog_posts)} stranica")
