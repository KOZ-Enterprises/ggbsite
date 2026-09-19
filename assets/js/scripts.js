

function toggleNavbar() {
  const nav = document.getElementById("myNavbar");
  const open = nav.classList.toggle("responsive");
  const btn = nav.querySelector(".nav-icon");
  if (btn) btn.setAttribute("aria-expanded", String(open));
}

