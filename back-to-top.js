(function () {
  var btn = document.getElementById('back-to-top');
  if (!btn) return;

  function toggle() {
    var y = window.pageYOffset || document.documentElement.scrollTop;
    if (y > 200) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }

  window.addEventListener('scroll', toggle, { passive: true });
  toggle();

  btn.addEventListener('click', function (e) {
    e.preventDefault();
    if ('scrollBehavior' in document.documentElement.style) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      window.scrollTo(0, 0);
    }
  });
})();
