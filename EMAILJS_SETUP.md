# 📧 EmailJS Setup Guide - Automatic Email Responses

Овај guide показује како поставити **аутоматске email одговоре** за све форме на сајту.

---

## 🎯 Шта добијаш:

✅ **Резервација** - Confirmation кориснику + notification ресторану  
✅ **Контакт форма** - "Примили смо вашу поруку" + notification  
✅ **Newsletter** - Welcome email  
✅ **Бесплатно** - 200 email-ова месечно  
✅ **Без backend-а** - само JavaScript  

---

## 🚀 Setup (15 минута)

### **Корак 1: Креирај EmailJS Account**

1. Иди на: https://www.emailjs.com/
2. Кликни **"Sign Up"** (горе десно)
3. Региструј се преко Google-а или email-а
4. Потврди email адресу

### **Корак 2: Додај Email Service**

1. У EmailJS Dashboard, кликни **"Add New Service"**
2. Изабери **Gmail** (најлакше)
3. Кликни **"Connect Account"**
4. Login са Gmail-ом ресторана (`restoranzlatar@gmail.com`)
5. Дозволи приступ
6. Копирај **Service ID** (нешто као `service_abc123`)

💡 **Алтернатива**: Можеш користити Outlook, Yahoo, или Custom SMTP

### **Корак 3: Креирај Email Templates**

Требаш да креираш **5 template-а**:

#### **Template 1: Reservation Confirmation (за госта)**

1. Кликни **"Email Templates"** → **"Create New Template"**
2. **Template Name**: `Reservation Confirmation`
3. **Template ID**: `template_reservation_confirmation`
4. **Content** (копирај овај template):

```html
Поштовани/а {{guest_name}},

Хвала што сте изабрали Ресторан Златар!

ДЕТАЉИ РЕЗЕРВАЦИЈЕ:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Датум: {{reservation_date}}
🕐 Време: {{reservation_time}}
👥 Број гостију: {{number_of_guests}}
📝 Напомене: {{special_requests}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ваша резервација је ПРИМЉЕНА и очекујемо вас.

Уколико желите да промените или откажете резервацију, молимо вас да нас контактирате:
📞 +381 11 234 5678
📧 info@restoranzlatar.com

Радујемо се вашој посети!

С поштовањем,
Тим Ресторана Златар
```

**Subject line**: `Потврда резервације - Ресторан Златар`

5. Кликни **"Save"**

#### **Template 2: Reservation Admin Notification**

1. **Template Name**: `Reservation Admin Notification`
2. **Template ID**: `template_reservation_admin`
3. **Content**:

```html
НОВА РЕЗЕРВАЦИЈА!

ИНФОРМАЦИЈЕ О ГОСТУ:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Име: {{guest_name}}
📧 Email: {{guest_email}}
📞 Телефон: {{guest_phone}}

ДЕТАЉИ РЕЗЕРВАЦИЈЕ:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Датум: {{reservation_date}}
🕐 Време: {{reservation_time}}
👥 Број гостију: {{number_of_guests}}
📝 Напомене: {{special_requests}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Потребна акција: Потврди резервацију контактирањем госта.
```

**To Email**: `{{admin_email}}` (admin email ће бити послат из кода)  
**Subject**: `🔔 Нова резервација - {{guest_name}}`

#### **Template 3: Contact Confirmation (за пошиљаоца)**

1. **Template Name**: `Contact Form Confirmation`
2. **Template ID**: `template_contact_confirmation`
3. **Content**:

```html
Поштовани/а {{guest_name}},

Хвала вам што сте нас контактирали!

Примили смо вашу поруку и одговорићемо вам у најкраћем могућем року (обично у року од 24 сата).

ВАША ПОРУКА:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{message_content}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Уколико је хитно, можете нас контактирати директно:
📞 +381 11 234 5678
📧 info@restoranzlatar.com

С поштовањем,
Тим Ресторана Златар
```

**Subject**: `Примили смо вашу поруку - Ресторан Златар`

#### **Template 4: Contact Admin Notification**

1. **Template Name**: `Contact Admin Notification`
2. **Template ID**: `template_contact_admin`
3. **Content**:

```html
НОВА ПОРУКА СА КОНТАКТ ФОРМЕ!

ОД:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
👤 Име: {{guest_name}}
📧 Email: {{guest_email}}
📞 Телефон: {{guest_phone}}
📋 Тема: {{message_subject}}

ПОРУКА:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{message_content}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Одговори на: {{guest_email}}
```

**To Email**: `{{admin_email}}`  
**Subject**: `💬 Нова порука - {{guest_name}}`

#### **Template 5: Newsletter Welcome**

1. **Template Name**: `Newsletter Welcome`
2. **Template ID**: `template_newsletter_confirmation`
3. **Content**:

```html
Здраво {{subscriber_name}}!

Добродошли у Златар Newsletter! 🎉

Хвала што сте се придружили нашој заједници. Од сада ћете бити први који ће сазнати за:

🍷 Специјалне дегустације вина
🍽️ Нова јела и сезонске специјалитете
🎵 Жива музика и догађаје
💰 Ексклузивне попусте и промоције

Очекујте наш први newsletter ускоро!

Волите нас и на друштвеним мрежама:
📘 Facebook: /restoranzlatar
📸 Instagram: @restoranzlatar

Не желите више да примате? Одјавите се овде: [Unsubscribe Link]

Пријатно,
Тим Ресторана Златар
```

**Subject**: `Добродошли у Златар Newsletter! 🎉`

### **Корак 4: Преузми Credentials**

1. У EmailJS Dashboard, кликни **Account** (горе десно)
2. Копирај:
   - **Service ID**: `service_abc123`
   - **User ID (Public Key)**: `user_xyz789`

### **Корак 5: Конфигуриши JavaScript**

1. Отвори `js/email-service.js`
2. Пронађи линије 14-15:
```javascript
SERVICE_ID: 'your_service_id',
USER_ID: 'your_user_id',
```
3. Замени са својим credentials-има:
```javascript
SERVICE_ID: 'service_abc123',  // твој Service ID
USER_ID: 'user_xyz789',        // твој User ID
```
4. Сачувај фајл

### **Корак 6: Додај EmailJS SDK**

У `<head>` секцији **свих HTML страница**, додај:

```html
<!-- EmailJS SDK -->
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script src="js/email-service.js"></script>
```

---

## 🔗 Интеграција са Формама

### **РЕЗЕРВАЦИЈА (Reservation Modal)**

Пронађи submit handler за резервацију (приближно линија 1500-1600) и замени:

```javascript
// У reservationForm submit handler-у
reservationForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Get form data
    const formData = {
        name: document.getElementById('resName').value,
        email: document.getElementById('resEmail').value,
        phone: document.getElementById('resPhone').value,
        date: document.getElementById('resDate').value,
        time: document.getElementById('resTime').value,
        guests: document.getElementById('resGuests').value,
        notes: document.getElementById('resNotes').value
    };
    
    // Show loading state
    const submitBtn = this.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.textContent = 'Шаље се...';
    
    try {
        // Send emails via EmailJS
        const result = await EmailService.sendReservationEmails(formData);
        
        // Show message
        EmailService.showMessage(result.message, result.success);
        
        if (result.success) {
            // Reset form
            this.reset();
            
            // Close modal after 2 seconds
            setTimeout(() => {
                document.getElementById('modalOverlay').click();
            }, 2000);
        }
    } catch (error) {
        EmailService.showMessage('Грешка при слању. Покушајте поново.', false);
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    }
});
```

### **КОНТАКТ ФОРМА (Contact Page)**

На `contact.html` страници:

```javascript
document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = {
        name: this.querySelector('[name="name"]').value,
        email: this.querySelector('[name="email"]').value,
        phone: this.querySelector('[name="phone"]').value,
        subject: this.querySelector('[name="subject"]').value,
        message: this.querySelector('[name="message"]').value
    };
    
    const submitBtn = this.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    submitBtn.textContent = 'Шаље се...';
    
    try {
        const result = await EmailService.sendContactEmails(formData);
        EmailService.showMessage(result.message, result.success);
        
        if (result.success) {
            this.reset();
        }
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Пошаљи поруку';
    }
});
```

### **NEWSLETTER (Footer Form)**

Ажурирај newsletter handler:

```javascript
// У js/newsletter-supabase.js, после успешног subscribe-а:
const result = await NewsletterSystem.subscribe(email);

if (result.success) {
    // Send welcome email
    await EmailService.sendNewsletterEmail({ email, name: null });
    
    // Show message
    EmailService.showMessage('Пријава успешна! Проверите email.', true);
}
```

---

## 🧪 Тестирање

### **1. Test Reservation:**

1. Попуни резервацију са **својим email-ом**
2. Submit форму
3. Провери **inbox** - требало би да стигне confirmation
4. Провери **restoranzlatar@gmail.com** - требало би admin notification

### **2. Test Contact:**

1. Попуни контакт форму
2. Submit
3. Провери email-ове

### **3. Test Newsletter:**

1. Пријави се за newsletter
2. Провери welcome email

---

## 📊 EmailJS Dashboard - Monitoring

После слања:

1. Иди на EmailJS Dashboard
2. **Email History** - види све послате email-ове
3. **Usage** - провери колико је остало (200/месец на free плану)

---

## 💰 Трошкови

| План | Email-ова/месец | Цена |
|------|----------------|------|
| **Free** | 200 | $0 |
| **Personal** | 1,000 | $7/месец |
| **Professional** | 10,000 | $20/месец |

**За ресторан**: Free план је довољан (200 email-ова = ~6-7 резервација дневно)

---

## 🎨 Customization

### **Промени admin email:**

У `js/email-service.js`, промени:
```javascript
admin_email: 'tvoj-novi-email@gmail.com'
```

### **Додај додатна поља:**

У template-има, можеш користити било које поље из `emailData` објекта:
```javascript
const emailData = {
    custom_field: 'твоја вредност',
    // ...
};
```

У template-у:
```
{{custom_field}}
```

---

## 🔒 Сигурност

EmailJS је **сигуран** јер:
- ✅ User ID је јаван (безбедно у frontend-у)
- ✅ Gmail login је преко OAuth
- ✅ Нема credentials-а у коду
- ✅ Rate limiting (200/месец на free)

---

## 🆘 Troubleshooting

**Email-ови не стижу:**
- Провери **Spam folder**
- Провери Service ID и User ID
- Провери Template ID-јеве
- Отвори Console (F12) за грешке

**"Service not found" грешка:**
- Провери да ли је Gmail account connection активан
- Reconnect Gmail у EmailJS Dashboard

**Template not found:**
- Провери Template ID тачно (case-sensitive)
- Сачувај template после промене

---

## ✨ Резиме

Сада имаш:
- ✅ Аутоматске confirmation email-ове за кориснике
- ✅ Admin notifications за све форме
- ✅ Welcome email за newsletter
- ✅ Toast поруке на сајту
- ✅ Email history и monitoring

**Setup време: 15 минута**  
**Трошак: $0/месечно**  
**Капацитет: 200 email-ова месечно** 📧

---

Следећи корак: Deploy на Netlify! 🚀
