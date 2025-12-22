# -*- coding: utf-8 -*-
"""
Script to add data-i18n attributes to all menu items in menu.html
"""

import re

# Read the menu.html file
with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define mapping for each item (Serbian name -> i18n key)
menu_items = {
    # Roštilj (Grill)
    'Бифтек на жару': 'biftek-na-zaru',
    'Мешано месо за 2 особе': 'mesano-meso-2',
    'Јагњећа џигерица на жару': 'jagneca-dzigerica-zar',
    'Јагњећа џигерица у марамици': 'jagneca-dzigerica-maramica',
    'Свињски филе на жару': 'svinjski-file-zar',
    'Пуњени свињски филе': 'punjeni-svinjski-file',
    'Свињски медаљони на жару': 'svinjski-medaljoni',
    'Бела вешалица \\(лакс каре\\)': 'bela-vesalica',
    'Димљена вешалица': 'dimljena-vesalica',
    'Свињски ражњићи': 'svinjski-raznjici',
    'Ћевапчићи са луком': 'cevapcici-sa-lukom',
    'Плескавица са луком': 'pljeskavica-sa-lukom',
    'Ћевапчићи или плескавица на кајмаку': 'cevapcici-na-kajmaku',
    'Лесковачки ћевапи': 'leskovacki-cevapi',
    'Лесковачки уштипци': 'leskovacki-ustipci',
    'Гурманска плескавица': 'gurmanska-pljeskavica',
    'Домаће димљене кобасице': 'domace-kobasice',
    'Мешани роштиљ': 'mesani-rostilj',
    'Пилеће бело на жару': 'pilece-belo',
    'Пилећи ражњићи у сланиници': 'pileci-raznjici-u-slanici',
    'Пилећи батак на жару': 'pileci-batak',
    'Пилећа џигерица ролована у сланиници': 'pileca-dzigerica',
    
    # Po porudžbini (À la carte)
    'Бифтек у сосу од бибера': 'biftek-sos-biber',
    'Медаљони на путеру': 'medaljoni-na-puteru',
    'Медаљони са печуркама': 'medaljoni-sa-pecurkama',
    'Медаљони са кајмаком': 'medaljoni-sa-kajmakom',
    'Ужички филе': 'uzicki-file',
    'Натур / Париска / Бечка шницла': 'snicla',
    'Карађорђева шницла': 'karadjordeva-snicla',
    'Лесковачка мућкалица': 'leskovacka-muckalica',
    'Похована пилетина „паризијен"': 'pohovana-piletina',
    'Пилећи штапићи у сусаму': 'pileci-stapici',
    'Пилећи медаљони у сосу од наранџе': 'pileci-medaljoni-narandza',
    'Пилећи медаљони у сосу од нане': 'pileci-medaljoni-nana',
    'Пилећи медаљони са кајмаком': 'pileci-medaljoni-kajmak',
    
    # Variva (Vegetables)
    'Грилловано поврће': 'grilovano-povrce',
    'Барено поврће': 'bareno-povrce',
    'Печени кромпир': 'peceni-krompir',
    'Печени кромпир са кајмаком': 'peceni-krompir-kajmak',
    'Помфрит': 'pomfrit',
    'Кромпир и блитва': 'krompir-i-blitva',
    'Подварак \\(сезонски\\)': 'podvarak',
    'Пребранац вариво': 'prebranac-varivo',
    'Сарме, сармице \\(сезонске\\)': 'sarme',
    'Шкембићи у сафту': 'skembici',
    'Пребранац са кобасицом': 'prebranac-sa-kobasicom',
    'Пребранац са месом': 'prebranac-sa-mesom',
    'Говеђи гулаш': 'govedi-gulas',
    'Рибић у кајмаку': 'ribic-u-kajmaku',
    'Чорбаст пасуљ са месом': 'corbast-pasulj',
    'Кувано дневно јело': 'kuvano-dnevno',
    
    # Salate (Salads)
    'Српска салата': 'srpska-salata',
    'Шопска салата': 'sopska-salata',
    'Моравска салата': 'moravska-salata',
    'Таратор салата': 'tarator-salata',
    'Грчка салата': 'grcka-salata',
    'Целер салата': 'celer-salata',
    '„Башта" салата': 'basta-salata',
    'Витаминска салата': 'vitaminska-salata',
    'Пролећна салата': 'prolecna-salata',
    'Ајвар домаћи': 'ajvar-domaci',
    'Урнебес салата': 'urnebes-salata',
    'Парадајз са сиром': 'paradajz-sa-sirom',
    'Мешана салата': 'mesana-salata',
    'Печена паприка': 'pecena-paprika',
    'Парадајз': 'paradajz',
    'Краставац': 'krastavac',
    'Зелена салата': 'zelena-salata',
    'Сладак купус': 'sladak-kupus',
    'Ротквице': 'rotkvice',
    'Млади лук \\(веза\\)': 'mladi-luk',
    'Цвекла': 'cvekla',
    'Кисели купус': 'kiseli-kupus',
    'Кисели краставац': 'kiseli-krastavac',
    'Туршија': 'tursija',
    
    # Poslastice (Desserts)
    'Пита са сувим шљивама „Златар"': 'pita-sa-sljivama',
    'Сува пита са орасима': 'suva-pita-orasi',
    'Пита са јабукама': 'pita-sa-jabukama',
    'Пита са вишњама': 'pita-sa-visnjama',
    'Тухафија': 'tuhafija',
    'Орасница': 'orasnica',
    'Палачинке са орасима': 'palacinke-sa-orasima',
    'Палачинке са „нутелом"': 'palacinke-sa-nutelom',
    'Палачинке са домаћим џемом': 'palacinke-sa-dzemom',
    'Сладолед порција \\(4 кугле\\)': 'sladoled-porcija',
}

# Descriptions mapping
descriptions = {
    'сланина, качкаваљ, бели лук, љута паприка': 'leskovacki-ustipci-desc',
    'љута по жељи': 'gurmanska-pljeskavica-desc',
    'бела вешалица, пилеће бело, плескавица': 'mesani-rostilj-desc',
    'бели лук и стари кајмак': 'uzicki-file-desc',
    'свињски филе са кајмаком': 'karadjordeva-snicla-desc',
    'лук, парадајз, краставац': 'srpska-salata-desc',
    'лук, парадајз, краставац, златарски сир': 'sopska-salata-desc',
    'печена паприка, парадајз, црни и бели лук': 'moravska-salata-desc',
    'краставац, павлака, бели лук': 'tarator-salata-desc',
    'лук, парадајз, паприка, краставац, козји сир': 'grcka-salata-desc',
    'целер, јабука, орах, павлака': 'celer-salata-desc',
    'парадајз, паприка, купус, краставац': 'basta-salata-desc',
    'шаргарепа, купус, целер, зелена салата': 'vitaminska-salata-desc',
    'купус, зелена салата, ротквице, млади лук': 'prolecna-salata-desc',
    'домаћи ајвар и златарски сир': 'urnebes-salata-desc',
    '3 врсте сезонске салате': 'mesana-salata-desc',
    'од кајсија или шљива': 'palacinke-sa-dzemom-desc',
}

# Add data-i18n to item names
for serbian_name, key in menu_items.items():
    # Pattern to match: <div class="item-name">Serbian Name</div>
    pattern = f'<div class="item-name">({serbian_name})</div>'
    replacement = f'<div class="item-name" data-i18n="menu-page.item.{key}">\\1</div>'
    content = re.sub(pattern, replacement, content)

# Add data-i18n to descriptions
for serbian_desc, key in descriptions.items():
    pattern = f'<div class="item-description">({re.escape(serbian_desc)})</div>'
    replacement = f'<div class="item-description" data-i18n="menu-page.item.{key}">\\1</div>'
    content = re.sub(pattern, replacement, content)

# Write back to file
with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Successfully added data-i18n attributes to all menu items!")
print(f"   Processed {len(menu_items)} item names")
print(f"   Processed {len(descriptions)} descriptions")
