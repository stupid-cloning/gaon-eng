/* ㈜가온이엔지 공통 스크립트: 모바일 메뉴, 드롭다운, 탭, 메인 슬라이드, 스크롤 페이드인, 헤더 축소 */
(function () {
  document.documentElement.classList.add('js');

  /* ---- 모바일 메뉴 ---- */
  var t = document.getElementById('menuToggle'), n = document.getElementById('nav');
  if (t && n) {
    t.addEventListener('click', function () {
      var o = n.classList.toggle('open');
      t.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
    /* 모바일에서 대메뉴 터치 → 하위 메뉴 펼침 */
    n.querySelectorAll('.has-sub > a').forEach(function (a) {
      a.addEventListener('click', function (e) {
        if (window.matchMedia('(max-width: 900px)').matches) {
          e.preventDefault();
          a.parentElement.classList.toggle('open');
        }
      });
    });
  }

  /* ---- 헤더 축소 ---- */
  var h = document.getElementById('header');
  if (h) {
    var onScroll = function () { h.classList.toggle('scrolled', window.scrollY > 40); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- 탭 ---- */
  document.querySelectorAll('[data-tabs]').forEach(function (box) {
    var btns = box.querySelectorAll('[role="tab"]'), panels = box.querySelectorAll('[role="tabpanel"]');
    btns.forEach(function (b, i) {
      b.addEventListener('click', function () {
        btns.forEach(function (x, k) { x.setAttribute('aria-selected', k === i ? 'true' : 'false'); });
        panels.forEach(function (p, k) { p.hidden = k !== i; });
      });
    });
  });

  /* ---- 실적 필터 ---- */
  var f = document.getElementById('filters');
  if (f) {
    var rows = document.querySelectorAll('#ptable tbody tr');
    f.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      f.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var y = b.dataset.type;
      rows.forEach(function (r) { r.hidden = !(y === 'all' || r.dataset.type === y); });
    });
  }

  /* ---- 메인 비주얼 슬라이드 (사진 + 문구 + 버튼이 함께 바뀜) ---- */
  var sl = document.querySelector('[data-slider]');
  if (sl) {
    var imgs = sl.querySelectorAll('.hero-img'), copies = document.querySelectorAll('.slide-copy'),
        dots = document.querySelector('[data-dots]'), labels = ['지상형 발전소', '공공시설 · 지붕형', 'BIPV · 특수 유형'], cur = 0, timer;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var go = function (i) {
      i = (i + imgs.length) % imgs.length;
      imgs[cur].classList.remove('is-on'); copies[cur].classList.remove('is-on'); cur = i;
      imgs[cur].classList.add('is-on'); copies[cur].classList.add('is-on');
      if (dots) dots.querySelectorAll('button').forEach(function (d, k) { d.classList.toggle('on', k === cur); d.setAttribute('aria-selected', k === cur ? 'true' : 'false'); });
    };
    var restart = function () { clearInterval(timer); if (!reduce && imgs.length > 1) timer = setInterval(function () { go(cur + 1); }, 7000); };
    if (dots) imgs.forEach(function (_, k) {
      var d = document.createElement('button'); d.type = 'button'; d.setAttribute('role', 'tab');
      d.innerHTML = '<i>0' + (k + 1) + '</i>' + labels[k]; if (k === 0) d.className = 'on';
      d.addEventListener('click', function () { go(k); restart(); });
      dots.appendChild(d);
    });
    sl.parentElement.addEventListener('mouseenter', function () { clearInterval(timer); });
    sl.parentElement.addEventListener('mouseleave', restart);
    restart();
  }

  /* ---- 스크롤 페이드인 ---- */
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && els.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -10% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }
})();
