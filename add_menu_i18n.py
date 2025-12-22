# -*- coding: utf-8 -*-
"""
Comprehensive script to add data-i18n attributes to all menu items in menu.html
"""
import re
import sys

def main():
    # Read the menu.html file
    with open('menu.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Map Serbian Cyrillic item names to their i18n keys (based on existing i18n.js)
    menu_items_map = {
        # Doručak
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
        
        # Hladna predjela
        'Златарска овчија пршута 100г': 'zlatarska-prsuta',
        'Mutton prosciutto from Zlatar': 'zlatarska-prsuta-desc',
        'Златиборска говеђа пршута 100г': 'zlatiborska-prsuta',
        'Beef prosciutto from Zlatibor': 'zlatiborska-prsuta-desc',
        'Ужичка свињска печеница 100г': 'uzicka-pecenica',
        'Dry cured pork tenderloin from Užice': 'uzicka-pecenica-desc',
        'Његушки пршут 100г': 'njeguski-prsut',
        'Dry cured ham from Njeguši': 'njeguski-prsut-desc',
        'Златарски сир пуномасни 150г': 'zlatarski-sir',
        'Full-fat cheese from Zlatar': 'zlatarski-sir-desc',
        'Козји сир пуномасни 100г': 'kozji-sir',
        'Full-fat goat cheese': 'kozji-sir-desc',
        'Паприка у павлаци 150г': 'paprika-u-pavlaci',
        'Pepper with cheese and sour cream': 'paprika-u-pavlaci-desc',
        'Едамац качкаваљ 100г': 'edamac-kackava',
        'Edam cheese': 'edamac-kackava-desc',
        'Пиротски качкаваљ 100г': 'pirotski-kackava',
        'Hard yellow cheese from Pirot': 'pirotski-kackava-desc',
        'Ужички кајмак млади 100г': 'uzicki-kajmak-mladi',
        'Heavy cow\'s milk cream from Užice': 'uzicki-kajmak-mladi-desc',
        'Ивањички кајмак стари 100г': 'ivanjicki-kajmak-stari',
        'Heavy cow\'s milk cream from Ivanjica': 'ivanjicki-kajmak-stari-desc',
        'Пребранац': 'prebranac',
        'Baked beans': 'prebranac-desc',
        'Пихтије': 'pihtije',
        'Татар бифтек 200г': 'tatar-biftek',
        
        # Topla predjela
        'Пита од хељде 250г': 'pita-od-heljde',
        'Проја са сиром 200г': 'proja-sa-sirom',
        'Грилловани козји сир 150г': 'grilovani-kozji-sir',
        'Печурке на жару 250г': 'pecurke-na-zaru',
        'Поховани качкаваљ 150г': 'pohovani-kackavalj',
        'Поховане паприке пуњене сиром': 'pohovane-paprike',
        'Поховане печурке 200г': 'pohovane-pecurke',
        'Пршута са јајима': 'prsuta-sa-jajima',
        'Сланина са јајима': 'slanina-sa-jajima',
        'Омлет': 'omlet',
        'са сиром, кајмаком, печуркама или пршутом': 'omlet-desc',
        'Кајгана (3 јаја)': 'kajgana',
        'Јаја на око (3 јаја)': 'jaja-na-oko',
        'Палента (за 2 особе)': 'palenta',
        'Уштипци - приганице': 'ustipci-priganice',
        'за 2 особе до 12h': 'ustipci-priganice-desc',
        
        # Kombinovana predjela
        'Предјело „Златар" (за 2 особе)': 'predjelo-zlatar',
        'говеђа пршута, свињска пршута, златарски сир, кајмак, проја, пита од хељде, пребранац': 'predjelo-zlatar-desc',
        'Тањир пршута „Златар" (за 2 особе)': 'tanjir-prsuta',
        'говеђа, свињска, овчија пршута, његушки пршут': 'tanjir-prsuta-desc',
        'Тањир сирева „Златар" (за 2 особе)': 'tanjir-sireva',
        'златарски сир, козји сир, козји сир у маслиновом уљу, кајмак, качкаваљ, трапист': 'tanjir-sireva-desc',
        'Тањир пршута и сирева (за 2 особе)': 'tanjir-prsuta-sireva',
        'говеђа, свињска пршута, његушки пршут, златарски сир, козји сир, качкаваљ': 'tanjir-prsuta-sireva-desc',
        
        # Supe i corbe
        'Говеђа супа са резанцима': 'goveda-supa',
        'Телећа рагу чорба': 'teleca-ragu',
        'Јагњећа српска чорба': 'jagneca-corba',
        'Чорба од печурака': 'corba-od-pecuraka',
        'Рибља чорба (постом)': 'riblja-corba',
        
        # Riba
        'Димљена пастрмка 300г': 'dimljena-pastrmka',
        'филети': 'dimljena-pastrmka-desc',
        'Смуђ на жару 300г': 'smudj-na-zaru',
        'Лигње на жару 300г': 'lignje-na-zaru',
        'Лигње поховане 200г': 'lignje-pohovane',
        
        # Pecenje
        'Шурена јаретина у млеку 250г': 'surena-jaretina',
        'Јагњетина испод сача 250г': 'jagnetina-ispod-saca',
        'Телетина испод сача 250г': 'teletina-ispod-saca',
        'Свињске коленице у купусу': 'svinjske-kolenice',
        'порција, сезонски': 'svinjske-kolenice-desc',
        
        # Specijaliteti
        'Златарска трпеза': 'zlatarska-trpeza',
        'ролована печурка, пуњена вешалица, пилећи, гурманска плескавица': 'zlatarska-trpeza-desc',
        'Златарска шницла': 'zlatarska-snicla',
        'панирани свињски филе пуњен кајмаком, пршутом, качкављем и печуркама': 'zlatarska-snicla-desc',
        'Пуњени пилећи ражњићи ролат': 'punjeni-pileci-raznjici',
        'кајмак, качкаваљ, пршута, сланина': 'punjeni-pileci-raznjici-desc',
        'Пуњени свињски ражњићи': 'punjeni-svinjski-raznjici',
        'кајмак, качкаваљ, пршута': 'punjeni-svinjski-raznjici-desc',
        'Пуњена бела вешалица у марамици': 'punjena-bela-vesalica',
        'Пуњени филе са печуркама': 'punjeni-file-sa-pecurkama',
        'кајмак, качкаваљ, пршута, печуркарски сос': 'punjeni-file-sa-pecurkama-desc',
        'Бризле на жару': 'brizle-na-zaru',
        'Мешани роштиљ „Златар"': 'mesani-rostilj-zlatar',
        'пуњена вешалица, роловане печурке, пилећи ражњић са сувим шљивама, гурманска плескавица': 'mesani-rostilj-zlatar-desc',
        'Роловане печурке са пилећим и сланином': 'rolovane-pecurke',
        'Пилећи ражњићи са сувим шљивама': 'pileci-raznjici-sa-sljivama',
        'Свињска реброцрца на кајмаку': 'svinjska-rebarca',
        'Јагњећи котлети на жару': 'jagneci-kotleti',
        
        # Rostilj
        'Бифтек на жару': 'biftek-na-zaru',
        'Мешано месо за 2 особе': 'mesano-meso-2',
        'Јагњећа џигерица на жару': 'jagneca-dzigerica-zar',
        'Јагњећа џигерица у марамици': 'jagneca-dzigerica-maramica',
        'Свињски филе на жару': 'svinjski-file-zar',
        'Пуњени свињски филе': 'punjeni-svinjski-file',
        'Свињски медаљони на жару': 'svinjski-medaljoni',
        'Бела вешалица (свињско месо са врата)': 'bela-vesalica',
        'Димљена вешалица': 'dimljena-vesalica',
        'Свињски ражњићи': 'svinjski-raznjici',
        'Ћевапчићи са луком': 'cevapcici-sa-lukom',
        'Плескавица са луком': 'pljeskavica-sa-lukom',
        'Ћевапчићи или плескавица на кајмаку': 'cevapcici-na-kajmaku',
        'Лесковачки ћевапи': 'leskovacki-cevapi',
        'Лесковачки уштипци': 'leskovacki-ustipci',
        'сланина, качкаваљ, бели лук, љута паприка': 'leskovacki-ustipci-desc',
        'Гурманска плескавица': 'gurmanska-pljeskavica',
        'љута по жељи': 'gurmanska-pljeskavica-desc',
        'Домаће кобасице димљене': 'domace-kobasice',
        'Мешани роштиљ': 'mesani-rostilj',
        'бела вешалица, пилеће бело, плескавица': 'mesani-rostilj-desc',
        'Пилеће бело на жару': 'pilece-belo',
        'Пилећи ражњићи у сланини': 'pileci-raznjici-u-slanici',
        'Пилећи батак на жару': 'pileci-batak',
        'Пилећа џигерица ролована у сланини': 'pileca-dzigerica',
        
        # Po porudzbini
        'Бифтек са сосом од бибера': 'biftek-sos-biber',
        'Медаљони на путеру': 'medaljoni-na-puteru',
        'Медаљони са печуркама': 'medaljoni-sa-pecurkama',
        'Медаљони са кајмаком': 'medaljoni-sa-kajmakom',
        'Ужички филе': 'uzicki-file',
        'бели лук и стари кајмак': 'uzicki-file-desc',
        'Шницла природна / париз / бечка': 'snicla',
        'Карађорђева шницла': 'karadjordeva-snicla',
        'свињски филе са кајмаком': 'karadjordeva-snicla-desc',
        'Лесковачка мућкалица': 'leskovacka-muckalica',
        'Похована пилетина „парисиен"': 'pohovana-piletina',
        'Пилећи штапићи у сусаму': 'pileci-stapici',
        'Пилећи медаљони у сосу од наранџе': 'pileci-medaljoni-narandza',
        'Пилећи медаљони у сосу од нане': 'pileci-medaljoni-nana',
        'Пилећи медаљони са кајмаком': 'pileci-medaljoni-kajmak',
        
        # Variva
        'Григовано поврће': 'grilovano-povrce',
        'Барено поврће': 'bareno-povrce',
        'Печени кромпир': 'peceni-krompir',
        'Печени кромпир са кајмаком': 'peceni-krompir-kajmak',
        'Помфрит': 'pomfrit',
        'Кромпир и блитва': 'krompir-i-blitva',
        'Подварак (сезонски)': 'podvarak',
        'Пребранац варово': 'prebranac-varivo',
        'Сарме (сезонски)': 'sarme',
        'Шкембићи': 'skembici',
        'Пребранац са кобасицом': 'prebranac-sa-kobasicom',
        'Пребранац са месом': 'prebranac-sa-mesom',
        'Говеђи гулаш': 'govedi-gulas',
        'Рибиц у кајмаку': 'ribic-u-kajmaku',
        'Чорбаст пасуљ': 'corbast-pasulj',
        'Кувано дневно': 'kuvano-dnevno',
        
        # Salate
        'Српска салата': 'srpska-salata',
        'лук, парадајз, краставац': 'srpska-salata-desc',
        'Шопска салата': 'sopska-salata',
        'лук, парадајз, краставац, златарски сир': 'sopska-salata-desc',
        'Моравска салата': 'moravska-salata',
        'печена паприка, парадајз, бели и црни лук': 'moravska-salata-desc',
        'Таратор салата': 'tarator-salata',
        'краставац, павлака, бели лук': 'tarator-salata-desc',
        'Грчка салата': 'grcka-salata',
        'лук, парадајз, паприка, краставац, козји сир': 'grcka-salata-desc',
        'Целер салата': 'celer-salata',
        'целер, јабука, орах, павлака': 'celer-salata-desc',
        'Башта салата': 'basta-salata',
        'парадајз, паприка, купус, краставац': 'basta-salata-desc',
        'Витаминска салата': 'vitaminska-salata',
        'шаргарепа, купус, целер, зелена салата': 'vitaminska-salata-desc',
        'Пролећна салата': 'prolecna-salata',
        'купус, зелена салата, ротквице, млади лук': 'prolecna-salata-desc',
        'Ајвар домаћи': 'ajvar-domaci',
        'Урнебес салата': 'urnebes-salata',
        'домаћи ајвар и златарски сир': 'urnebes-salata-desc',
        'Парадајз са сиром': 'paradajz-sa-sirom',
        'Мешана салата': 'mesana-salata',
        '3 врсте салате по сезони': 'mesana-salata-desc',
        'Печена паприка': 'pecena-paprika',
        'Парадајз': 'paradajz',
        'Краставац': 'krastavac',
        'Зелена салата': 'zelena-salata',
        'Сладак купус': 'sladak-kupус',
        'Ротквице': 'rotkvice',
        'Млади лук (веза)': 'mladi-luk',
        'Цвекла': 'cvekla',
        'Кисели купус': 'kiseli-kupus',
        'Кисели краставац': 'kiseli-krastavac',
        'Туршија': 'tursija',
        
        # Poslastice
        'Пита са сувим шљивама „Златар"': 'pita-sa-sljivama',
        'Сува пита са орасима': 'suva-pita-orasi',
        'Пита са јабукама': 'pita-sa-jabukama',
        'Пита са вишњама': 'pita-sa-visnjama',
        'Туфахија': 'tuhafija',
        'Орашница': 'orasnica',
        'Палачинке са орасима': 'palacinke-sa-orasima',
        'Палачинке са нутелом': 'palacinke-sa-nutelom',
        'Палачинке са џемом домаћим': 'palacinke-sa-dzemom',
        'кајсија или шљива': 'palacinke-sa-dzemom-desc',
        'Сладолед порција (4 кугле)': 'sladoled-porcija',
    }
    
    # Add data-i18n attributes to item names
    for serbian_text, i18n_key in menu_items_map.items():
        # Escape special regex characters in serbian_text
        escaped_text = re.escape(serbian_text)
        
        # For item-name
        pattern = rf'(<div class="item-name">){escaped_text}(</div>)'
        replacement = rf'\1<span data-i18n="menu-page.item.{i18n_key}">{serbian_text}</span>\2'
        content, count = re.subn(pattern, replacement, content)
        if count > 0:
            print(f"Replaced {count} occurrence(s) of item-name: {serbian_text}")
        
        # For item-description
        pattern = rf'(<div class="item-description">){escaped_text}(</div>)'
        replacement = rf'\1<span data-i18n="menu-page.item.{i18n_key}">{serbian_text}</span>\2'
        content, count = re.subn(pattern, replacement, content)
        if count > 0:
            print(f"Replaced {count} occurrence(s) of item-description: {serbian_text}")
    
    # Save the updated content
    with open('menu.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\nSuccessfully added data-i18n attributes to menu.html!")
    print("Total replacements made")

if __name__ == '__main__':
    main()
