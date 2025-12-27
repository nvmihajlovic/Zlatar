/**
 * Service Worker - Ресторан Златар PWA
 * Обезбеђује offline функционалност и брзо учитавање
 */

const CACHE_NAME = 'zlatar-pwa-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/menu.html',
  '/wine.html',
  '/contact.html',
  '/gallery.html',
  '/about.html',
  '/blog.html',
  '/new-style.css',
  '/js/email-service.js',
  '/i18n.js',
  '/images/znak-restoran-zlatar-vektorski_clipped_rev_1.png',
  // Додатни ресурси се кеширају по потреби
];

// Install event - кеширај основне ресурсе
self.addEventListener('install', (event) => {
  console.log('[Service Worker] Installing...');
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[Service Worker] Caching app shell');
        return cache.addAll(ASSETS_TO_CACHE);
      })
      .then(() => {
        console.log('[Service Worker] Skip waiting');
        return self.skipWaiting();
      })
  );
});

// Activate event - очисти старе кешеве
self.addEventListener('activate', (event) => {
  console.log('[Service Worker] Activating...');
  
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('[Service Worker] Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
    .then(() => {
      console.log('[Service Worker] Claiming clients');
      return self.clients.claim();
    })
  );
});

// Fetch event - Network First са Fallback на Cache
self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // Ако је одговор успешан, кеширај га
        if (response.status === 200) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
        }
        return response;
      })
      .catch(() => {
        // Ако нема интернета, врати из кеша
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          
          // Ако нема у кешу, врати offline страницу
          return caches.match('/index.html');
        });
      })
  );
});

// Push notification event
self.addEventListener('push', (event) => {
  console.log('[Service Worker] Push received');
  
  const data = event.data ? event.data.json() : {};
  const title = data.title || 'Ресторан Златар';
  const options = {
    body: data.body || 'Нова порука од Ресторана Златар',
    icon: '/images/znak-restoran-zlatar-vektorski_clipped_rev_1.png',
    badge: '/images/znak-restoran-zlatar-vektorski_clipped_rev_1.png',
    vibrate: [200, 100, 200],
    tag: 'zlatar-notification',
    requireInteraction: false,
    data: {
      url: data.url || '/',
      dateOfArrival: Date.now()
    },
    actions: [
      {
        action: 'open',
        title: 'Отвори',
        icon: '/images/znak-restoran-zlatar-vektorski_clipped_rev_1.png'
      },
      {
        action: 'close',
        title: 'Затвори'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});

// Notification click event
self.addEventListener('notificationclick', (event) => {
  console.log('[Service Worker] Notification clicked');
  
  event.notification.close();
  
  if (event.action === 'open' || !event.action) {
    const urlToOpen = event.notification.data.url || '/';
    
    event.waitUntil(
      clients.matchAll({ type: 'window', includeUncontrolled: true })
        .then((clientList) => {
          // Провери да ли је апликација већ отворена
          for (let client of clientList) {
            if (client.url === urlToOpen && 'focus' in client) {
              return client.focus();
            }
          }
          // Ако није, отвори нови прозор
          if (clients.openWindow) {
            return clients.openWindow(urlToOpen);
          }
        })
    );
  }
});

// Background sync event (за будућност - offline резервације)
self.addEventListener('sync', (event) => {
  console.log('[Service Worker] Background sync:', event.tag);
  
  if (event.tag === 'sync-reservations') {
    event.waitUntil(
      // Овде би синхронизовао offline резервације
      Promise.resolve()
    );
  }
});
