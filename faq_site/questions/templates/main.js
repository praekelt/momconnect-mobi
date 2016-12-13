if ('serviceWorker' in navigator) {

    console.log('Service Worker is supported');

    navigator.serviceWorker.register('/static/questions/js/sw.js', {scope: '/faq_site/questions/'})
    .then(function(reg) {
        console.log("Service Worker successfully registered", reg);
    })
    .catch(function(error) {
        console.log("Service Worker failed to register", error);
    });
}
else{
  console.log('Service Worker is not supported');
}
