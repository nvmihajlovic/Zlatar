import re
from pathlib import Path

# Stilovi koji nedostaju za blog post stranice
blog_post_styles = """
        /* Blog Post Hero Section */
        .blog-hero {
            position: relative;
            min-height: 70vh;
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
            filter: brightness(0.4);
        }
        
        .blog-hero__overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.7) 100%);
        }
        
        .blog-hero__content {
            position: relative;
            z-index: 2;
            max-width: 900px;
            padding: 2rem;
            text-align: center;
        }
        
        .blog-hero__breadcrumbs {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            font-size: 0.9rem;
        }
        
        .blog-hero__breadcrumbs a {
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .blog-hero__breadcrumbs a:hover {
            color: #D4AF37;
        }
        
        .blog-hero__breadcrumbs i {
            color: rgba(255,255,255,0.5);
            font-size: 0.7rem;
        }
        
        .blog-hero__category {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: rgba(212,175,55,0.2);
            border: 1px solid rgba(212,175,55,0.4);
            border-radius: 50px;
            color: #FFD700;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .blog-hero__title {
            font-size: clamp(2rem, 5vw, 3.5rem);
            font-weight: 800;
            margin-bottom: 2rem;
            line-height: 1.2;
        }
        
        .blog-hero__meta {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1.5rem;
        }
        
        .blog-hero__meta-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: rgba(255,255,255,0.8);
            font-size: 0.9rem;
        }
        
        .blog-hero__meta-item i {
            color: #D4AF37;
        }
        
        /* Article Section */
        .article {
            background: #0A0A0A;
            padding: 4rem 0;
        }
        
        .back-to-blog {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            font-size: 0.95rem;
            margin-bottom: 3rem;
            transition: all 0.3s;
        }
        
        .back-to-blog:hover {
            color: #D4AF37;
            transform: translateX(-5px);
        }
        
        .back-to-blog i {
            transition: transform 0.3s;
        }
        
        .back-to-blog:hover i {
            transform: translateX(-3px);
        }
        
        .article__wrapper {
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: 4rem;
            max-width: 1400px;
        }
        
        /* Table of Contents */
        .toc {
            position: sticky;
            top: 120px;
            height: fit-content;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 2rem;
        }
        
        .toc__title {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            color: #D4AF37;
        }
        
        .toc__list {
            list-style: none;
            padding: 0;
        }
        
        .toc__item {
            margin-bottom: 1rem;
        }
        
        .toc__link {
            color: rgba(255,255,255,0.7);
            text-decoration: none;
            font-size: 0.9rem;
            transition: all 0.3s;
            display: block;
            padding: 0.5rem 0;
            border-left: 2px solid transparent;
            padding-left: 1rem;
        }
        
        .toc__link:hover {
            color: #D4AF37;
            border-left-color: #D4AF37;
            transform: translateX(5px);
        }
        
        /* Article Main Content */
        .article__main {
            max-width: 800px;
        }
        
        .article__content {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 3rem;
            margin-bottom: 3rem;
        }
        
        .article__content p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: rgba(255,255,255,0.85);
            margin-bottom: 1.5rem;
        }
        
        .article__content h2 {
            font-size: 2rem;
            font-weight: 700;
            color: #fff;
            margin: 3rem 0 1.5rem 0;
            padding-top: 1rem;
        }
        
        .article__content h3 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #fff;
            margin: 2rem 0 1rem 0;
        }
        
        .article__content ul, 
        .article__content ol {
            margin: 1.5rem 0;
            padding-left: 2rem;
        }
        
        .article__content li {
            font-size: 1.1rem;
            line-height: 1.8;
            color: rgba(255,255,255,0.85);
            margin-bottom: 0.75rem;
        }
        
        .article__content blockquote {
            background: rgba(212,175,55,0.05);
            border-left: 4px solid #D4AF37;
            padding: 1.5rem 2rem;
            margin: 2rem 0;
            font-style: italic;
            font-size: 1.2rem;
            color: rgba(255,255,255,0.9);
        }
        
        /* Like Section */
        .article-like {
            text-align: center;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 3rem;
            margin-bottom: 2rem;
        }
        
        .article-like__text {
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
            color: rgba(255,255,255,0.9);
        }
        
        .article-like__button {
            background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
            color: #fff;
            border: none;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        .article-like__button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(212,175,55,0.4);
        }
        
        .article-like__button.liked {
            background: linear-gradient(135deg, #c92a2a 0%, #e03131 100%);
        }
        
        .article-like__button.liked i {
            animation: heartBeat 0.3s;
        }
        
        @keyframes heartBeat {
            0%, 100% { transform: scale(1); }
            25% { transform: scale(1.3); }
            50% { transform: scale(1); }
            75% { transform: scale(1.2); }
        }
        
        /* Share Buttons */
        .share-buttons {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 3rem;
            padding: 2rem;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
        }
        
        .share-buttons__title {
            font-weight: 600;
            color: rgba(255,255,255,0.9);
        }
        
        .share-buttons__btn {
            width: 45px;
            height: 45px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 50%;
            color: rgba(255,255,255,0.7);
            transition: all 0.3s;
            text-decoration: none;
        }
        
        .share-buttons__btn:hover {
            background: #D4AF37;
            color: #fff;
            transform: translateY(-3px);
        }
        
        /* Author Bio */
        .author-bio {
            display: flex;
            gap: 2rem;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 2.5rem;
            margin-bottom: 3rem;
        }
        
        .author-bio__avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            font-weight: 700;
            flex-shrink: 0;
        }
        
        .author-bio__content h3 {
            font-size: 1.3rem;
            margin-bottom: 0.75rem;
            color: #fff;
        }
        
        .author-bio__content p {
            color: rgba(255,255,255,0.7);
            line-height: 1.6;
        }
        
        /* Related Posts */
        .related-posts {
            margin-top: 4rem;
        }
        
        .related-posts__title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .related-posts__grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
        }
        
        .related-post-card {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .related-post-card:hover {
            transform: translateY(-5px);
            border-color: rgba(212,175,55,0.3);
            box-shadow: 0 12px 30px rgba(0,0,0,0.3);
        }
        
        .related-post-card__image-wrapper {
            position: relative;
            height: 200px;
            overflow: hidden;
        }
        
        .related-post-card__image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }
        
        .related-post-card:hover .related-post-card__image {
            transform: scale(1.1);
        }
        
        .related-post-card__category {
            position: absolute;
            top: 1rem;
            left: 1rem;
            padding: 0.4rem 0.8rem;
            background: rgba(212,175,55,0.9);
            color: #fff;
            font-size: 0.75rem;
            font-weight: 600;
            border-radius: 50px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .related-post-card__content {
            padding: 1.5rem;
        }
        
        .related-post-card__title {
            margin-bottom: 1rem;
        }
        
        .related-post-card__title a {
            color: #fff;
            text-decoration: none;
            font-size: 1.1rem;
            font-weight: 600;
            line-height: 1.4;
            transition: color 0.3s;
        }
        
        .related-post-card__title a:hover {
            color: #D4AF37;
        }
        
        .related-post-card__meta {
            display: flex;
            gap: 1rem;
            font-size: 0.85rem;
            color: rgba(255,255,255,0.6);
        }
        
        .related-post-card__meta-item {
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
        
        .related-post-card__meta-item i {
            color: #D4AF37;
            font-size: 0.8rem;
        }
        
        /* Responsive for Blog Post */
        @media (max-width: 1200px) {
            .article__wrapper {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
            
            .toc {
                position: static;
                max-width: 300px;
            }
            
            .related-posts__grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 768px) {
            .blog-hero {
                min-height: 50vh;
            }
            
            .blog-hero__content {
                padding: 1rem;
            }
            
            .blog-hero__title {
                font-size: 1.8rem;
            }
            
            .article {
                padding: 2rem 0;
            }
            
            .article__content {
                padding: 2rem 1.5rem;
            }
            
            .toc {
                display: none;
            }
            
            .author-bio {
                flex-direction: column;
                text-align: center;
                align-items: center;
            }
            
            .related-posts__grid {
                grid-template-columns: 1fr;
            }
            
            .share-buttons {
                flex-wrap: wrap;
            }
        }
"""

def add_styles_to_blog_post(file_path):
    """Dodaje nedostajuće stilove za blog post stranicu."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Proveri da li stilovi već postoje
    if '.blog-hero__content {' in content:
        return False
    
    # Pronađi prvi </style> tag i dodaj stilove PRIJE njega
    pattern = r'(\.btn-reserve:hover \{[^}]+\}\s*)(    </style>)'
    replacement = r'\1' + blog_post_styles + r'\2'
    
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
    if add_styles_to_blog_post(post):
        success_count += 1
        print(f"✅ Dodati stilovi u: {post.name}")
    else:
        print(f"⚠️  Stilovi već postoje ili pattern nije pronađen u: {post.name}")

print(f"\n✅ Završeno! Uspešno ažurirano {success_count}/{len(blog_posts)} stranica")
