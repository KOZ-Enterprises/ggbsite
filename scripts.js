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
  loadHTML('footer.html', 'footer');
});

function toggleRow(rowIndex) {
  var row = document.getElementById("row" + rowIndex);
  var icon = document.getElementById("icon" + rowIndex);

  if (row.style.display === "table-row") {
      row.style.display = "none";
      icon.textContent = "+";  // Change to "+" when the row is collapsed
  } else {
      row.style.display = "table-row";
      icon.textContent = "-";  // Change to "-" when the row is expanded
  }
}
