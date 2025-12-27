import codecs
import re

print("✨ Финална оптимизација UI/UX...\n")

# CSS енхенцементи који неће покварити функционалности
enhancements_css = """
<style>
/* UI/UX Final Polish - Не дира постојеће функционалности */

/* Smooth hover effects for all links */
a:not([onclick]):not(.btn) {
    transition: color 0.3s ease, opacity 0.3s ease !important;
}

a:not([onclick]):not(.btn):hover {
    opacity: 0.85;
}

/* Better focus states for accessibility */
button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
    outline: 2px solid rgba(212,175,55,0.5);
    outline-offset: 2px;
}

/* Smooth animations for modals */
.modal {
    animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* Better button hover states */
button:not(:disabled):hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.15) !important;
}

button:not(:disabled):active {
    transform: translateY(0);
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
}

/* Better mobile touch targets */
@media (max-width: 768px) {
    button,
    a {
        min-height: 44px;
        min-width: 44px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
}

/* Loading skeleton animation */
@keyframes skeleton-loading {
    0% {
        background-position: 200% 0;
    }
    100% {
        background-position: -200% 0;
    }
}

/* Accessibility: Reduced motion */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Print styles */
@media print {
    nav,
    footer,
    .modal,
    button:not(.print-visible) {
        display: none !important;
    }
}
</style>
"""

# Apply to all pages
pages = ['index.html', 'about.html', 'menu.html', 'wine.html', 'gallery.html', 'contact.html', 'blog.html']
blog_posts = [f'blog-post-{i}.html' for i in range(1, 13)]
all_pages = pages + blog_posts

for page in all_pages:
    try:
        with codecs.open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Proveri da li već ima ove стилове
        if 'UI/UX Final Polish' in content:
            print(f"⏭ {page} већ има финалне стилове")
            continue
        
        # Додај пре затварајућег </head> тага
        if '</head>' in content:
            content = content.replace('</head>', enhancements_css + '\n</head>')
            
            with codecs.open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Оптимизован {page}")
        else:
            print(f"⚠ {page} нема </head> таг")
    
    except FileNotFoundError:
        print(f"⏭ {page} не постоји")
    except Exception as e:
        print(f"✗ Грешка код {page}: {e}")

print("\n✅ ГОТОВО! Сви UX енханцементи примењени.")
print("   - Smooth hover ефекти")
print("   - Better focus states за приступачност")
print("   - Smooth modal анимације")
print("   - Better button interactions")
print("   - Mobile touch targets")
print("   - Accessibility: Reduced motion подршка")
print("   - Print stylesheet")
print("\n💡 ВАЖНО: Like и Share функционалности НИСУ дирнуте!")
