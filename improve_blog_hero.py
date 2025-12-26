import re
from pathlib import Path

# Poboljšani stilovi za blog post hero sekciju
improved_hero_styles = """        /* Blog Post Hero Section - Improved */
        .blog-hero {
            position: relative;
            min-height: 75vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            margin-top: 80px;
        }
        
        .blog-hero__image {
            position: absolute;
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: brightness(0.35);
            animation: zoomIn 20s ease infinite alternate;
        }
        
        @keyframes zoomIn {
            from { transform: scale(1); }
            to { transform: scale(1.05); }
        }
        
        .blog-hero__overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, 
                rgba(0,0,0,0.2) 0%, 
                rgba(10,10,10,0.6) 40%,
                rgba(20,15,8,0.85) 100%);
            backdrop-filter: blur(1px);
        }
        
        .blog-hero__content {
            position: relative;
            z-index: 2;
            max-width: 950px;
            padding: 3rem 2rem;
            text-align: center;
            animation: fadeInUp 0.8s ease;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .blog-hero__breadcrumbs {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            margin-bottom: 2rem;
            font-size: 0.9rem;
            animation: fadeIn 1s ease 0.2s both;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .blog-hero__breadcrumbs a {
            color: rgba(255,255,255,0.75);
            text-decoration: none;
            transition: all 0.3s;
            position: relative;
            font-weight: 500;
        }
        
        .blog-hero__breadcrumbs a::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #FFD700, #D4AF37);
            transition: width 0.3s;
        }
        
        .blog-hero__breadcrumbs a:hover {
            color: #FFD700;
        }
        
        .blog-hero__breadcrumbs a:hover::after {
            width: 100%;
        }
        
        .blog-hero__breadcrumbs span {
            color: rgba(255,255,255,0.9);
            font-weight: 600;
        }
        
        .blog-hero__breadcrumbs i {
            color: rgba(212,175,55,0.6);
            font-size: 0.65rem;
        }
        
        .blog-hero__category {
            display: inline-block;
            padding: 0.65rem 1.5rem;
            background: linear-gradient(135deg, rgba(212,175,55,0.25) 0%, rgba(212,175,55,0.15) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(212,175,55,0.5);
            border-radius: 50px;
            color: #FFD700;
            font-size: 0.8rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            box-shadow: 0 4px 20px rgba(212,175,55,0.2),
                        inset 0 1px 0 rgba(255,255,255,0.1);
            animation: fadeIn 1s ease 0.4s both;
            transition: all 0.3s;
        }
        
        .blog-hero__category:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(212,175,55,0.35),
                        inset 0 1px 0 rgba(255,255,255,0.2);
        }
        
        .blog-hero__title {
            font-size: clamp(2.2rem, 5.5vw, 4rem);
            font-weight: 900;
            margin-bottom: 2.5rem;
            line-height: 1.15;
            letter-spacing: -0.02em;
            background: linear-gradient(180deg, #FFFFFF 0%, rgba(255,255,255,0.95) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 4px 20px rgba(0,0,0,0.3);
            animation: fadeIn 1s ease 0.6s both;
        }
        
        .blog-hero__meta {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 2rem;
            animation: fadeIn 1s ease 0.8s both;
        }
        
        .blog-hero__meta-item {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            color: rgba(255,255,255,0.85);
            font-size: 0.95rem;
            font-weight: 500;
            padding: 0.5rem 1rem;
            background: rgba(255,255,255,0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 50px;
            transition: all 0.3s;
        }
        
        .blog-hero__meta-item:hover {
            background: rgba(212,175,55,0.1);
            border-color: rgba(212,175,55,0.3);
            transform: translateY(-2px);
        }
        
        .blog-hero__meta-item i {
            color: #D4AF37;
            font-size: 0.9rem;
            transition: transform 0.3s;
        }
        
        .blog-hero__meta-item:hover i {
            transform: scale(1.15);
        }"""

def update_blog_hero_styles(file_path):
    """Zamenjuje postojeće blog-hero stilove poboljšanim verzijama."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern koji pokriva postojeće blog-hero stilove
    pattern = r'(        /\* Blog Post Hero Section[^*]*\*/)[\s\S]*?(        /\* Article Section \*/)'
    
    replacement = improved_hero_styles + '\n\n' + r'        /* Article Section */'
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Procesuj sve blog post fajlove
blog_posts = list(Path('.').glob('blog-post-*.html'))
success_count = 0

for post in sorted(blog_posts):
    if update_blog_hero_styles(post):
        success_count += 1
        print(f"✅ Ažuriran hero u: {post.name}")
    else:
        print(f"⚠️  Pattern nije pronađen u: {post.name}")

print(f"\n✅ Završeno! Uspešno ažurirano {success_count}/{len(blog_posts)} stranica")
