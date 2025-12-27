"""
Додаје EmailJS SDK и email-service.js на све HTML странице
"""

import os
import re

# HTML странице где треба додати EmailJS
html_files = [
    'about.html',
    'menu.html', 
    'wine.html',
    'gallery.html',
    'blog.html',
    'blog-post-1.html',
    'blog-post-2.html',
    'blog-post-3.html',
    'blog-post-4.html',
    'blog-post-5.html',
    'blog-post-6.html',
    'blog-post-7.html',
    'blog-post-8.html',
    'blog-post-9.html',
    'blog-post-10.html',
    'blog-post-11.html',
    'blog-post-12.html',
    'privacy.html',
    'terms.html',
    'sitemap.html'
]

emailjs_scripts = '''
    <!-- EmailJS SDK -->
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
    <script src="js/email-service.js"></script>'''

def add_emailjs_to_file(filepath):
    """Додаје EmailJS скрипте пре затварајућег </body> тага"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Провера да ли већ има EmailJS
        if 'emailjs/browser' in content or 'email-service.js' in content:
            print(f"✓ {filepath} - већ има EmailJS")
            return
        
        # Додај пре </body>
        if '</body>' in content:
            content = content.replace('</body>', f'{emailjs_scripts}\n</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ {filepath} - додат EmailJS SDK")
        else:
            print(f"✗ {filepath} - нема </body> таг")
            
    except Exception as e:
        print(f"✗ {filepath} - грешка: {e}")

def update_reservation_form_handlers():
    """Ажурира reservation form handlers са EmailJS интеграцијом"""
    
    files_with_reservation = [
        'about.html',
        'menu.html', 
        'wine.html',
        'gallery.html',
        'blog.html',
        'privacy.html',
        'terms.html',
        'sitemap.html'
    ]
    
    old_handler = """reservationForm.addEventListener('submit', (e) => {
                e.preventDefault();
                
                const formData = {
                    name: document.getElementById('resName').value,
                    phone: document.getElementById('resPhone').value,
                    date: document.getElementById('resDate').value,
                    time: document.getElementById('resTime').value,
                    guests: document.getElementById('resGuests').value,
                    note: document.getElementById('resNote').value
                };
                
                // Here you would typically send data to server
                console.log('Reservation data:', formData);
                
                // Show success message
                alert('Хвала! Ваша резервација је послата. Контактираћемо вас ускоро за потврду.');
                
                // Close modal and reset form
                closeModal();
                reservationForm.reset();
            });"""
    
    new_handler = """reservationForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                
                const formData = {
                    name: document.getElementById('resName').value,
                    email: document.getElementById('resEmail')?.value || '',
                    phone: document.getElementById('resPhone').value,
                    date: document.getElementById('resDate').value,
                    time: document.getElementById('resTime').value,
                    guests: document.getElementById('resGuests').value,
                    notes: document.getElementById('resNote').value
                };
                
                // Show loading state
                const submitBtn = reservationForm.querySelector('button[type="submit"]');
                const originalText = submitBtn.textContent;
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Шаље се...';
                
                try {
                    // Send emails via EmailJS
                    const result = await EmailService.sendReservationEmails(formData);
                    
                    // Show toast message
                    EmailService.showMessage(result.message, result.success);
                    
                    if (result.success) {
                        // Reset form and close modal after 2 seconds
                        reservationForm.reset();
                        setTimeout(() => {
                            closeModal();
                        }, 2000);
                    }
                } catch (error) {
                    EmailService.showMessage('Дошло је до грешке. Покушајте поново или нас позовите.', false);
                } finally {
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalText;
                }
            });"""
    
    for filepath in files_with_reservation:
        if not os.path.exists(filepath):
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Провера да ли већ има нови handler
            if 'EmailService.sendReservationEmails' in content:
                print(f"✓ {filepath} - већ има EmailJS handler")
                continue
            
            # Замени alert са EmailJS
            if "alert('Хвала! Ваша резервација је послата" in content:
                content = content.replace(old_handler, new_handler)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✓ {filepath} - ажуриран reservation handler")
            else:
                print(f"- {filepath} - нема стари handler за замену")
                
        except Exception as e:
            print(f"✗ {filepath} - грешка: {e}")

def update_newsletter_forms():
    """Ажурира newsletter форме да имају ID и шаљу EmailJS"""
    
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Провера да ли већ има newsletterForm ID
            if 'id="newsletterForm"' in content:
                print(f"✓ {filepath} - већ има newsletterForm ID")
                continue
            
            # Додај ID на newsletter форму
            if 'class="newsletter-form"' in content:
                # Претвори div у form са ID
                content = re.sub(
                    r'<div class="newsletter-form"([^>]*)>',
                    r'<form id="newsletterForm" class="newsletter-form"\1>',
                    content
                )
                
                # Затвори са </form>
                content = re.sub(
                    r'</div>\s*<div style="margin-top: 1\.5rem',
                    r'</form>\n                    <div style="margin-top: 1.5rem',
                    content
                )
                
                # Додај name и required на input
                content = re.sub(
                    r'<input type="email"([^>]*?)placeholder',
                    r'<input type="email" name="email" required\1placeholder',
                    content
                )
                
                # Замени button са type="submit"
                content = re.sub(
                    r'<button class="newsletter-btn"',
                    r'<button type="submit" class="newsletter-btn"',
                    content
                )
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✓ {filepath} - ажурирана newsletter форма")
            else:
                print(f"- {filepath} - нема newsletter форму")
                
        except Exception as e:
            print(f"✗ {filepath} - грешка: {e}")

if __name__ == '__main__':
    print("🚀 Додавање EmailJS система...\n")
    
    print("📦 Корак 1: Додавање EmailJS SDK-а...")
    for filepath in html_files:
        if os.path.exists(filepath):
            add_emailjs_to_file(filepath)
    
    print("\n🔄 Корак 2: Ажурирање reservation форми...")
    update_reservation_form_handlers()
    
    print("\n📧 Корак 3: Ажурирање newsletter форми...")
    update_newsletter_forms()
    
    print("\n✅ ГОТОВО! EmailJS је додат на све странице")
    print("\n📝 Следећи корак:")
    print("   1. Региструј се на emailjs.com")
    print("   2. Креирај email template-е")
    print("   3. Копирај credentials у js/email-service.js")
    print("\n📖 Детаљна упутства у EMAILJS_SETUP.md")
