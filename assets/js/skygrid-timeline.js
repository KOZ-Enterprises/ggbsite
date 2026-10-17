// The chart and accessible table are rendered by Jekyll. JS only adds tooltips.
(() => {
    const chart = document.querySelector('.skygrid-chart');
    if (!chart) return;
    const tip = chart.querySelector('.sg-tooltip');
    const hide = () => { tip.hidden = true; };
    const show = (mark, x, y) => {
        tip.textContent = mark.getAttribute('aria-label');
        tip.hidden = false;
        tip.style.left = Math.max(8, Math.min(x + 14, innerWidth - tip.offsetWidth - 8)) + 'px';
        tip.style.top = Math.max(8, Math.min(y + 14, innerHeight - tip.offsetHeight - 8)) + 'px';
    };
    chart.querySelectorAll('.sg-mark').forEach(mark => {
        mark.addEventListener('pointermove', e => show(mark, e.clientX, e.clientY));
        mark.addEventListener('pointerleave', hide);
        mark.addEventListener('focus', () => {
            const rect = mark.getBoundingClientRect();
            show(mark, rect.right, rect.bottom);
        });
        mark.addEventListener('blur', hide);
    });
    chart.addEventListener('keydown', e => { if (e.key === 'Escape') hide(); });
    window.addEventListener('scroll', hide, true);
})();
