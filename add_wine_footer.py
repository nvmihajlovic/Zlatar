import re

with open('wine.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Footer description
    ('                        Етно ресторан у срцу Београда. 40 година традиције, аутентични укуси и незаборавна атмосфера.\n',
     '                        <span data-i18n="footer.desc">Етно ресторан у срцу Београда. 40 година традиције, аутентични укуси и незаборавна атмосфера.</span>\n'),
    
    # Address
    ('                            <span style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.8); font-size: 1rem; line-height: 1.6;">Прерадовићева 9а<br>Београд, Србија</span>',
     '                            <span style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.8); font-size: 1rem; line-height: 1.6;" data-i18n="footer.address">Прерадовићева 9а<br>Београд, Србија</span>'),
    
    # Working hours title
    ('                    <h4 style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 1.125rem; font-weight: 600; margin-bottom: 1.5rem; letter-spacing: 0.02em; padding-bottom: 0.75rem; border-bottom: 2px solid transparent; border-image: linear-gradient(90deg, #D4AF37 0%, rgba(212,175,55,0.3) 70%, transparent 100%) 1; position: relative;">Радно време</h4>',
     '                    <h4 style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 1.125rem; font-weight: 600; margin-bottom: 1.5rem; letter-spacing: 0.02em; padding-bottom: 0.75rem; border-bottom: 2px solid transparent; border-image: linear-gradient(90deg, #D4AF37 0%, rgba(212,175,55,0.3) 70%, transparent 100%) 1; position: relative;" data-i18n="footer.working-hours">Радно време</h4>'),
    
    # Days
    ('                            <span style="white-space: nowrap;">Пон-Пет</span>',
     '                            <span style="white-space: nowrap;" data-i18n="footer.days.mon-fri">Пон-Пет</span>'),
    ('                            <span>Субота</span>',
     '                            <span data-i18n="footer.days.saturday">Субота</span>'),
    ('                            <span>Недеља</span>',
     '                            <span data-i18n="footer.days.sunday">Недеља</span>'),
    
    # Navigation title
    ('                    <h4 style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 1.125rem; font-weight: 600; margin-bottom: 1.5rem; letter-spacing: 0.02em; padding-bottom: 0.75rem; border-bottom: 2px solid transparent; border-image: linear-gradient(90deg, #D4AF37 0%, rgba(212,175,55,0.3) 70%, transparent 100%) 1; position: relative;">Навигација</h4>',
     '                    <h4 style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 1.125rem; font-weight: 600; margin-bottom: 1.5rem; letter-spacing: 0.02em; padding-bottom: 0.75rem; border-bottom: 2px solid transparent; border-image: linear-gradient(90deg, #D4AF37 0%, rgba(212,175,55,0.3) 70%, transparent 100%) 1; position: relative;" data-i18n="footer.navigation">Навигација</h4>'),
    
    # Navigation links
    ('                        <li><a href="about.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-info-circle" style="color: #D4AF37; font-size: 0.95rem;"></i>О нама</a></li>',
     '                        <li><a href="about.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-info-circle" style="color: #D4AF37; font-size: 0.95rem;"></i><span data-i18n="footer.link.about">О нама</span></a></li>'),
    
    ('                        <li><a href="menu.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-utensils" style="color: #D4AF37; font-size: 0.95rem;"></i>Јеловник</a></li>',
     '                        <li><a href="menu.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-utensils" style="color: #D4AF37; font-size: 0.95rem;"></i><span data-i18n="footer.link.menu">Јеловник</span></a></li>'),
    
    ('                        <li><a href="wine.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-wine-glass-alt" style="color: #D4AF37; font-size: 0.95rem;"></i>Винска карта</a></li>',
     '                        <li><a href="wine.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-wine-glass-alt" style="color: #D4AF37; font-size: 0.95rem;"></i><span data-i18n="footer.link.wine">Винска карта</span></a></li>'),
    
    ('                        <li><a href="gallery.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-images" style="color: #D4AF37; font-size: 0.95rem;"></i>Галерија</a></li>',
     '                        <li><a href="gallery.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-images" style="color: #D4AF37; font-size: 0.95rem;"></i><span data-i18n="footer.link.gallery">Галерија</span></a></li>'),
    
    ('                        <li><a href="contact.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-phone" style="color: #D4AF37; font-size: 0.95rem;"></i>Контакт</a></li>',
     '                        <li><a href="contact.html" style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-flex; align-items: center; gap: 0.75rem;"><i class="fas fa-phone" style="color: #D4AF37; font-size: 0.95rem;"></i><span data-i18n="footer.link.contact">Контакт</span></a></li>'),
    
    # Newsletter title
    ('                    <h4 style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 1.125rem; font-weight: 600; margin-bottom: 1rem; letter-spacing: 0.02em; padding-bottom: 0.75rem; border-bottom: 2px solid transparent; border-image: linear-gradient(90deg, #D4AF37 0%, rgba(212,175,55,0.3) 70%, transparent 100%) 1; position: relative;">Newsletter</h4>',
     '                    <h4 style="font-family: \'Montserrat\', sans-serif; color: #D4AF37; font-size: 1.125rem; font-weight: 600; margin-bottom: 1rem; letter-spacing: 0.02em; padding-bottom: 0.75rem; border-bottom: 2px solid transparent; border-image: linear-gradient(90deg, #D4AF37 0%, rgba(212,175,55,0.3) 70%, transparent 100%) 1; position: relative;" data-i18n="footer.newsletter">Newsletter</h4>'),
    
    ('                    <p style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 0.9375rem; margin-bottom: 1.25rem;">Пријавите се за специјалне понуде</p>',
     '                    <p style="font-family: \'Montserrat\', sans-serif; color: rgba(255,255,255,0.7); font-size: 0.9375rem; margin-bottom: 1.25rem;" data-i18n="footer.newsletter.text">Пријавите се за специјалне понуде</p>'),
    
    ('                        <input type="email" placeholder="Ваш email" class="newsletter-input"',
     '                        <input type="email" data-i18n-placeholder="footer.newsletter.placeholder" placeholder="Ваш email" class="newsletter-input"'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1

with open('wine.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✓ Updated {count} footer elements in wine.html")

print("\n=== ADDITIONAL FOOTER TRANSLATIONS ===")
print("\nSERBIAN:")
print("        'footer.desc': 'Етно ресторан у срцу Београда. 40 година традиције, аутентични укуси и незаборавна атмосфера.',")
print("        'footer.address': 'Прерадовићева 9а<br>Београд, Србија',")
print("        'footer.working-hours': 'Радно време',")
print("        'footer.days.mon-fri': 'Пон-Пет',")
print("        'footer.days.saturday': 'Субота',")
print("        'footer.days.sunday': 'Недеља',")
print("        'footer.navigation': 'Навигација',")
print("        'footer.link.about': 'О нама',")
print("        'footer.link.menu': 'Јеловник',")
print("        'footer.link.wine': 'Винска карта',")
print("        'footer.link.gallery': 'Галерија',")
print("        'footer.link.contact': 'Контакт',")
print("        'footer.newsletter': 'Newsletter',")
print("        'footer.newsletter.text': 'Пријавите се за специјалне понуде',")
print("        'footer.newsletter.placeholder': 'Ваш email',")

print("\nENGLISH:")
print("        'footer.desc': 'Ethno restaurant in the heart of Belgrade. 40 years of tradition, authentic flavors and unforgettable atmosphere.',")
print("        'footer.address': 'Preradovićeva 9a<br>Belgrade, Serbia',")
print("        'footer.working-hours': 'Working Hours',")
print("        'footer.days.mon-fri': 'Mon-Fri',")
print("        'footer.days.saturday': 'Saturday',")
print("        'footer.days.sunday': 'Sunday',")
print("        'footer.navigation': 'Navigation',")
print("        'footer.link.about': 'About Us',")
print("        'footer.link.menu': 'Menu',")
print("        'footer.link.wine': 'Wine List',")
print("        'footer.link.gallery': 'Gallery',")
print("        'footer.link.contact': 'Contact',")
print("        'footer.newsletter': 'Newsletter',")
print("        'footer.newsletter.text': 'Subscribe for special offers',")
print("        'footer.newsletter.placeholder': 'Your email',")

print("\nRUSSIAN:")
print("        'footer.desc': 'Этно-ресторан в центре Белграда. 40 лет традиций, подлинные вкусы и незабываемая атмосфера.',")
print("        'footer.address': 'Прерадовичева 9а<br>Белград, Сербия',")
print("        'footer.working-hours': 'Режим работы',")
print("        'footer.days.mon-fri': 'Пн-Пт',")
print("        'footer.days.saturday': 'Суббота',")
print("        'footer.days.sunday': 'Воскресенье',")
print("        'footer.navigation': 'Навигация',")
print("        'footer.link.about': 'О нас',")
print("        'footer.link.menu': 'Меню',")
print("        'footer.link.wine': 'Винная карта',")
print("        'footer.link.gallery': 'Галерея',")
print("        'footer.link.contact': 'Контакт',")
print("        'footer.newsletter': 'Рассылка',")
print("        'footer.newsletter.text': 'Подпишитесь на специальные предложения',")
print("        'footer.newsletter.placeholder': 'Ваш email',")
