#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob

def fix_blog_post_css(filepath):
    """Popravlja CSS strukturu na blog post stranicama"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Ukloni sve pobrljane CSS blokove između @media (max-width: 768px) i </style>
        # Pronađi kraj @media (max-width: 768px) sekcije
        pattern = r'(@media \(max-width: 768px\) \{[^}]*?\.modal-header h2 \{[^}]*?\}\s*\})\s*(?:/\* Mobile Navigation Styles \*/)?[\s\S]*?(?=</style>)'
        
        replacement = r'''\1

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
            
            body.menu-open::before {
                content: '';
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.7);
                backdrop-filter: blur(4px);
                z-index: 999;
                animation: fadeIn 0.3s;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            .nav-actions .language-switcher {
                display: none !important;
            }
        }
        
        @media (min-width: 1282px) {
            .nav-toggle {
                display: none !important;
            }
        }
        
        .nav-link:hover {
            background: linear-gradient(135deg, rgba(212,175,55,0.25) 0%, rgba(212,175,55,0.15) 100%) !important;
            border-color: rgba(212,175,55,0.45) !important;
            color: #FFD700 !important;
            box-shadow: 0 8px 24px rgba(212,175,55,0.35), inset 0 1px 0 rgba(255,255,255,0.15) !important;
        }
        
        .nav-logo:hover {
            transform: scale(1.05) !important;
        }
        
        .lang-btn:hover {
            filter: grayscale(0) !important;
            opacity: 1 !important;
            transform: scale(1.2);
        }
        
        .lang-btn.active {
            filter: grayscale(0) !important;
            opacity: 1 !important;
            box-shadow: 0 0 20px rgba(212,175,55,0.5);
        }
        
        .btn-reserve:hover {
            transform: translateY(-2px) scale(1.03);
            box-shadow: 0 8px 30px rgba(212,175,55,0.6), inset 0 1px 0 rgba(255,255,255,0.4) !important;
            background: linear-gradient(135deg, #FFD700 0%, #D4AF37 100%) !important;
        }
    '''
        
        content = re.sub(pattern, replacement, content)
        
        # Sačuvaj promene
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Popravljeno: {os.path.basename(filepath)}")
        return True
    except Exception as e:
        print(f"✗ Greška kod {os.path.basename(filepath)}: {str(e)}")
        return False

def main():
    # Pronađi sve blog post datoteke
    blog_posts = glob.glob('blog-post-*.html')
    
    if not blog_posts:
        print("Nisu pronađene blog post stranice!")
        return
    
    print(f"\n🔧 Pronađeno {len(blog_posts)} blog post stranica\n")
    
    success_count = 0
    for filepath in sorted(blog_posts):
        if fix_blog_post_css(filepath):
            success_count += 1
    
    print(f"\n✅ Završeno! Uspešno popravljeno {success_count}/{len(blog_posts)} stranica\n")

if __name__ == '__main__':
    main()
