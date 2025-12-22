import re

with open('wine.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find locations with city names (Србија, City or Италија, City)
# We need to wrap only the country name in data-i18n span

replacements = [
    # Serbia with cities
    ('Србија, Topola', '<span data-i18n="wine-page.country.serbia">Србија</span>, Topola'),
    ('Србија, Vršac', '<span data-i18n="wine-page.country.serbia">Србија</span>, Vršac'),
    ('Србија, Jagodina', '<span data-i18n="wine-page.country.serbia">Србија</span>, Jagodina'),
    ('Србија, Prokuplje', '<span data-i18n="wine-page.country.serbia">Србија</span>, Prokuplje'),
    
    # Italy with cities
    ('Италија, Abruzzo', '<span data-i18n="wine-page.country.italy">Италија</span>, Abruzzo'),
]

count = 0
for old, new in replacements:
    # Check if not already has data-i18n
    if old in content and 'data-i18n' not in content[content.find(old)-50:content.find(old)]:
        occurrences = content.count(old)
        content = content.replace(old, new)
        count += occurrences

with open('wine.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Added data-i18n to {count} country names with city locations")
print("\nThese country names in locations with cities now have translation support:")
print("- Србија, Topola → Serbia, Topola / Сербия, Topola")
print("- Србија, Vršac → Serbia, Vršac / Сербия, Vršac")
print("- Србија, Jagodina → Serbia, Jagodina / Сербия, Jagodina")
print("- Србија, Prokuplje → Serbia, Prokuplje / Сербия, Prokuplje")
print("- Италија, Abruzzo → Italy, Abruzzo / Италия, Abruzzo")
