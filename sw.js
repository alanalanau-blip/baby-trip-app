const CACHE_NAME = 'bb-trip-v1';
const urlsToCache = [
  './SCHEDULE.html',
  './manifest.json',
  './icon.png'
];

// 安裝時快取檔案
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache);
      })
  );
});

// 攔截請求，若無網路則提供快取檔案
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response; // 找到快取
        }
        return fetch(event.request); // 無快取則透過網路請求
      })
  );
});