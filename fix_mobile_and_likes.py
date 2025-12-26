import re
import codecs

# Mobile nav CSS to add
mobile_nav_css = """
    /* Mobile Navigation */
    @media (max-width: 1281px) {
        .nav-menu {
            display: none !important;
        }
        
        .nav-menu.mobile-active {
            display: flex !important;
            position: fixed !important;
            top: 0 !important;
            right: 0 !important;
            width: 320px !important;
            height: 100vh !important;
            background: linear-gradient(180deg, rgba(20,15,8,0.98) 0%, rgba(35,26,15,0.97) 50%, rgba(25,18,10,0.96) 100%) !important;
            backdrop-filter: blur(40px) !important;
            padding: 6rem 2rem 2rem !important;
            flex-direction: column !important;
            gap: 0.5rem !important;
            z-index: 999 !important;
            overflow-y: auto !important;
            box-shadow: -8px 0 32px rgba(0,0,0,0.5) !important;
            border-left: 1px solid rgba(212,175,55,0.2) !important;
        }
        
        .nav-menu .nav-item {
            width: 100%;
        }
        
        .nav-menu .nav-link {
            width: 100%;
            padding: 1rem 1.5rem !important;
            justify-content: flex-start;
        }
        
        .nav-actions {
            flex-direction: column;
            align-items: stretch !important;
            gap: 1rem !important;
            padding-left: 0 !important;
        }
        
        .language-switcher {
            justify-content: center;
            width: 100%;
        }
        
        .btn-reserve {
            width: 100%;
        }
    }

    @media (min-width: 1282px) {
        .nav-toggle {
            display: none !important;
        }
    }
"""

# Fix blog-post files
print("🔧 Поправљам blog-post странице...\n")

for i in range(1, 13):
    filename = f'blog-post-{i}.html'
    
    try:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove duplicate mobile nav CSS blocks
        # Remove all existing @media (max-width: 1281px) and @media (min-width: 1282px) blocks
        content = re.sub(
            r'@media \(max-width: 1281px\) \{[^\}]*\{[^\}]*\}[^\}]*\}',
            '',
            content,
            flags=re.DOTALL
        )
        
        content = re.sub(
            r'@media \(min-width: 1282px\) \{[^\}]*\}',
            '',
            content
        )
        
        # Add new mobile nav CSS before </style>
        if '</style>' in content:
            content = content.replace('</style>', mobile_nav_css + '\n    </style>')
            print(f"✓ Додат mobile nav CSS у {filename}")
        else:
            print(f"⚠ Нисам пронашао </style> у {filename}")
        
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    except FileNotFoundError:
        print(f"✗ Фајл {filename} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {filename}: {e}")

# Fix blog.html like button styling
print("\n🔧 Поправљам like button на blog.html...\n")

try:
    with codecs.open('blog.html', 'r', encoding='utf-8') as f:
        blog_content = f.read()
    
    # Find and replace .blog-card__stat styles
    old_stat_css = r'\.blog-card__stat \{[^\}]*\}'
    
    new_stat_css = """.blog-card__stat {
            display: flex;
            align-items: center;
            gap: 0.4rem;
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.875rem;
            transition: all 0.3s;
            background: none;
            border: none;
            cursor: pointer;
            padding: 0;
        }"""
    
    blog_content = re.sub(old_stat_css, new_stat_css, blog_content, flags=re.DOTALL)
    
    # Add like button specific styles after .blog-card__stat
    like_btn_css = """
        
        .blog-card__stat.like-btn {
            position: relative;
        }
        
        .blog-card__stat.like-btn.liked {
            color: #ff4757;
        }
        
        .blog-card__stat.like-btn.liked i {
            animation: heartBeat 0.3s ease;
        }
        
        @keyframes heartBeat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.3); }
        }
        
        .blog-card__stat.like-btn:hover {
            color: #ff4757;
            transform: translateY(-2px);
        }
        
        .blog-card__stat.like-btn:active {
            transform: translateY(0);
        }"""
    
    # Insert after .blog-card__stat definition
    blog_content = re.sub(
        r'(\.blog-card__stat \{[^\}]*\})',
        r'\1' + like_btn_css,
        blog_content,
        flags=re.DOTALL
    )
    
    with codecs.open('blog.html', 'w', encoding='utf-8') as f:
        f.write(blog_content)
    
    print("✓ Додати стилови за like button у blog.html")

except Exception as e:
    print(f"✗ Грешка код blog.html: {e}")

print("\n✅ Готово!")
print("\nПромене:")
print("  ✓ Додат mobile nav CSS на све blog-post странице")
print("  ✓ Уклоњени дупликати mobile CSS-а")
print("  ✓ Поправљен стил за like button (црвено срце, анимација)")
print("  ✓ Mobile meni сада ради на свим страницама")
