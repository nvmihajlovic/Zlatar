# -*- coding: utf-8 -*-
"""
Script to add data-i18n attributes to wine.html and generate translations
"""
import re

# Read wine.html
with open('wine.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Translations for category titles
category_translations = {
    'sr': {
        'wine-page.category.champagne.title': 'Шампањац & Пенушава вина',
        'wine-page.category.champagne.desc': 'Врхунски шампањци и пенушава вина за посебне тренутке',
        'wine-page.category.white.title': 'Бела вина',
        'wine-page.category.white.desc': 'Освежавајућа и елегантна бела вина',
        'wine-page.category.red.title': 'Црвена вина',
        'wine-page.category.red.desc': 'Богата и комплексна црвена вина',
        'wine-page.category.rose.title': 'Розе вина',
        'wine-page.category.rose.desc': 'Лагана и освежавајућа розе вина',
        'wine-page.category.dessert.title': 'Десертна & Специјална вина',
        'wine-page.category.dessert.desc': 'Слатка и десертна вина за посебне тренутке',
        'wine-page.category.glass.title': 'Вино на чашу',
        'wine-page.category.glass.desc': 'Изабрана вина по чаши',
    },
    'en': {
        'wine-page.category.champagne.title': 'Champagne & Sparkling Wines',
        'wine-page.category.champagne.desc': 'Premium champagnes and sparkling wines for special moments',
        'wine-page.category.white.title': 'White Wines',
        'wine-page.category.white.desc': 'Refreshing and elegant white wines',
        'wine-page.category.red.title': 'Red Wines',
        'wine-page.category.red.desc': 'Rich and complex red wines',
        'wine-page.category.rose.title': 'Rosé Wines',
        'wine-page.category.rose.desc': 'Light and refreshing rosé wines',
        'wine-page.category.dessert.title': 'Dessert & Special Wines',
        'wine-page.category.dessert.desc': 'Sweet and dessert wines for special occasions',
        'wine-page.category.glass.title': 'Wine by the Glass',
        'wine-page.category.glass.desc': 'Selected wines by the glass',
    },
    'ru': {
        'wine-page.category.champagne.title': 'Шампанское и игристые вина',
        'wine-page.category.champagne.desc': 'Премиальное шампанское и игристые вина для особых моментов',
        'wine-page.category.white.title': 'Белые вина',
        'wine-page.category.white.desc': 'Освежающие и элегантные белые вина',
        'wine-page.category.red.title': 'Красные вина',
        'wine-page.category.red.desc': 'Насыщенные и сложные красные вина',
        'wine-page.category.rose.title': 'Розовые вина',
        'wine-page.category.rose.desc': 'Легкие и освежающие розовые вина',
        'wine-page.category.dessert.title': 'Десертные и специальные вина',
        'wine-page.category.dessert.desc': 'Сладкие и десертные вина для особых случаев',
        'wine-page.category.glass.title': 'Вино по бокалам',
        'wine-page.category.glass.desc': 'Избранные вина по бокалам',
    }
}

# Add data-i18n to category titles
patterns = [
    (r'<h2 class="category-title">Шампањац & Пенушава вина</h2>',
     '<h2 class="category-title"><span data-i18n="wine-page.category.champagne.title">Шампањац & Пенушава вина</span></h2>'),
    (r'<p class="category-description">Врхунски шампањци и пенушава вина за посебне тренутке</p>',
     '<p class="category-description"><span data-i18n="wine-page.category.champagne.desc">Врхунски шампањци и пенушава вина за посебне тренутке</span></p>'),
    (r'<h2 class="category-title">Бела вина</h2>',
     '<h2 class="category-title"><span data-i18n="wine-page.category.white.title">Бела вина</span></h2>'),
    (r'<p class="category-description">Освежавајућа и елегантна бела вина</p>',
     '<p class="category-description"><span data-i18n="wine-page.category.white.desc">Освежавајућа и елегантна бела вина</span></p>'),
    (r'<h2 class="category-title">Црвена вина</h2>',
     '<h2 class="category-title"><span data-i18n="wine-page.category.red.title">Црвена вина</span></h2>'),
    (r'<p class="category-description">Богата и комплексна црвена вина</p>',
     '<p class="category-description"><span data-i18n="wine-page.category.red.desc">Богата и комплексна црвена вина</span></p>'),
    (r'<h2 class="category-title">Розе вина</h2>',
     '<h2 class="category-title"><span data-i18n="wine-page.category.rose.title">Розе вина</span></h2>'),
    (r'<p class="category-description">Лагана и освежавајућа розе вина</p>',
     '<p class="category-description"><span data-i18n="wine-page.category.rose.desc">Лагана и освежавајућа розе вина</span></p>'),
    (r'<h2 class="category-title">Десертна & Специјална вина</h2>',
     '<h2 class="category-title"><span data-i18n="wine-page.category.dessert.title">Десертна & Специјална вина</span></h2>'),
    (r'<p class="category-description">Слатка и десертна вина за посебне тренутке</p>',
     '<p class="category-description"><span data-i18n="wine-page.category.dessert.desc">Слатка и десертна вина за посебне тренутке</span></p>'),
    (r'<h2 class="category-title">Вино на чашу</h2>',
     '<h2 class="category-title"><span data-i18n="wine-page.category.glass.title">Вино на чашу</span></h2>'),
    (r'<p class="category-description">Изабрана вина по чаши</p>',
     '<p class="category-description"><span data-i18n="wine-page.category.glass.desc">Изабрана вина по чаши</span></p>'),
]

# Add data-i18n to category buttons
button_patterns = [
    (r'<button class="category-btn active" data-category="all">\s*<i class="fas fa-wine-glass-alt"></i> Све\s*</button>',
     '<button class="category-btn active" data-category="all">\n                    <i class="fas fa-wine-glass-alt"></i> <span data-i18n="wine-page.filter.all">Све</span>\n                </button>'),
    (r'<button class="category-btn" data-category="champagne">\s*<i class="fas fa-champagne-glasses"></i> Шампањац & Пенушава\s*</button>',
     '<button class="category-btn" data-category="champagne">\n                    <i class="fas fa-champagne-glasses"></i> <span data-i18n="wine-page.filter.champagne">Шампањац & Пенушава</span>\n                </button>'),
    (r'<button class="category-btn" data-category="white">\s*<i class="fas fa-wine-glass"></i> Бела вина\s*</button>',
     '<button class="category-btn" data-category="white">\n                    <i class="fas fa-wine-glass"></i> <span data-i18n="wine-page.filter.white">Бела вина</span>\n                </button>'),
    (r'<button class="category-btn" data-category="red">\s*<i class="fas fa-wine-bottle"></i> Црвена вина\s*</button>',
     '<button class="category-btn" data-category="red">\n                    <i class="fas fa-wine-bottle"></i> <span data-i18n="wine-page.filter.red">Црвена вина</span>\n                </button>'),
    (r'<button class="category-btn" data-category="rose">\s*<i class="fas fa-glass-cheers"></i> Розе\s*</button>',
     '<button class="category-btn" data-category="rose">\n                    <i class="fas fa-glass-cheers"></i> <span data-i18n="wine-page.filter.rose">Розе</span>\n                </button>'),
    (r'<button class="category-btn" data-category="dessert">\s*<i class="fas fa-heart"></i> Десертна вина\s*</button>',
     '<button class="category-btn" data-category="dessert">\n                    <i class="fas fa-heart"></i> <span data-i18n="wine-page.filter.dessert">Десертна вина</span>\n                </button>'),
    (r'<button class="category-btn" data-category="glass">\s*<i class="fas fa-glass-martini-alt"></i> Вино на чашу\s*</button>',
     '<button class="category-btn" data-category="glass">\n                    <i class="fas fa-glass-martini-alt"></i> <span data-i18n="wine-page.filter.glass">Вино на чашу</span>\n                </button>'),
]

# Apply replacements
for pattern, replacement in patterns + button_patterns:
    content = re.sub(pattern, replacement, content)

# Write back
with open('wine.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Now add translations to i18n.js
print("✓ Додао data-i18n атрибуте за категорије вина")
print("✓ Треба сада додати преводе у i18n.js")

# Print translations for i18n.js
print("\n=== SR Translations ===")
for key, value in category_translations['sr'].items():
    print(f"        '{key}': '{value}',")

print("\n=== EN Translations ===")
for key, value in category_translations['en'].items():
    print(f"        '{key}': '{value}',")

print("\n=== RU Translations ===")
for key, value in category_translations['ru'].items():
    print(f"        '{key}': '{value}',")

# Filter button translations
filter_translations = {
    'sr': {
        'wine-page.filter.all': 'Све',
        'wine-page.filter.champagne': 'Шампањац & Пенушава',
        'wine-page.filter.white': 'Бела вина',
        'wine-page.filter.red': 'Црвена вина',
        'wine-page.filter.rose': 'Розе',
        'wine-page.filter.dessert': 'Десертна вина',
        'wine-page.filter.glass': 'Вино на чашу',
    },
    'en': {
        'wine-page.filter.all': 'All',
        'wine-page.filter.champagne': 'Champagne & Sparkling',
        'wine-page.filter.white': 'White Wines',
        'wine-page.filter.red': 'Red Wines',
        'wine-page.filter.rose': 'Rosé',
        'wine-page.filter.dessert': 'Dessert Wines',
        'wine-page.filter.glass': 'By the Glass',
    },
    'ru': {
        'wine-page.filter.all': 'Все',
        'wine-page.filter.champagne': 'Шампанское и игристые',
        'wine-page.filter.white': 'Белые вина',
        'wine-page.filter.red': 'Красные вина',
        'wine-page.filter.rose': 'Розе',
        'wine-page.filter.dessert': 'Десертные вина',
        'wine-page.filter.glass': 'По бокалам',
    }
}

print("\n=== Filter Button Translations ===")
print("\nSR:")
for key, value in filter_translations['sr'].items():
    print(f"        '{key}': '{value}',")
print("\nEN:")
for key, value in filter_translations['en'].items():
    print(f"        '{key}': '{value}',")
print("\nRU:")
for key, value in filter_translations['ru'].items():
    print(f"        '{key}': '{value}',")
