import re

with open('wine.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Info note
    ('                            <span>За групе веће од 10 особа обавезна резервација</span>',
     '                            <span data-i18n="footer.info.reservation">За групе веће од 10 особа обавезна резервација</span>'),
    
    # Badge 1 - Tradition
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;">40 година традиције</div>',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;" data-i18n="footer.badge.tradition">40 година традиције</div>'),
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;">Од 1985. године</div>\n                        </div>\n                    </div>\n                    <div style="display: flex; align-items: center; gap: 0.75rem;">\n                        <i class="fas fa-utensils"',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;" data-i18n="footer.badge.tradition.since">Од 1985. године</div>\n                        </div>\n                    </div>\n                    <div style="display: flex; align-items: center; gap: 0.75rem;">\n                        <i class="fas fa-utensils"'),
    
    # Badge 2 - Cuisine
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;">Аутентична кухиња</div>',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;" data-i18n="footer.badge.cuisine">Аутентична кухиња</div>'),
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;">Домаћи рецепти</div>\n                        </div>\n                    </div>\n                    <div style="display: flex; align-items: center; gap: 0.75rem;">\n                        <i class="fas fa-wine-bottle"',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;" data-i18n="footer.badge.cuisine.subtitle">Домаћи рецепти</div>\n                        </div>\n                    </div>\n                    <div style="display: flex; align-items: center; gap: 0.75rem;">\n                        <i class="fas fa-wine-bottle"'),
    
    # Badge 3 - Rakija
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;">31 врста ракије</div>',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;" data-i18n="footer.badge.rakija">31 врста ракије</div>'),
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;">Домаће производње</div>\n                        </div>\n                    </div>\n                    <div style="display: flex; align-items: center; gap: 0.75rem;">\n                        <i class="fas fa-music"',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;" data-i18n="footer.badge.rakija.subtitle">Домаће производње</div>\n                        </div>\n                    </div>\n                    <div style="display: flex; align-items: center; gap: 0.75rem;">\n                        <i class="fas fa-music"'),
    
    # Badge 4 - Music
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;">Жива музика</div>',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;" data-i18n="footer.badge.music">Жива музика</div>'),
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;">Петком и суботом</div>\n                        </div>\n                    </div>\n                    <div style="display: flex; align-items: center; gap: 0.75rem;">\n                        <i class="fas fa-parking"',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;" data-i18n="footer.badge.music.subtitle">Петком и суботом</div>\n                        </div>\n                    </div>\n                    <div style="display: flex; align-items: center; gap: 0.75rem;">\n                        <i class="fas fa-parking"'),
    
    # Badge 5 - Parking
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;">Бесплатан паркинг</div>',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 0.9rem; font-weight: 600; margin-bottom: 0.125rem;" data-i18n="footer.badge.parking">Бесплатан паркинг</div>'),
    ('                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;">За госте ресторана</div>\n                        </div>\n                    </div>\n                </div>\n            </div>',
     '                            <div style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.8rem;" data-i18n="footer.badge.parking.subtitle">За госте ресторана</div>\n                        </div>\n                    </div>\n                </div>\n            </div>'),
    
    # Copyright
    ('                <p style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.9375rem; margin: 0;">&copy; <span id="currentYear"></span> Ресторан Златар. Сва права задржана.</p>',
     '                <p style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.5); font-size: 0.9375rem; margin: 0;">&copy; <span id="currentYear"></span> <span data-i18n="footer.copyright">Ресторан Златар. Сва права задржана.</span></p>'),
    
    # Bottom links
    ('                    <a href="terms.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.875rem; text-decoration: none; transition: all 0.3s;">Услови коришћења</a>',
     '                    <a href="terms.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.875rem; text-decoration: none; transition: all 0.3s;" data-i18n="footer.terms">Услови коришћења</a>'),
    ('                    <a href="privacy.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.875rem; text-decoration: none; transition: all 0.3s;">Политика приватности</a>',
     '                    <a href="privacy.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.875rem; text-decoration: none; transition: all 0.3s;" data-i18n="footer.privacy">Политика приватности</a>'),
    ('                    <a href="sitemap.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.875rem; text-decoration: none; transition: all 0.3s;">Мапа сајта</a>',
     '                    <a href="sitemap.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.875rem; text-decoration: none; transition: all 0.3s;" data-i18n="footer.sitemap">Мапа сајта</a>'),
    ('                        <span style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.875rem;">Дизајн и израда</span>',
     '                        <span style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.875rem;" data-i18n="footer.design">Дизајн и израда</span>'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1

with open('wine.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Updated {count} additional footer elements in wine.html")

print("\n=== FOOTER BADGE & BOTTOM TRANSLATIONS ===")
print("\nSERBIAN:")
print("        'footer.info.reservation': 'За групе веће од 10 особа обавезна резервација',")
print("        'footer.badge.tradition': '40 година традиције',")
print("        'footer.badge.tradition.since': 'Од 1985. године',")
print("        'footer.badge.cuisine': 'Аутентична кухиња',")
print("        'footer.badge.cuisine.subtitle': 'Домаћи рецепти',")
print("        'footer.badge.rakija': '31 врста ракије',")
print("        'footer.badge.rakija.subtitle': 'Домаће производње',")
print("        'footer.badge.music': 'Жива музика',")
print("        'footer.badge.music.subtitle': 'Петком и суботом',")
print("        'footer.badge.parking': 'Бесплатан паркинг',")
print("        'footer.badge.parking.subtitle': 'За госте ресторана',")
print("        'footer.copyright': 'Ресторан Златар. Сва права задржана.',")
print("        'footer.terms': 'Услови коришћења',")
print("        'footer.privacy': 'Политика приватности',")
print("        'footer.sitemap': 'Мапа сајта',")
print("        'footer.design': 'Дизајн и израда',")

print("\nENGLISH:")
print("        'footer.info.reservation': 'Reservation required for groups over 10 people',")
print("        'footer.badge.tradition': '40 Years of Tradition',")
print("        'footer.badge.tradition.since': 'Since 1985',")
print("        'footer.badge.cuisine': 'Authentic Cuisine',")
print("        'footer.badge.cuisine.subtitle': 'Traditional Recipes',")
print("        'footer.badge.rakija': '31 Types of Rakija',")
print("        'footer.badge.rakija.subtitle': 'Homemade Production',")
print("        'footer.badge.music': 'Live Music',")
print("        'footer.badge.music.subtitle': 'Friday and Saturday',")
print("        'footer.badge.parking': 'Free Parking',")
print("        'footer.badge.parking.subtitle': 'For restaurant guests',")
print("        'footer.copyright': 'Restaurant Zlatar. All rights reserved.',")
print("        'footer.terms': 'Terms of Use',")
print("        'footer.privacy': 'Privacy Policy',")
print("        'footer.sitemap': 'Sitemap',")
print("        'footer.design': 'Design and Development',")

print("\nRUSSIAN:")
print("        'footer.info.reservation': 'Для групп более 10 человек обязательна резервация',")
print("        'footer.badge.tradition': '40 лет традиций',")
print("        'footer.badge.tradition.since': 'С 1985 года',")
print("        'footer.badge.cuisine': 'Подлинная кухня',")
print("        'footer.badge.cuisine.subtitle': 'Домашние рецепты',")
print("        'footer.badge.rakija': '31 вид ракии',")
print("        'footer.badge.rakija.subtitle': 'Домашнее производство',")
print("        'footer.badge.music': 'Живая музыка',")
print("        'footer.badge.music.subtitle': 'Пятница и суббота',")
print("        'footer.badge.parking': 'Бесплатная парковка',")
print("        'footer.badge.parking.subtitle': 'Для гостей ресторана',")
print("        'footer.copyright': 'Ресторан Златар. Все права защищены.',")
print("        'footer.terms': 'Условия использования',")
print("        'footer.privacy': 'Политика конфиденциальности',")
print("        'footer.sitemap': 'Карта сайта',")
print("        'footer.design': 'Дизайн и разработка',")
