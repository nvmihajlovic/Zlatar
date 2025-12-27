# 📧 Newsletter System Setup Guide

Овај guide показује како поставити **бесплатан newsletter систем** користећи Supabase + Netlify.

---

## 🎯 Шта добијаш:

✅ **Email signup форма** у footer-у  
✅ **Supabase база** за чување email-ова  
✅ **Дупликат prevention** - један email = једна пријава  
✅ **Export у CSV** - за Mailchimp/SendGrid/MailerLite  
✅ **Analytics dashboard** - преглед subscriber-а  
✅ **Fallback** - ради и offline (localStorage)  

---

## 🔧 Setup Кораци

### **Корак 1: Додај SQL у Supabase**

1. Отвори Supabase Dashboard (исти пројекат као за blog stats)
2. Иди на **SQL Editor**
3. Копирај садржај из `supabase-newsletter.sql`
4. Кликни **Run**
5. ✅ Требало би да видиш: "Success. No rows returned"

Ово креира:
- 📊 Табелу `newsletter_subscribers` (email, name, дате)
- 🔒 Row Level Security
- ⚙️ Функције за subscribe/unsubscribe
- 📈 View за лак export

### **Корак 2: Конфигуриши JavaScript**

1. Отвори `js/newsletter-supabase.js`
2. Пронађи линије 14-15:
```javascript
const SUPABASE_URL = 'https://your-project.supabase.co';
const SUPABASE_ANON_KEY = 'your-anon-key-here';
```
3. Замени са **истим credentials-има** као за blog stats
4. Сачувај фајл

### **Корак 3: Додај у Footer**

У **footer секцији** свих HTML страница, пронађи newsletter форму и додај ID:

**ПРИМЕР - index.html:**

```html
<!-- Newsletter Form -->
<form id="newsletterForm" style="display: flex; gap: 0.5rem; max-width: 400px;">
    <input 
        type="email" 
        placeholder="Ваша email адреса" 
        required
        style="flex: 1; padding: 0.875rem 1.25rem; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; color: #fff; font-size: 0.9rem;"
    >
    <button 
        type="submit"
        style="background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); color: #fff; font-weight: 600; padding: 0.875rem 1.75rem; border: none; border-radius: 8px; cursor: pointer; transition: all 0.3s; font-size: 0.9rem;">
        Пријави се
    </button>
</form>
```

**ВАЖНО**: Додај `id="newsletterForm"` на форму!

### **Корак 4: Додај JavaScript у Footer (пре `</body>`)**

```html
<!-- Newsletter System -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="js/newsletter-supabase.js"></script>
```

---

## 🧪 Тестирање

### **1. Локални тест:**

1. Отвори `index.html` у прегледачу
2. Scroll до footer-а
3. Унеси свој email → Кликни "Пријави се"
4. Требало би да видиш: ✅ **"Успешно сте се пријавили за newsletter!"**

### **2. Провера у Supabase:**

1. Иди на Supabase Dashboard
2. **Table Editor** → `newsletter_subscribers`
3. Требало би да видиш свој email! 🎉

### **3. Дупликат тест:**

1. Покушај да се пријавиш истим email-ом поново
2. Требало би да видиш: ⚠️ **"Ова email адреса је већ пријављена"**

### **4. Валидација тест:**

1. Унеси невалидан email: `test@test`
2. Требало би да видиш: ❌ **"Молимо унесите валидну email адресу"**

---

## 📊 Преглед Subscriber-а

### **Dashboard метод:**

1. Supabase → **Table Editor** → `newsletter_subscribers`
2. Види све subscriber-е са датумима
3. Можеш мануелно обрисати или едитовати

### **Export у CSV:**

1. У Supabase, иди на **SQL Editor**
2. Run query:
```sql
SELECT email, name, subscribed_at 
FROM newsletter_subscribers 
WHERE is_active = true 
ORDER BY subscribed_at DESC;
```
3. Кликни **Download CSV** (горе десно)
4. Upload у **Mailchimp** / **SendGrid** / **MailerLite**

---

## 📈 Корисни SQL Queries

### **Број активних subscriber-а:**
```sql
SELECT COUNT(*) as total_subscribers
FROM newsletter_subscribers
WHERE is_active = true;
```

### **Нови subscriber-и (задњих 7 дана):**
```sql
SELECT email, name, subscribed_at
FROM newsletter_subscribers
WHERE subscribed_at > NOW() - INTERVAL '7 days'
AND is_active = true
ORDER BY subscribed_at DESC;
```

### **Статистика по датумима:**
```sql
SELECT 
    DATE(subscribed_at) as date,
    COUNT(*) as new_subscribers
FROM newsletter_subscribers
WHERE is_active = true
GROUP BY DATE(subscribed_at)
ORDER BY date DESC
LIMIT 30;
```

### **Export за Mailchimp:**
```sql
SELECT 
    email as "Email Address",
    name as "First Name",
    subscribed_at as "Subscribed Date"
FROM newsletter_subscribers
WHERE is_active = true;
```

---

## 📧 Интеграција са Email Сервисима

### **Опција 1: Мануелни Export (Најлакше)**

1. Једном недељно export-уј CSV из Supabase
2. Upload у Mailchimp/SendGrid/MailerLite
3. Пошаљи newsletter campaign

### **Опција 2: Zapier (Аутоматски)**

1. Креирај Zapier account (бесплатно)
2. New Zap: **Supabase → Mailchimp**
3. Trigger: "New row in newsletter_subscribers"
4. Action: "Add subscriber to Mailchimp list"
5. ✅ Аутоматски sync!

### **Опција 3: Make.com (Advanced)**

1. Креирај Make.com account
2. Create scenario: Supabase webhook → Email service
3. Trigger on new subscriber
4. Send welcome email аутоматски

---

## 🎨 Побољшања Newsletter Форме

### **Додај Name поље:**

```html
<form id="newsletterForm" style="display: flex; flex-direction: column; gap: 0.75rem; max-width: 400px;">
    <input 
        type="text" 
        id="subscriberName"
        placeholder="Ваше име (опционо)" 
        style="padding: 0.875rem 1.25rem; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; color: #fff; font-size: 0.9rem;"
    >
    <div style="display: flex; gap: 0.5rem;">
        <input 
            type="email" 
            id="subscriberEmail"
            placeholder="Ваша email адреса" 
            required
            style="flex: 1; padding: 0.875rem 1.25rem; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; color: #fff; font-size: 0.9rem;"
        >
        <button type="submit">Пријави се</button>
    </div>
</form>
```

Затим ажурирај JavaScript:
```javascript
const email = newsletterForm.querySelector('#subscriberEmail').value;
const name = newsletterForm.querySelector('#subscriberName').value;
const result = await NewsletterSystem.subscribe(email, name);
```

### **Додај Privacy Link:**

```html
<p style="font-size: 0.75rem; color: rgba(255,255,255,0.5); margin-top: 0.5rem;">
    Пријавом прихватате нашу <a href="privacy.html" style="color: #D4AF37; text-decoration: underline;">политику приватности</a>
</p>
```

---

## 🔒 GDPR Compliance

### **Unsubscribe link:**

Додај на крају footer-а:
```html
<p style="font-size: 0.75rem; color: rgba(255,255,255,0.5);">
    Желите да се одјавите? 
    <a href="#" id="unsubscribeLink" style="color: #D4AF37; text-decoration: underline;">Кликните овде</a>
</p>

<script>
document.getElementById('unsubscribeLink').addEventListener('click', async (e) => {
    e.preventDefault();
    const email = prompt('Унесите вашу email адресу за одјаву:');
    if (email) {
        const result = await NewsletterSystem.unsubscribe(email);
        alert(result.message);
    }
});
</script>
```

---

## 💡 Pro Tips

### **1. Welcome Email (са Netlify Functions):**

Креирај `netlify/functions/send-welcome-email.js`:
```javascript
const sgMail = require('@sendgrid/mail');

exports.handler = async (event) => {
    const { email, name } = JSON.parse(event.body);
    
    sgMail.setApiKey(process.env.SENDGRID_API_KEY);
    
    await sgMail.send({
        to: email,
        from: 'info@restoranzlatar.com',
        subject: 'Добродошли у Златар Newsletter!',
        text: `Здраво ${name || 'пријатељу'}! Хвала што сте се придружили...`
    });
    
    return { statusCode: 200 };
};
```

### **2. Subscriber Count Badge:**

```html
<div style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background: rgba(212,175,55,0.15); border-radius: 20px; font-size: 0.875rem; color: #D4AF37;">
    <i class="fas fa-users"></i>
    <span id="subscriberCount">0</span> претплатника
</div>

<script>
// Fetch count from Supabase
async function updateSubscriberCount() {
    const { count } = await supabase
        .from('newsletter_subscribers')
        .select('*', { count: 'exact', head: true })
        .eq('is_active', true);
    
    document.getElementById('subscriberCount').textContent = count || 0;
}
updateSubscriberCount();
</script>
```

---

## 🆘 Troubleshooting

**Форма не ради:**
- Провери да ли је `id="newsletterForm"` додат
- Провери Console (F12) за грешке
- Провери да ли је Supabase SDK учитан

**Email се не чува:**
- Провери Supabase credentials у newsletter-supabase.js
- Провери да ли је SQL script покренут
- Провери Network tab у DevTools

**Дупликат се ипак прикаже:**
- Очисти browser cache
- Hard refresh: Ctrl+F5

---

## ✨ Резиме

Сада имаш:
- ✅ Newsletter систем са Supabase backend-ом
- ✅ Валидација и дупликат prevention
- ✅ CSV export за email сервисе
- ✅ GDPR compliant (unsubscribe)
- ✅ Fallback на localStorage
- ✅ Analytics и статистике

**Setup време: 10 минута**  
**Трошак: $0/месечно**  
**Капацитет: 500MB = хиљаде subscriber-а** 🎉

---

## 📞 Следећи кораци:

1. Setup Mailchimp account (бесплатно до 500 контаката)
2. Design newsletter template
3. Export subscriber-е из Supabase → Import у Mailchimp
4. Шаљи месечне newsletter-е! 📧

Хоћеш ли да ти помогнем и са **Netlify deployment-ом** сада? 🚀
