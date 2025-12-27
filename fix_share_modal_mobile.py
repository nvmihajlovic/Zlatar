import codecs
import re

print("🔧 Приlagођавам share modal за мобилни приказ...\n")

# CSS for mobile share modal
mobile_share_css = """
    <style>
        /* Share Modal Mobile Responsive */
        @media (max-width: 768px) {
            #shareModal > div {
                padding: 2rem 1.25rem !important;
                width: 95% !important;
                max-width: none !important;
                margin: 1rem !important;
                max-height: 85vh !important;
                overflow-y: auto !important;
            }
            
            #shareModal h3 {
                font-size: 1.375rem !important;
                margin-bottom: 1.25rem !important;
            }
            
            #shareModal > div > div:first-of-type {
                grid-template-columns: repeat(2, 1fr) !important;
                gap: 0.75rem !important;
            }
            
            #shareModal button {
                padding: 0.875rem 0.5rem !important;
                font-size: 0.875rem !important;
                gap: 0.5rem !important;
            }
            
            #shareModal > div > div:last-of-type {
                margin-top: 1.25rem !important;
                padding: 0.875rem !important;
                flex-direction: column !important;
                gap: 0.75rem !important;
            }
            
            #shareLink {
                font-size: 0.8125rem !important;
                text-align: center !important;
            }
            
            #shareModal button[onclick="copyLink()"] {
                width: 100% !important;
                padding: 0.75rem 1rem !important;
            }
        }
        
        @media (max-width: 480px) {
            #shareModal > div {
                padding: 1.5rem 1rem !important;
            }
            
            #shareModal h3 {
                font-size: 1.25rem !important;
            }
            
            #shareModal button {
                font-size: 0.8125rem !important;
                padding: 0.75rem 0.375rem !important;
            }
            
            #shareModal button i {
                font-size: 1rem !important;
            }
        }
    </style>"""

# Process all blog post files
for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find shareModal and add mobile CSS before it
        if '<div id="shareModal"' in content:
            # Insert mobile CSS before shareModal
            content = content.replace(
                '<div id="shareModal"',
                mobile_share_css + '\n\n    <div id="shareModal"'
            )
            
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Ажуриран {filename}")
        else:
            print(f"⚠ Share modal nije pronađen u {filename}")
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

print("\n✅ ГОТОВО! Share modal је приlagођен за мобилни приказ.")
