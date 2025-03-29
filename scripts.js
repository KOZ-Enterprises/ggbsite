function loadHTML(url, elementId) {
  console.log(`Attempting to load ${url} into #${elementId}`);
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error(`Network response was not ok: ${response.statusText}`);
      }
      return response.text();
    })
    .then(data => {
      document.getElementById(elementId).innerHTML = data;
      console.log(`Loaded ${url} into #${elementId}`);
    })
    .catch(error => console.error(`Error loading ${url}:`, error));
}

document.addEventListener('DOMContentLoaded', function () {
  loadHTML('header.html', 'header');
  loadHTML('nav.html', 'nav', highlightActiveLink);
  loadHTML('footer.html', 'footer');

});

function highlightActiveLink() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('nav a');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage) {
      link.classList.add('active');
    }
  });
}