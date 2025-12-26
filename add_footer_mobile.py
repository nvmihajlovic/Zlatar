import codecs
import re

# Footer mobile CSS to add
footer_mobile_css = '''
            
            /* Footer mobilni */
            .footer {
                padding: 3rem 0 1.5rem 0 !important;
            }
            .footer-grid {
                grid-template-columns: 1fr !important;
                gap: 3rem !important;
                margin-bottom: 3rem !important;
            }
            .footer-col {
                text-align: left !important;
            }
            .footer-col h4 {
                border-image: linear-gradient(90deg, #D4AF37 0%, rgba(212,175,55,0.3) 50%, transparent 100%) 1 !important;
                max-width: 200px !important;
                margin-left: 0 !important;
                margin-right: auto !important;
                margin-bottom: 1.5rem !important;
            }
            .footer-desc {
                max-width: 90% !important;
                margin-left: 0 !important;
                margin-right: auto !important;
                font-size: 0.9375rem !important;
            }
            .footer-contact-info {
                display: flex !important;
                flex-direction: column !important;
                align-items: flex-start !important;
                gap: 0.75rem !important;
            }
            .footer-socials {
                justify-content: flex-start !important;
                gap: 1rem !important;
            }
            .footer-links {
                align-items: flex-start !important;
                gap: 1rem !important;
            }
            .footer-links li {
                justify-content: flex-start !important;
            }
            .newsletter-form {
                max-width: 320px !important;
                margin: 0 !important;
            }
        }
    </style>'''

# Update blog-post-2 through blog-post-12
for i in range(2, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if footer mobile CSS already exists
        if '/* Footer mobilni */' in content:
            print(f"✓ {filename} - већ има footer mobilni CSS")
            continue
        
        # Add footer mobile CSS before closing of @media (max-width: 768px) block
        content = content.replace(
            '            .back-to-blog {\n                padding: 0.875rem 1.5rem;\n                font-size: 0.9rem;\n            }\n        }\n    </style>',
            '            .back-to-blog {\n                padding: 0.875rem 1.5rem;\n                font-size: 0.9rem;\n            }' + footer_mobile_css
        )
        
        # Write updated content
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Додат footer mobilni CSS у {filename}")
        
    except FileNotFoundError:
        print(f"✗ Није пронађено: {filename}")
    except Exception as e:
        print(f"✗ Грешка у {filename}: {str(e)}")

print("\nЗавршено! Footer mobilni CSS додат на свим страницама.")
