# -*- coding: utf-8 -*-
"""
Script to add data-i18n attributes to menu.html
"""
import re

# Read the file
with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Normalizacija za slugifikaciju
def slugify(text):
    """Convert text to slug format for i18n keys"""
    import unicodedata
    # Ukloni dijaritike
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    
    # Donja slova i zameni razmake sa -
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.strip('-')
    
    # Replace serbian letters with ascii
    replacements = {
        'č': 'c', 'ć': 'c', 'đ': 'd', 'š': 's', 'ž': 'z',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'dj', 'е': 'e', 'ж': 'z', 'з': 'z',
        'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj', 'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'ћ': 'c', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
        'ч': 'c', 'џ': 'dz', 'ш': 's'
    }
    
    for sr, en in replacements.items():
        text = text.replace(sr, en)
    
    return text

# Mappings from Serbian text to i18n keys
item_mappings = {
    'Комплет лепиња': 'komplet-lepinja',
    'кајмак, јаја, претоп, кисело млеко': 'komplet-lepinja-desc',
    'Уштипци': 'ustipci',
    'са сиром / џемом / нутелом': 'ustipci-desc',
    'Пуњене прженице': 'punjene-przenice',
    'тост, пршута, качкаваљ, јаје': 'punjene-przenice-desc',
    'Доручак 1': 'dorucak1',
    'јаја на око са кобасицом, урнебес, сомун': 'dorucak1-desc',
    'Доручак 2': 'dorucak2',
    'сланина са јајима, урнебес, сомун': 'dorucak2-desc',
    'Доручак 3': 'dorucak3',
    'проја, пршута, урнебес, кисело млеко': 'dorucak3-desc',
    'Доручак 4': 'dorucak4',
    'кувана јаја, сир, пршута, урнебес, сомун': 'dorucak4-desc',
    'Доручак 5': 'dorucak5',
    'пита од хељде, пршута, кисело млеко': 'dorucak5-desc',
}

# Add data-i18n to category titles
content = re.sub(
    r'<h2 class="category-title"><i[^>]*></i>Доручак <span class="highlight">\(до 12h\)</span></h2>',
    r'<h2 class="category-title"><i class="fas fa-coffee" style="margin-right: 0.5rem; color: #D4AF37;"></i><span data-i18n="menu-page.breakfast.title">Доручак</span> <span class="highlight" data-i18n="menu-page.breakfast.time">(до 12h)</span></h2>',
    content
)

# Add data-i18n to item names and descriptions
# Pattern to find menu items
item_pattern = r'<div class="item-name">([^<]+)</div>'
desc_pattern = r'<div class="item-description">([^<]+)</div>'

def add_i18n_to_item(match):
    item_name = match.group(1)
    slug = item_mappings.get(item_name, slugify(item_name))
    return f'<div class="item-name" data-i18n="menu-page.item.{slug}">{item_name}</div>'

def add_i18n_to_desc(match):
    desc_text = match.group(1)
    # Try to find base item name for this description
    slug = item_mappings.get(desc_text, slugify(desc_text[:30]))  # Limit to 30 chars for slug
    return f'<div class="item-description" data-i18n="menu-page.item.{slug}">{desc_text}</div>'

# Apply replacements
content = re.sub(item_pattern, add_i18n_to_item, content)
# Don't add to descriptions for now - they're complex

# Write back
with open('menu_updated.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated menu.html saved as menu_updated.html")
print("Please review the changes before replacing the original file.")
