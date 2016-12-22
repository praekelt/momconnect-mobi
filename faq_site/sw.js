var version = 'v1';

// Note the location of this script should allow scope to cache below
// However resource paths are instead being read by django as urls
// Attempts need to be made to change the way django views these files

var cacheFiles = [
  //'./home/',
  //'./',
  //'./templates/questions/answers.html',t
  //'./templates/questions/home.html',
  //'./templates/questions/index.html',
  //'./templates/questions/questions.html',
];

self.addEventListener('install', function(e){
  console.log('Service Worker successfully installed');
  e.waitUntil(
    caches.open(version).then(function(cache){
      console.log('Caching files...', cacheFiles);
      return cache.addAll(cacheFiles);
    })
  );
});

self.addEventListener("activate", function(event) {
  /* Just like with the install event, event.waitUntil blocks activate on a promise.
     Activation will fail unless the promise is fulfilled.
  */
  console.log('WORKER: activate event in progress.');

  event.waitUntil(
    caches
      /* This method returns a promise which will resolve to an array of available
         cache keys.
      */
      .keys()
      .then(function (keys) {
        // We return a promise that settles when all outdated caches are deleted.
        return Promise.all(
          keys
            .filter(function (key) {
              // Filter by keys that don't start with the latest version prefix.
              return !key.startsWith(version);
            })
            .map(function (key) {
              /* Return a promise that's fulfilled
                 when each outdated cache is deleted.
              */
              return caches.delete(key);
            })
        );
      })
      .then(function() {
        console.log('WORKER: activate completed.');
      })
  );
});

// self.addEventListener('activate', function(event) {
//   console.log('Activated', event);
// });

self.addEventListener('push', function(event) {
  console.log('Push message received', event);
  // TODO
});
