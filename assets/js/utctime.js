(function() {
  document.addEventListener('DOMContentLoaded', function() {
    const times = document.querySelectorAll('span.utctime');
    times.forEach((t) => {
      try{
        const d = new Date(t.innerText);
        t.innerText = d.toLocaleString();
      } catch(e) {}
    });
  });
})()
