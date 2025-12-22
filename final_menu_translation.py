#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete translation for menu.html - add ALL remaining data-i18n attributes
"""

import re
from datetime import datetime
import shutil
import os

MENU_FILE = r"c:\Users\WEB STUDIO LINK\OneDrive\Desktop\Restoran Zlatar Novi\menu.html"

def create_backup():
    backup_dir = r"c:\Users\WEB STUDIO LINK\OneDrive\Desktop\Restoran Zlatar Novi\backup_" + datetime.now().strftime("%Y-%m-%d_%H%M%S")
    os.makedirs(backup_dir, exist_ok=True)
    shutil.copy2(MENU_FILE, os.path.join(backup_dir, "menu.html"))
    print(f"✓ Backup: {backup_dir}")
    return backup_dir

def add_all_remaining_items(content):
    """Add data-i18n to ALL remaining menu items"""
    
    changes = 0
    
    # Complete mapping of ALL remaining items - exact text to i18n key
    mappings = [
        # Soups
        ('Рибља чорба (у време поста)', 'menu-page.item.riblja-corba'),
        
        # Fish
        ('Димљена пастрмка на жару 300г', 'menu-page.item.dimljena-pastrmka'),
        ('Смуђ на жару 300г', 'menu-page.item.smudj-na-zaru'),
        ('Лигње на жару 300г', 'menu-page.item.lignje-na-zaru'),
        ('Лигње поховане 200г', 'menu-page.item.lignje-pohovane'),
        
        # Roast
        ('Сурена јаретина у млеку 250г', 'menu-page.item.surena-jaretina'),
        ('Јагњетина испод сача 250г', 'menu-page.item.jagnetina-ispod-saca'),
        ('Телетина испод сача 250г', 'menu-page.item.teletina-ispod-saca'),
        ('Свињске коленице у купусу', 'menu-page.item.svinjske-kolenice'),
        
        # Specialties
        ('Златарска трпеза', 'menu-page.item.zlatarska-trpeza'),
        ('Златарска шницла', 'menu-page.item.zlatarska-snicla'),
        ('Пуњени роловани пилећи ражњићи', 'menu-page.item.punjeni-pileci-raznjici'),
        ('Пуњени свињски ражњићи', 'menu-page.item.punjeni-svinjski-raznjici'),
        ('Пуњена бела вешалица у марамици', 'menu-page.item.punjena-bela-vesalica'),
        ('Пуњени филе са печуркама', 'menu-page.item.punjeni-file-sa-pecurkama'),
        ('Бризле на жару', 'menu-page.item.brizle-na-zaru'),
        ('Мешани роштиљ „Златар"', 'menu-page.item.mesani-rostilj-zlatar'),
        ('Роловане печурке са пилетином и сланиницом', 'menu-page.item.rolovane-pecurke'),
        ('Пилећи ражњићи са сувим шљивама', 'menu-page.item.pileci-raznjici-sa-sljivama'),
        ('Свињска ребарца на кајмаку', 'menu-page.item.svinjska-rebarca'),
        ('Јагњећи котлети на жару', 'menu-page.item.jagneci-kotleti'),
        
        # Grill
        ('Бифтек на жару', 'menu-page.item.biftek-na-zaru'),
        ('Мешано месо за 2 особе', 'menu-page.item.mesano-meso-2'),
        ('Јагњећа џигерица на жару', 'menu-page.item.jagneca-dzigerica-zar'),
        ('Јагњећа џигерица у марамици', 'menu-page.item.jagneca-dzigerica-maramica'),
        ('Свињски филе на жару', 'menu-page.item.svinjski-file-zar'),
        ('Пуњени свињски филе', 'menu-page.item.punjeni-svinjski-file'),
        ('Свињски медаљони на жару', 'menu-page.item.svinjski-medaljoni'),
        ('Бела вешалица (лакс каре)', 'menu-page.item.bela-vesalica'),
        ('Димљена вешалица', 'menu-page.item.dimljena-vesalica'),
        ('Свињски ражњићи', 'menu-page.item.svinjski-raznjici'),
        ('Ћевапчићи са луком', 'menu-page.item.cevapcici-sa-lukom'),
        ('Плескавица са луком', 'menu-page.item.pljeskavica-sa-lukom'),
        ('Ћевапчићи или плескавица на кајмаку', 'menu-page.item.cevapcici-na-kajmaku'),
        ('Лесковачки ћевапи', 'menu-page.item.leskovacki-cevapi'),
        ('Лесковачки уштипци', 'menu-page.item.leskovacki-ustipci'),
        ('Гурманска плескавица', 'menu-page.item.gurmanska-pljeskavica'),
        ('Домаће димљене кобасице', 'menu-page.item.domace-kobasice'),
        ('Мешани роштиљ', 'menu-page.item.mesani-rostilj'),
        ('Пилеће бело месо на жару', 'menu-page.item.pilece-belo'),
        ('Пилећи ражњићи у сланиници', 'menu-page.item.pileci-raznjici-u-slanici'),
        ('Пилећи батак на жару', 'menu-page.item.pileci-batak'),
        ('Пилећа џигерица ролована у сланиници', 'menu-page.item.pileca-dzigerica'),
        
        # A la carte
        ('Бифтек у сосу од бибера', 'menu-page.item.biftek-sos-biber'),
        ('Медаљони на путеру', 'menu-page.item.medaljoni-na-puteru'),
        ('Медаљони са печуркама', 'menu-page.item.medaljoni-sa-pecurkama'),
        ('Медаљони са кајмаком', 'menu-page.item.medaljoni-sa-kajmakom'),
        ('Ужички филе', 'menu-page.item.uzicki-file'),
        ('Натур / Париска / Бечка шницла', 'menu-page.item.snicla'),
        ('Карађорђева шницла', 'menu-page.item.karadjordeva-snicla'),
        ('Лесковачка мућкалица', 'menu-page.item.leskovacka-muckalica'),
        ('Похована пилетина „паризијен"', 'menu-page.item.pohovana-piletina'),
        ('Пилећи штапићи у сусаму', 'menu-page.item.pileci-stapici'),
        ('Пилећи медаљони у сосу од наранџе', 'menu-page.item.pileci-medaljoni-narandza'),
        ('Пилећи медаљони у сосу од нане', 'menu-page.item.pileci-medaljoni-nana'),
        ('Пилећи медаљони са кајмаком', 'menu-page.item.pileci-medaljoni-kajmak'),
        
        # Vegetables
        ('Грилловано поврће', 'menu-page.item.grilovano-povrce'),
        ('Барено поврће', 'menu-page.item.bareno-povrce'),
        ('Печени кромпир', 'menu-page.item.peceni-krompir'),
        ('Печени кромпир са кајмаком', 'menu-page.item.peceni-krompir-kajmak'),
        ('Помфрит', 'menu-page.item.pomfrit'),
        ('Кромпир и блитва', 'menu-page.item.krompir-i-blitva'),
        ('Подварак (сезонски)', 'menu-page.item.podvarak'),
        ('Пребранац вариво', 'menu-page.item.prebranac-varivo'),
        ('Сарме, сармице (сезонске)', 'menu-page.item.sarme'),
        ('Шкембићи у сафту', 'menu-page.item.skembici'),
        ('Пребранац са кобасицом', 'menu-page.item.prebranac-sa-kobasicom'),
        ('Пребранац са месом', 'menu-page.item.prebranac-sa-mesom'),
        ('Говеђи гулаш', 'menu-page.item.govedi-gulas'),
        ('Рибић у кајмаку', 'menu-page.item.ribic-u-kajmaku'),
        ('Чорбаст пасуљ са месом', 'menu-page.item.corbast-pasulj'),
        ('Кувано дневно јело', 'menu-page.item.kuvano-dnevno'),
        
        # Salads
        ('Српска салата', 'menu-page.item.srpska-salata'),
        ('Шопска салата', 'menu-page.item.sopska-salata'),
        ('Моравска салата', 'menu-page.item.moravska-salata'),
        ('Таратор салата', 'menu-page.item.tarator-salata'),
        ('Грчка салата', 'menu-page.item.grcka-salata'),
        ('Целер салата', 'menu-page.item.celer-salata'),
        ('„Башта" салата', 'menu-page.item.basta-salata'),
        ('Витаминска салата', 'menu-page.item.vitaminska-salata'),
        ('Пролећна салата', 'menu-page.item.prolecna-salata'),
        ('Ајвар домаћи', 'menu-page.item.ajvar-domaci'),
        ('Урнебес салата', 'menu-page.item.urnebes-salata'),
        ('Парадајз са сиром', 'menu-page.item.paradajz-sa-sirom'),
        ('Мешана салата', 'menu-page.item.mesana-salata'),
        ('Печена паприка', 'menu-page.item.pecena-paprika'),
        ('Парадајз', 'menu-page.item.paradajz'),
        ('Краставац', 'menu-page.item.krastavac'),
        ('Зелена салата', 'menu-page.item.zelena-salata'),
        ('Сладак купус', 'menu-page.item.sladak-kupus'),
        ('Ротквице', 'menu-page.item.rotkvice'),
        ('Млади лук (кesa)', 'menu-page.item.mladi-luk'),
        ('Цвекла', 'menu-page.item.cvekla'),
        ('Кисели купус', 'menu-page.item.kiseli-kupus'),
        ('Кисели краставац', 'menu-page.item.kiseli-krastavac'),
        ('Туршија', 'menu-page.item.tursija'),
        
        # Desserts
        ('Пита са сувим шљивама „Златар"', 'menu-page.item.pita-sa-sljivama'),
        ('Сува пита са орасима', 'menu-page.item.suva-pita-orasi'),
        ('Пита са јабукама', 'menu-page.item.pita-sa-jabukama'),
        ('Пита са вишњама', 'menu-page.item.pita-sa-visnjama'),
        ('Тухафија', 'menu-page.item.tuhafija'),
        ('Орасница', 'menu-page.item.orasnica'),
        ('Палачинке са орасима', 'menu-page.item.palacinke-sa-orasima'),
        ('Палачинке са „нутелом"', 'menu-page.item.palacinke-sa-nutelom'),
        ('Палачинке са домаћим џемом', 'menu-page.item.palacinke-sa-dzemom'),
        ('Сладолед порција (4 кугле)', 'menu-page.item.sladoled-porcija'),
        
        # Rakije
        ('Шљива пожегача 10 год (45%, 0,03l)', 'menu-page.rakije.sljiva-pozegaca-10'),
        ('Дивља крушка (44%, 0,03l)', 'menu-page.rakije.divlja-kruska'),
        ('Кајсија (43%, 0,03l)', 'menu-page.rakije.kajsija'),
        ('Дуња (43%, 0,03l)', 'menu-page.rakije.dunja'),
        ('Јабука (42%, 0,03l)', 'menu-page.rakije.jabuka'),
        ('Дивља јабука (45%, 0,03l)', 'menu-page.rakije.divlja-jabuka'),
        ('Вишња (42%, 0,03l)', 'menu-page.rakije.visnja'),
        ('Трешња (42%, 0,03l)', 'menu-page.rakije.tresnja'),
        ('Дрењина (43%, 0,03l)', 'menu-page.rakije.drenjina'),
        ('Боровница (43%, 0,03l)', 'menu-page.rakije.borovnica'),
        ('Јагода (42%, 0,03l)', 'menu-page.rakije.jagoda'),
        ('Малина (38%, 0,03l)', 'menu-page.rakije.malina'),
        ('Купина (42%, 0,03l)', 'menu-page.rakije.kupina'),
        ('Диња (42%, 0,03l)', 'menu-page.rakije.dinja'),
        ('Лоза Тамјаника (45%, 0,03l)', 'menu-page.rakije.loza-tamjanika'),
        ('Банана (42%, 0,03l)', 'menu-page.rakije.banana'),
        
        # Rakije Barrique
        ('Шљива пожегача barrique 15 год (45%, 0,03l)', 'menu-page.rakije.sljiva-barrique-15'),
        ('Кајсија barrique (43%, 0,03l)', 'menu-page.rakije.kajsija-barrique'),
        ('Дивља крушка barrique (43%, 0,03l)', 'menu-page.rakije.divlja-kruska-barrique'),
        ('Дуња barrique (43%, 0,03l)', 'menu-page.rakije.dunja-barrique'),
        ('Дивља јабука barrique (45%, 0,03l)', 'menu-page.rakije.divlja-jabuka-barrique'),
        
        # Special Rakije
        ('Медовача (40%, 0,33l)', 'menu-page.rakije.medovaca'),
        ('Медовина (38%, 0,03l)', 'menu-page.rakije.medovina'),
        ('Ораховача (38%, 0,03l)', 'menu-page.rakije.orahovaca'),
        ('Кантарионка (42%, 0,03l)', 'menu-page.rakije.kantarionka'),
        ('Клековача (43%, 0,03l)', 'menu-page.rakije.klekovaca'),
        ('ПоТенцијал (40%, 0,03l)', 'menu-page.rakije.potencijal'),
        ('Линцура (50%, 0,03l)', 'menu-page.rakije.lincura'),
        ('Нановача (42%, 0,03l)', 'menu-page.rakije.nanovaca'),
        ('Аронија (42%, 0,03l)', 'menu-page.rakije.aronija'),
        ('Сува шљива (40%, 0,03l)', 'menu-page.rakije.suva-sljiva'),
        ('Ликер од суве шљиве (25%, 0,03l)', 'menu-page.rakije.liker-suve-sljive'),
    ]
    
    print(f"\nДодајем data-i18n на {len(mappings)} јела...\n")
    
    for text, i18n_key in mappings:
        # Wrap plain text in span with data-i18n
        old_pattern = f'<div class="item-name">{text}</div>'
        new_pattern = f'<div class="item-name"><span data-i18n="{i18n_key}">{text}</span></div>'
        
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            changes += 1
            print(f"  ✓ {text[:50]}...")
    
    print(f"\n✓ Укупно додато: {changes} data-i18n атрибута")
    return content

def main():
    print("=" * 60)
    print("КОМПЛЕТАН ПРЕВОД MENU.HTML")
    print("=" * 60 + "\n")
    
    backup_dir = create_backup()
    
    with open(MENU_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    
    # Add all remaining items
    content = add_all_remaining_items(content)
    
    with open(MENU_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_len = len(content)
    
    print(f"\n{'=' * 60}")
    print(f"✓ ЗАВРШЕНО!")
    print(f"Величина фајла: {original_len:,} → {new_len:,} chars")
    print(f"Backup: {backup_dir}")
    print(f"{'=' * 60}\n")

if __name__ == "__main__":
    main()
