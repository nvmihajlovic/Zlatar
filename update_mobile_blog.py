import codecs
import re

# Mobile CSS improvements to apply
mobile_css = '''        @media (max-width: 1024px) {
            .article__wrapper {
                grid-template-columns: 1fr;
            }

            .toc {
                display: none;
            }

            .related-posts__grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 2rem;
                padding: 0 2rem;
            }
        }

        @media (max-width: 768px) {
            .blog-hero {
                min-height: 50vh;
                padding: 6rem 1.5rem 3rem 1.5rem;
            }
            
            .blog-hero__title {
                font-size: 2rem;
            }
            
            .blog-hero__meta {
                gap: 1rem;
                font-size: 0.875rem;
            }

            .article__content {
                padding: 2rem 1.5rem;
                border-radius: 16px;
            }

            .article__content h2 {
                font-size: 1.5rem;
            }

            .article__content h3 {
                font-size: 1.25rem;
            }

            .article__content p {
                font-size: 0.9375rem;
            }

            .related-posts__grid {
                grid-template-columns: 1fr;
                gap: 1.5rem;
                padding: 0 1rem;
            }
            
            .related-posts {
                padding: 3rem 0;
                margin: 3rem auto;
                border-radius: 16px;
            }
            
            .related-posts__title {
                font-size: 1.75rem;
                margin-bottom: 2rem;
            }

            .author-bio {
                flex-direction: column;
                text-align: center;
                padding: 2rem 1.5rem;
            }
            
            .article-like__button {
                padding: 1rem 2rem;
                font-size: 1rem;
            }
            
            .share-buttons {
                justify-content: center;
                flex-wrap: wrap;
            }
            
            .back-to-blog {
                padding: 0.875rem 1.5rem;
                font-size: 0.9rem;
            }
        }
    </style>'''

# Update blog-post-2 through blog-post-12
for i in range(2, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the media queries section
        pattern = r'@media \(max-width: 1024px\).*?</style>'
        
        content = re.sub(pattern, mobile_css, content, flags=re.DOTALL)
        
        # Write updated content
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Ажурирана мобилна респонзивност: {filename}")
        
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Мобилна респонзивност побољшана на свим страницама.")
