# MOBILNI NAVBAR - JEDNOSTAVNO REŠENJE

## ŠTA SAM NAPRAVIO:

Kreirao sam 2 nova fajla koja rešavaju mobilni meni:

1. **mobile-nav.css** - Svi stilovi za mobilni meni
2. **mobile-nav.js** - Sav JavaScript za mobilni meni

## KAKO DA PRIMENITE NA SVE STRANICE:

### Korak 1: Dodaj CSS link u `<head>` sekciju

Nađi ovu liniju u head-u:
```html
<link rel="stylesheet" href="new-style.css">
```

Odmah ispod nje dodaj:
```html
<link rel="stylesheet" href="mobile-nav.css">
```

### Korak 2: Dodaj JavaScript na kraju `<body>` sekcije

Nađi ovu liniju na kraju body-ja:
```html
<script src="i18n.js"></script>
```

Odmah ispod nje dodaj:
```html
<script src="mobile-nav.js"></script>
```

### Korak 3: Obriši SVE stare mobilne stilove

Pronađi i obriši SVE sekcije koje počinju sa:
```html
<style>
    @media (max-width: 1281px) {
    ...
    </style>
```

I SVE JavaScript sekcije koje imaju:
```javascript
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
...
```

## FAJLOVI KOJE TREBA EDITOVATI:

- index.html
- about.html
- contact.html
- gallery.html
- menu.html  
- wine.html
- privacy.html
- sitemap.html
- terms.html

## ŠTA RADI:

- Hamburger ikonica se transformiše u X
- Meni se otvara sa desne strane
- Klik na blur pozadinu zatvara meni
- Klik na link zatvara meni
- BEZ !important konflikata
- ISTI NA SVIM STRANICAMA

## GOTOVO - NEMA VIŠE KOMPLIKACIJA!
