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
  
  document.addEventListener('DOMContentLoaded', function() {
    loadHTML('header.html', 'header');
    loadHTML('footer.html', 'footer');
  });
  