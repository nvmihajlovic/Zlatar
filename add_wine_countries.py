import re

# Read wine.html
with open('wine.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Country names to translate
countries = [
    ('Србија', 'Serbia', 'Сербия', 'serbia'),
    ('Италија', 'Italy', 'Италия', 'italy'),
    ('Француска', 'France', 'Франция', 'france'),
    ('Аустрија', 'Austria', 'Австрия', 'austria'),
    ('Аргентина', 'Argentina', 'Аргентина', 'argentina'),
]

count = 0

# Process each country
for sr, en, ru, key in countries:
    # Pattern 1: Wine detail locations
    pattern1 = f'<span class="wine-detail"><i class="fas fa-map-marker-alt"></i> {sr}</span>'
    replacement1 = f'<span class="wine-detail"><i class="fas fa-map-marker-alt"></i> <span data-i18n="wine-page.country.{key}">{sr}</span></span>'
    
    # Pattern 2: Winery locations
    pattern2 = f'<i class="fas fa-map-marker-alt"></i>\n                                <span>{sr}</span>'
    replacement2 = f'<i class="fas fa-map-marker-alt"></i>\n                                <span data-i18n="wine-page.country.{key}">{sr}</span>'
    
    # Pattern 3: Country headers
    pattern3 = f'<h3>{sr}</h3>'
    replacement3 = f'<h3><span data-i18n="wine-page.country.{key}">{sr}</span></h3>'
    
    # Replace if not already has data-i18n
    before_len = len(content)
    content = content.replace(pattern1, replacement1)
    content = content.replace(pattern2, replacement2)
    content = content.replace(pattern3, replacement3)
    after_len = len(content)
    
    if after_len > before_len:
        count += 1

# Write back
with open('wine.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Processed wine.html for country translations")

# Generate translations for i18n.js
print("\n=== SERBIAN ===")
for sr, en, ru, key in countries:
    print(f"        'wine-page.country.{key}': '{sr}',")

print("\n=== ENGLISH ===")
for sr, en, ru, key in countries:
    print(f"        'wine-page.country.{key}': '{en}',")

print("\n=== RUSSIAN ===")
for sr, en, ru, key in countries:
    print(f"        'wine-page.country.{key}': '{ru}',")

# Footer translations
print("\n\n=== ADDITIONAL WINE PAGE TRANSLATIONS ===")
print("\nSERBIAN:")
print("        'wine-page.breadcrumb.current': 'Винска карта',")
print("        'wine-page.download': 'Преузми винску карту (PDF)',")

print("\nENGLISH:")
print("        'wine-page.breadcrumb.current': 'Wine List',")
print("        'wine-page.download': 'Download Wine List (PDF)',")

print("\nRUSSIAN:")
print("        'wine-page.breadcrumb.current': 'Винная карта',")
print("        'wine-page.download': 'Скачать винную карту (PDF)',")
