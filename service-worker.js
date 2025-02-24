self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open("lawbot-cache").then((cache) => {
      return cache.addAll([
        "/",
        "favicon.png",
        "manifest.json"
      ]);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
