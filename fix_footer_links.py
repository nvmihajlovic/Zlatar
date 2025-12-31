"""
Popravi footer linkove na svim HTML stranicama:
- Smanji gap sa 1.1rem na 0.7rem
- Dodaj lepe hover efekte
"""

import os
import re
from pathlib import Path

def fix_footer_links(html_content):
    """Popravi footer linkove"""
    
    # 1. Smanji gap u footer-links
    html_content = re.sub(
        r'(<ul class="footer-links"[^>]*gap:\s*)1\.1rem',
        r'\g<1>0.7rem',
        html_content
    )
    
    # 2. Dodaj hover efekat za footer linkove
    old_link_style = r'font-family: \'Montserrat\', sans-serif; color: rgba\(255,255,255,0\.7\); font-size: 1rem; text-decoration: none; transition: all 0\.[0-9]+s[^;]*; display: inline-block; position: relative;'
    new_link_style = r"font-family: 'Montserrat', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.8s ease-out; display: inline-block; position: relative;"
    
    html_content = re.sub(old_link_style, new_link_style, html_content)
    
    # Ako još nije bilo promenjeno, promeni originalni stil
    old_link_style_orig = r'font-family: \'Montserrat\', sans-serif; color: rgba\(255,255,255,0\.7\); font-size: 1rem; text-decoration: none; transition: all 0\.3s;'
    new_link_style_orig = r"font-family: 'Montserrat', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.8s ease-out; display: inline-block; position: relative;"
    
    html_content = re.sub(old_link_style_orig, new_link_style_orig, html_content)
    
    # 3. Dodaj hover style ako ne postoji u head
    if '<style id="footer-hover-effect">' not in html_content:
        style_tag = '''    <style id="footer-hover-effect">
        .footer-links a:hover {
            color: #FFD700 !important;
            transform: translateX(5px);
            text-shadow: 0 2px 8px rgba(255, 215, 0, 0.3);
        }
        .footer-links a::before {
            content: '';
            position: absolute;
            left: -15px;
            top: 50%;
            transform: translateY(-50%) scaleX(0);
            width: 8px;
            height: 2px;
            background: linear-gradient(90deg, #D4AF37, #FFD700);
            border-radius: 2px;
            transition: transform 0.6s ease;
            box-shadow: 0 0 8px rgba(212, 175, 55, 0.6);
        }
        .footer-links a:hover::before {
            transform: translateY(-50%) scaleX(1);
        }
    </style>
</head>'''
        html_content = html_content.replace('</head>', style_tag)
    
    return html_content


def process_all_html_files():
    """Procesuiraj sve HTML fajlove"""
    
    # Glavne stranice
    main_pages = [
        'index.html', 'about.html', 'menu.html', 'wine.html',
        'blog.html', 'gallery.html', 'contact.html', 'terms.html',
        'privacy.html', 'sitemap.html'
    ]
    
    # Blog postovi
    blog_posts = [f'blog-post-{i}.html' for i in range(1, 13)]
    
    all_pages = main_pages + blog_posts
    
    fixed_count = 0
    
    for filename in all_pages:
        filepath = Path(filename)
        
        if not filepath.exists():
            print(f"⚠️  Preskačem {filename} (ne postoji)")
            continue
        
        try:
            # Učitaj HTML
            with open(filepath, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Proveri da li ima footer linkove
            if 'footer-links' not in html_content:
                print(f"⚠️  Preskačem {filename} (nema footer-links)")
                continue
            
            # Popravi
            new_content = fix_footer_links(html_content)
            
            # Sačuvaj
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            fixed_count += 1
            print(f"✅ Popravljeno: {filename}")
            
        except Exception as e:
            print(f"❌ Greška kod {filename}: {e}")
    
    print(f"\n🎉 Završeno! Popravljeno {fixed_count} stranica.")


if __name__ == '__main__':
    process_all_html_files()
