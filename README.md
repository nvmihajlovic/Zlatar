# Ресторан Златар - Модеран Веб Сајт

## 📋 Преглед пројекта

Модеран, респонзивни веб сајт за етно ресторан Златар са напредним popup функцијама, златном темом и mobile-first дизајном.

---

## ✨ Кључне карактеристике

### 🎨 Дизајн
- **Златна палета**: #D4AF37 (Primary), #1a3a1a (Dark Green), #FFA500 (Amber)
- **Typography**: Playfair Display (headings) + Montserrat (body)
- **Mobile-first**: Потпуно респонзиван дизајн (480px, 768px, 1024px breakpoints)
- **Smooth animations**: Fade-in, slide-up, parallax, 3D tilt effects

### 📱 Секције
1. **Hero** - Full-screen са златним градијентом, статистикама (95/80/31)
2. **О нама** - Прича од 1985., породица Поповић, Милешева heritage
3. **Специјалитети** - 4 категорије јела, CTA box
4. **Ракије** - 31 врста домаће ракије, велики counter
5. **Музика** - Распорред бендова по данима (Уторак-Недеља)
6. **Галерија** - Grid са lightbox функцијом
7. **Услуге** - Организација догађаја (свадбе, рођендани, пословни)
8. **Контакт** - Форма + социјалне мреже + радно време

---

## 🎯 POPUP СИСТЕМ - 3 врсте popup-а

### 1️⃣ **Newsletter Popup** (Пријава на newsletter)

**Тригер**: Аутоматски после 5 секунди (само прво посећивање)

**Карактеристике**:
- Email подстрекивање за newsletter
- 3 бенефита (Ексклузивне понуде, Догађаји, Попусти)
- Checkbox за услове коришћења
- Cookie persistence (7 дана)

**Како користити**:
```javascript
// Мануални тригер
popupManager.show('newsletter');

// Аутоматски тригер (већ подешен)
setTimeout(() => {
    popupManager.show('newsletter');
}, 5000);
```

**Где је дефинисан**: 
- HTML: `<div class="modal" id="newsletter-modal">` (линија ~420)
- CSS: `.modal-newsletter` (линија ~1080)
- JS: Auto-trigger (линија ~180)

---

### 2️⃣ **Special Offer Popup** (Промо понуда)

**Тригер**: Аутоматски на 30% скрола (само прво посећивање)

**Карактеристике**:
- Промо пакет "Злата Традиција"
- Стара цена (прецртана) + Нова цена (истакнута)
- Листа артикала (5 ставки)
- 2 дугмета (Резервиши / Касније)
- Badge "ПРОМОЦИЈА"

**Како користити**:
```javascript
// Мануални тригер
document.getElementById('btn-special-offer').addEventListener('click', () => {
    popupManager.show('specialOffer');
});

// Аутоматски тригер (већ подешен на 30% скрола)
window.addEventListener('scroll', () => {
    if (scrollPercentage >= 30) {
        popupManager.show('specialOffer');
    }
});
```

**Где је дефинисан**:
- HTML: `<div class="modal" id="special-offer-modal">` (линија ~480)
- CSS: `.modal-offer` (линија ~1120)
- JS: Scroll trigger (линија ~185)

---

### 3️⃣ **Reservation Modal** (Резервација стола)

**Тригер**: Мануално (кликом на дугмад "Резервишите сто")

**Карактеристике**:
- 7 поља (Име, Телефон, Датум, Време, Број особа, Напомена)
- Валидација за датум (не може у прошлости)
- Drop-down за број особа (2, 4, 6, 8, 10+)
- Notification систем (success/error)
- Форма се ресетује после слања

**Како користити**:
```javascript
// Тригер дугмад
document.getElementById('btn-reserve-nav').addEventListener('click', () => {
    popupManager.show('reservation');
});

document.getElementById('btn-reserve-hero').addEventListener('click', () => {
    popupManager.show('reservation');
});
```

**Где је дефинисан**:
- HTML: `<div class="modal" id="reservation-modal">` (линија ~380)
- CSS: `.modal-reservation` (линија ~1050)
- JS: Triggers (линија ~150-160)

---

## 🔧 PopupManager Class - Како ради

### Методе:

#### `show(popupName)`
Приказује popup и проверава да ли је већ приказан данас.
```javascript
popupManager.show('newsletter');
popupManager.show('specialOffer');
popupManager.show('reservation');
```

#### `hide(popupName)`
Сакрива специфичан popup.
```javascript
popupManager.hide('newsletter');
```

#### `hideAll()`
Сакрива све popup-е одједном.
```javascript
popupManager.hideAll();
```

#### `setCookie(popupName, days)`
Поставља cookie да не приказује popup поново (default: 1 дан).
```javascript
popupManager.setCookie('newsletter', 7); // Не приказуј 7 дана
```

#### `checkCookie(popupName)`
Проверава да ли је popup већ приказан.
```javascript
if (!popupManager.checkCookie('newsletter')) {
    popupManager.show('newsletter');
}
```

---

## 🎪 Како додати нови popup

### 1. HTML структура
```html
<div class="modal" id="my-custom-modal">
    <div class="modal-overlay"></div>
    <div class="modal-content">
        <button class="modal-close"><i class="fas fa-times"></i></button>
        <div class="modal-header">
            <h2>Наслов</h2>
            <p>Опис</p>
        </div>
        <form class="modal-form" id="my-custom-form">
            <!-- Твој садржај -->
            <button type="submit" class="btn btn-primary btn-full">
                <span>Пошаљи</span>
            </button>
        </form>
    </div>
</div>
```

### 2. Регистровање у PopupManager
```javascript
// У constructor PopupManager класе
this.popups = {
    reservation: document.getElementById('reservation-modal'),
    newsletter: document.getElementById('newsletter-modal'),
    specialOffer: document.getElementById('special-offer-modal'),
    myCustom: document.getElementById('my-custom-modal') // ДОДАЈ ОВО
};
```

### 3. Тригер дугме
```javascript
document.getElementById('btn-my-custom').addEventListener('click', () => {
    popupManager.show('myCustom');
});
```

### 4. Form submission
```javascript
document.getElementById('my-custom-form').addEventListener('submit', (e) => {
    e.preventDefault();
    showNotification('Успешно!', 'success');
    popupManager.hide('myCustom');
    popupManager.setCookie('myCustom', 7);
    e.target.reset();
});
```

---

## 🚀 Напредне функције

### Аутоматски тригери

#### Time-based (после X секунди)
```javascript
setTimeout(() => {
    if (!popupManager.checkCookie('myPopup')) {
        popupManager.show('myPopup');
    }
}, 10000); // 10 секунди
```

#### Scroll-based (на X% скрола)
```javascript
let shown = false;
window.addEventListener('scroll', () => {
    const scrollPercentage = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
    
    if (scrollPercentage >= 50 && !shown && !popupManager.checkCookie('myPopup')) {
        popupManager.show('myPopup');
        shown = true;
    }
});
```

#### Exit-intent (када мишем иде ван прозора)
```javascript
document.addEventListener('mouseout', (e) => {
    if (!e.toElement && !e.relatedTarget && !popupManager.checkCookie('exitPopup')) {
        popupManager.show('exitPopup');
        popupManager.setCookie('exitPopup', 1);
    }
});
```

#### Idle-based (после X секунди неактивности)
```javascript
let idleTimer;
function resetIdleTimer() {
    clearTimeout(idleTimer);
    idleTimer = setTimeout(() => {
        if (!popupManager.checkCookie('idlePopup')) {
            popupManager.show('idlePopup');
        }
    }, 30000); // 30 секунди
}

['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart'].forEach(event => {
    document.addEventListener(event, resetIdleTimer, true);
});
resetIdleTimer();
```

---

## 📊 Cookie систем

### Како функционише:
- **Име**: `popup_{popupName}_shown`
- **Вредност**: `true`
- **Трајање**: Подесиво (default 1 дан)
- **Path**: `/` (цео сајт)

### Cookie persistence:
- **Newsletter**: 7 дана
- **Special Offer**: 1 дан
- **Reservation**: 1 дан (после слања)

### Ресетовање cookies:
```javascript
// У browser console:
document.cookie = "popup_newsletter_shown=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
document.cookie = "popup_specialOffer_shown=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
document.cookie = "popup_reservation_shown=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
```

---

## 🎨 Стилизовање popup-а

### Основни стилови (style.css)
```css
.modal {
    position: fixed;
    z-index: 10000;
    backdrop-filter: blur(5px);
}

.modal-content {
    background: white;
    border-radius: 20px;
    max-width: 500px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.modal.active {
    opacity: 1;
    pointer-events: all;
}
```

### Анимације:
- **Fade-in**: Opacity 0 → 1
- **Slide-up**: translateY(50px) → 0
- **Backdrop blur**: Замаглјен позадински садржај

### Респонзивност:
```css
@media (max-width: 768px) {
    .modal-content {
        width: 95%;
        max-height: 95vh;
    }
}
```

---

## 🔔 Notification систем

### Коришћење:
```javascript
showNotification('Порука', 'success'); // Зелена ✓
showNotification('Порука', 'error');   // Црвена ✗
```

### Карактеристике:
- Аутоматски нестаје после 3 секунде
- Slide-in анимација са десне стране
- Иконе (check-circle / exclamation-circle)
- Респонзиван дизајн

---

## 🎯 Lightbox Галерија

### Карактеристике:
- Клик на било коју слику у галерији
- Full-screen преглед
- Previous/Next дугмад
- Keyboard навигација (← → ESC)
- Затварање кликом на overlay

### Контроле:
- **←** Претходна слика
- **→** Следећа слика
- **ESC** Затвори lightbox
- **Клик на overlay** Затвори

---

## 🌐 Остале интеракције

### Navbar
- Transparent → Solid на скролу
- Active link highlighting
- Mobile hamburger menu

### Hero секција
- Parallax позадина (0.5 коефицијент)
- Animated counters (95, 80, 31)
- Bounce анимација на scroll hint

### Картице
- 3D tilt effect на hover (mouse position)
- Transform scale на hover
- Box-shadow elevation

### Форме
- Real-time валидација
- Email regex провера
- Минимум датум (данас) за резервације

### Дугмад
- Ripple effect на клик
- Smooth transitions
- Hover lift effect

---

## 📦 Структура фајлова

```
Restoran Zlatar Novi/
│
├── index.html          # Главна HTML структура (757 линија)
├── style.css           # Златна тема + респонзивност (1300+ линија)
├── script.js           # PopupManager + све интеракције (450+ линија)
└── README.md           # Ова документација
```

---

## 🔧 Технологије

- **HTML5** - Semantic markup
- **CSS3** - Custom properties, Grid, Flexbox, Animations
- **JavaScript ES6+** - Classes, Arrow functions, Template literals
- **Font Awesome 6.4.0** - Иконе
- **Google Fonts** - Playfair Display, Montserrat

---

## 📱 Респонзивни breakpoints

### Desktop (1024px+)
- Full navigation
- Multi-column layouts
- Large typography

### Tablet (768px - 1024px)
- Hamburger menu
- 2-column grids
- Medium typography

### Mobile (480px - 768px)
- Stacked layouts
- Single column
- Optimized touch targets

### Small mobile (< 480px)
- Smaller padding
- Compact components
- Reduced font sizes

---

## 🎨 Палета боја

| Боја | Hex код | Употреба |
|------|---------|----------|
| Gold Primary | #D4AF37 | Дугмад, акценти, наслови |
| Gold Light | #F4E4C1 | Позадине, badges |
| Gold Dark | #B8941F | Hover states |
| Green Dark | #1a3a1a | Navbar, footer, текст |
| Green Medium | #2c4a3e | Секундарне секције |
| Amber | #FFA500 | Call-to-action |
| Cream | #FFF8DC | Светле позадине |

---

## ⚡ Перформансе

### Оптимизације:
- ✅ Debounced scroll events (10ms)
- ✅ IntersectionObserver за анимације
- ✅ RequestAnimationFrame за smooth counters
- ✅ CSS transforms (GPU-accelerated)
- ✅ Lazy loading за галерију
- ✅ Минималне reflows/repaints

### Предлози:
- 📌 Компресовати слике (WebP format)
- 📌 Минификовати CSS/JS за продукцију
- 📌 Користити CDN за библиотеке
- 📌 Додати Service Worker за offline

---

## 🚀 Deployment

### 1. Upload фајлове на сервер
```bash
# Via FTP ili SSH
scp -r * user@server:/var/www/restoranzlatar.com/
```

### 2. Провери permissions
```bash
chmod 755 index.html style.css script.js
```

### 3. Тестирај на различитим уређајима
- Desktop (Chrome, Firefox, Safari, Edge)
- Tablet (iPad, Android tablets)
- Mobile (iOS, Android)

---

## 📞 Контакт за подршку

**Web Studio Link**
- 🌐 Website: https://www.webstudiolink.rs/
- 📧 Email: info@webstudiolink.rs

---

## 📝 Лиценца

© 2024 Ресторан Златар. Сва права задржана.

---

## 🎉 Credits

**Дизајн & Развој**: Web Studio Link
**Година**: 2024
**Верзија**: 1.0.0

---

**Уживајте у новом модерном сајту! 🌟✨**
