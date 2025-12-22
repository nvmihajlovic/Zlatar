import re

with open('wine.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all country headers without data-i18n
countries_to_add = [
    ('Црна Гора', 'montenegro'),
    ('Хрватска', 'croatia'),
    ('Словенија', 'slovenia'),
]

count = 0
for country_name, country_key in countries_to_add:
    # Pattern: <h3>CountryName</h3>
    pattern = f'<h3>{country_name}</h3>'
    replacement = f'<h3><span data-i18n="wine-page.country.{country_key}">{country_name}</span></h3>'
    
    # Count occurrences
    occurrences = content.count(pattern)
    if occurrences > 0:
        content = content.replace(pattern, replacement)
        count += occurrences
        print(f"✓ Added data-i18n to {occurrences} instances of {country_name}")

with open('wine.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Total: Added data-i18n to {count} country headers")

print("\n=== NEW COUNTRY TRANSLATIONS NEEDED ===")
print("\nSERBIAN:")
print("        'wine-page.country.montenegro': 'Црна Гора',")
print("        'wine-page.country.croatia': 'Хрватска',")
print("        'wine-page.country.slovenia': 'Словенија',")

print("\nENGLISH:")
print("        'wine-page.country.montenegro': 'Montenegro',")
print("        'wine-page.country.croatia': 'Croatia',")
print("        'wine-page.country.slovenia': 'Slovenia',")

print("\nRUSSIAN:")
print("        'wine-page.country.montenegro': 'Черногория',")
print("        'wine-page.country.croatia': 'Хорватия',")
print("        'wine-page.country.slovenia': 'Словения',")
