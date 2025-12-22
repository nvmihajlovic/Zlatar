import re

# Contact.html breadcrumbs
with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_breadcrumbs = '''                    <i class="fas fa-home" style="margin-right: 0.5rem;"></i>Почетна
                </a>
                <span style="color: rgba(255, 255, 255, 0.4); margin: 0 0.75rem;">/</span>
                <span style="color: #D4AF37; font-family: 'Montserrat', sans-serif; font-size: 0.9rem;">Контакт</span>'''

new_breadcrumbs = '''                    <i class="fas fa-home" style="margin-right: 0.5rem;"></i><span data-i18n="contact-page.breadcrumb.home">Почетна</span>
                </a>
                <span style="color: rgba(255, 255, 255, 0.4); margin: 0 0.75rem;">/</span>
                <span style="color: #D4AF37; font-family: 'Montserrat', sans-serif; font-size: 0.9rem;" data-i18n="contact-page.breadcrumb.current">Контакт</span>'''

if old_breadcrumbs in content:
    content = content.replace(old_breadcrumbs, new_breadcrumbs)
    print("✓ Updated contact.html breadcrumbs")
else:
    print("✗ Could not find contact.html breadcrumbs")

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Gallery.html breadcrumbs
with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_breadcrumbs = '''                    <i class="fas fa-home" style="margin-right: 0.5rem;"></i>Почетна
                </a>
                <span style="color: rgba(255, 255, 255, 0.4); margin: 0 0.75rem;">/</span>
                <span style="color: #D4AF37; font-family: 'Montserrat', sans-serif; font-size: 0.9rem;">Галерија</span>'''

new_breadcrumbs = '''                    <i class="fas fa-home" style="margin-right: 0.5rem;"></i><span data-i18n="gallery-page.breadcrumb.home">Почетна</span>
                </a>
                <span style="color: rgba(255, 255, 255, 0.4); margin: 0 0.75rem;">/</span>
                <span style="color: #D4AF37; font-family: 'Montserrat', sans-serif; font-size: 0.9rem;" data-i18n="gallery-page.breadcrumb.current">Галерија</span>'''

if old_breadcrumbs in content:
    content = content.replace(old_breadcrumbs, new_breadcrumbs)
    print("✓ Updated gallery.html breadcrumbs")
else:
    print("✗ Could not find gallery.html breadcrumbs")

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n=== BREADCRUMB TRANSLATIONS ===")
print("\nSERBIAN:")
print("        'contact-page.breadcrumb.home': 'Почетна',")
print("        'contact-page.breadcrumb.current': 'Контакт',")
print("        'gallery-page.breadcrumb.home': 'Почетна',")
print("        'gallery-page.breadcrumb.current': 'Галерија',")

print("\nENGLISH:")
print("        'contact-page.breadcrumb.home': 'Home',")
print("        'contact-page.breadcrumb.current': 'Contact',")
print("        'gallery-page.breadcrumb.home': 'Home',")
print("        'gallery-page.breadcrumb.current': 'Gallery',")

print("\nRUSSIAN:")
print("        'contact-page.breadcrumb.home': 'Главная',")
print("        'contact-page.breadcrumb.current': 'Контакт',")
print("        'gallery-page.breadcrumb.home': 'Главная',")
print("        'gallery-page.breadcrumb.current': 'Галерея',")
