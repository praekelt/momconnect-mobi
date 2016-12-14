var version = 'v1';

var cacheFiles = [
  './',
  './',
  './templates/questions/answers.html',
  './templates/questions/home.html',
  './templates/questions/index.html',
  './templates/questions/questions.html',
];


self.addEventListener('install', function(e){
  console.log('Service Worker successfully installed');
  e.waitUntil(
    caches.open(version).then(function(cache){
      console.log('Caching files...');
      return cache.addAll(cacheFiles);
    })
  );
});

self.addEventListener('activate', function(event) {
  console.log('Activated', event);
});

self.addEventListener('push', function(event) {
  console.log('Push message received', event);
  // TODO
});
