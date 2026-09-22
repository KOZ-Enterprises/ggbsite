

function toggleNavbar() {
  const nav = document.getElementById("myNavbar");
  if (!nav) return;
  const open = nav.classList.toggle("responsive");
  const btn = nav.querySelector(".nav-icon");
  if (btn) btn.setAttribute("aria-expanded", String(open));
}

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    const nav = document.getElementById("myNavbar");
    if (nav && nav.classList.contains("responsive")) {
      nav.classList.remove("responsive");
      const btn = nav.querySelector(".nav-icon");
      if (btn) {
        btn.setAttribute("aria-expanded", "false");
        btn.focus();
      }
    }
  }
});

document.addEventListener("click", function (e) {
  const nav = document.getElementById("myNavbar");
  if (nav && nav.classList.contains("responsive") && !nav.contains(e.target)) {
    nav.classList.remove("responsive");
    const btn = nav.querySelector(".nav-icon");
    if (btn) btn.setAttribute("aria-expanded", "false");
  }
});

