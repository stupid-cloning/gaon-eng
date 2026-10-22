# -*- coding: utf-8 -*-
"""서브페이지 4개를 공통 틀(상단띠·헤더·CTA·푸터)로 생성한다. 실행: python3 build_sub.py"""
import html

HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} | ㈜가온이엔지</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap">
<link rel="stylesheet" href="style.css">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
<div class="topbar"><div class="wrap">
  <span>대표전화 <strong>000-0000-0000</strong> · 평일 09:00–18:00</span>
  <span class="r">강원특별자치도 원주시 서원대로 479-3</span>
</div></div>
<header class="header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="가온이엔지 홈">
    <span class="brand-mark" aria-hidden="true"></span>
    <span class="brand-text"><b>㈜가온이엔지</b><span>GAON ENG</span></span>
  </a>
  <button class="menu-toggle" id="menuToggle" aria-expanded="false" aria-controls="nav">메뉴</button>
  <nav class="nav" id="nav">
    <a href="about.html"{a1}>회사소개</a>
    <a href="business.html"{a2}>사업분야</a>
    <a href="projects.html"{a3}>시공실적</a>
    <a href="process.html"{a4}>사업절차</a>
    <a href="index.html#contact" class="btn btn-primary">문의하기</a>
  </nav>
</div></header>
<section class="subvisual">
  <img src="img/{visual}" alt="" width="1400" height="1050">
  <div class="wrap">
    <p class="crumb"><a href="index.html">HOME</a> &rsaquo; {title}</p>
    <h1>{title}</h1>
    <p>{lead}</p>
  </div>
</section>
{lnb}
<main class="wrap">
"""

FOOT = """</main>
<section class="cta" id="contact"><div class="wrap">
  <div>
    <p class="eyebrow" style="color:#8fb6ff">Contact</p>
    <h2>태양광 발전소 설계·시공, 입찰 참여 문의</h2>
    <p>사업 검토 단계의 간단한 상담부터 지명원·실적증명 자료 요청까지 전화 또는 이메일로 연락 주시면 담당자가 안내해 드립니다.</p>
  </div>
  <div class="contact-grid">
    <div><small>TEL</small><b>000-0000-0000</b></div>
    <div><small>FAX</small><b>000-0000-0000</b></div>
    <div class="full"><small>E-MAIL</small><b>info@gaoneng.co.kr</b></div>
    <div class="full"><small>ADDRESS</small><b style="font-size:1rem">강원특별자치도 원주시 서원대로 479-3</b></div>
  </div>
</div></section>
<footer class="footer"><div class="wrap">
  <div class="footer-top">
    <div class="brand"><span class="brand-mark" aria-hidden="true"></span><span class="brand-text"><b>㈜가온이엔지</b><span>GAON ENG</span></span></div>
    <div class="footer-links"><a href="about.html">회사소개</a><a href="business.html">사업분야</a><a href="projects.html">시공실적</a><a href="process.html">사업절차</a><a href="index.html#contact">문의하기</a></div>
  </div>
  <div class="footer-info">
    <span>주식회사 가온이엔지</span><span>대표 김현국</span><span>사업자등록번호 512-86-02034</span><span>강원특별자치도 원주시 서원대로 479-3</span><span>TEL 000-0000-0000</span>
  </div>
  <div>© 2026 GAON ENG Co., Ltd. All rights reserved.</div>
</div></footer>
<script>
(function(){
  var t=document.getElementById('menuToggle'),n=document.getElementById('nav');
  t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o?'true':'false')});
  n.addEventListener('click',function(e){if(e.target.tagName==='A'){n.classList.remove('open');t.setAttribute('aria-expanded','false')}});
  var ls=document.querySelectorAll('.lnb a');
  if(ls.length){var secs=[].map.call(ls,function(a){return document.querySelector(a.getAttribute('href'))});
    function upd(){var y=window.scrollY+200,i=0;secs.forEach(function(s,k){if(s&&s.offsetTop<=y)i=k});ls.forEach(function(a,k){a.classList.toggle('on',k===i)})}
    window.addEventListener('scroll',upd,{passive:true});upd()}
})();
</script>
</body>
</html>
"""

def lnb(items):
    return '<nav class="lnb" aria-label="하위 메뉴"><div class="wrap">' + ''.join(f'<a href="#{i}">{t}</a>' for i, t in items) + '</div></nav>'

BIZ = [('business-epc.html', '태양광 설계·시공'), ('business-electric.html', '전기·통신공사'),
       ('business-steel.html', '철강 구조물'), ('business-om.html', '유지관리·A/S')]

def subnav(cur):
    return '<nav class="subnav" aria-label="사업분야"><div class="wrap">' + ''.join(
        f'<a href="{f}"{" class=\"on\"" if f == cur else ""}>{t}</a>' for f, t in BIZ) + '</div></nav>'

def page(fn, idx, title, lead, visual, items, body, crumb=None):
    act = {k: (' class="on"' if k == idx else '') for k in (1, 2, 3, 4)}
    nav = subnav(fn) if fn.startswith('business-') else ''
    out = HEAD.format(title=title, lead=lead, visual=visual, lnb=nav,
                      a1=act[1], a2=act[2], a3=act[3], a4=act[4]) + body + FOOT
    if crumb:
        out = out.replace('<a href="index.html">HOME</a> &rsaquo; ' + title, '<a href="index.html">HOME</a> &rsaquo; ' + crumb + ' &rsaquo; ' + title)
    open(fn, 'w', encoding='utf-8').write(out)
    print(fn, len(out))

# ---------------- 시공실적 데이터 (지명원 시공 실적 리스트) ----------------
PROJECTS = [
    ("연천 선곡리 태양광발전소", 770, "2020.12.31", ""),
    ("화천 삼화진 태양광발전소", 648, "2021.04.30", ""),
    ("원주 법천리 태양광발전소", 597, "2021.09.30", ""),
    ("영월 영승태양광발전소", 99.5, "2021.10.10", ""),
    ("소상 태양광발전소", 300, "2021.10.31", ""),
    ("고흥 태양광발전소", 3000, "2021.12.31", ""),
    ("화천 연운태양광발전소", 1000, "2022.08.31", ""),
    ("원주 혁신센터", 315.4, "2022.10.25", ""),
    ("화천 제이에너지 태양광발전소", 437, "2022.12.31", ""),
    ("화천 위라리 태양광발전소", 989, "2022.12.31", ""),
    ("횡성 말구리썬일렉트릭 태양광발전소", 1000, "2023.02.28", ""),
    ("화천 강남 태양광발전소", 99.9, "2023.06.29", ""),
    ("음성 하이퍼윈도우", 234, "2023.11.30", ""),
    ("여주 다업햇빛두레 태양광발전소", 999.6, "2023.12.31", ""),
    ("가평 위곡 리파워링", 137, "2024.02.28", "리파워링"),
    ("여의도 사학재단", 418.9, "2024.08.23", "BIPV"),
    ("마곡 CP", 163.9, "2024.08.23", "BIPV"),
    ("인천북항산업단지 태양광발전소", 5212, "2024.12.29", ""),
]
total_kw = sum(p[1] for p in PROJECTS)

# ================= 1. 회사소개 =================
about_body = f"""
<section class="block" id="greeting">
  <div class="two">
    <div class="prose">
      <p class="eyebrow">CEO Message</p>
      <h2 class="sec-title">인사말</h2>
      <p class="quote" style="margin-top:1.4rem">항상 안전을 생각하고 가치를 더욱 높이는<br>신뢰받는 동반자가 되겠습니다.</p>
      <p>주식회사 가온이엔지는 2020년도에 설립되어 태양광 발전사업을 영위하고 있는 회사입니다.</p>
      <p>친환경 에너지를 추구하며, 현장 여건에 맞는 설계와 기술력을 바탕으로 태양광 공사를 만들어가고 있습니다.</p>
      <p>주식회사 가온이엔지에 많은 관심과 응원 부탁드리며, 최선을 다하여 고객 만족으로 보답 드리겠습니다. 감사합니다.</p>
      <p class="sign">주식회사 가온이엔지<b>대표이사 김현국</b></p>
    </div>
    <div class="photo"><img src="img/field2.jpg" alt="지상형 태양광발전소 시공 현장" loading="lazy"></div>
  </div>
</section>

<section class="block" id="overview">
  <div class="two">
    <div>
      <p class="eyebrow">Overview</p>
      <h2 class="sec-title">회사개요</h2>
      <p class="sec-lead">태양광 설계·시공, 전기·통신공사, 철강 구조물을 수행하는 전기공사업 등록 법인입니다.</p>
      <table class="overview">
        <tr><th>회사명</th><td>주식회사 가온이엔지 (GAON ENG Co., Ltd.)</td></tr>
        <tr><th>대표자</th><td>김현국</td></tr>
        <tr><th>설립일</th><td>2020년 9월 9일</td></tr>
        <tr><th>사업자등록번호</th><td>512-86-02034</td></tr>
        <tr><th>사업종류</th><td>태양광 / 전기·통신공사</td></tr>
        <tr><th>소재지</th><td>강원특별자치도 원주시 서원대로 479-3</td></tr>
      </table>
    </div>
    <ul class="strengths" aria-label="경쟁력" style="align-self:center">
      <li><i>1</i><div><b>신속하고 정확한 시공</b><span>공정을 줄여 공사비를 최소화합니다.</span></div></li>
      <li><i>2</i><div><b>숙련된 기술인력</b><span>타 업체보다 견고하고 안전한 공사를 수행합니다.</span></div></li>
      <li><i>3</i><div><b>다양한 현장 경험</b><span>예상 밖 현장 상황에도 노하우로 신속히 대처합니다.</span></div></li>
      <li><i>4</i><div><b>품질과 가격 경쟁력</b><span>최고 품질 자재를 경쟁력 있는 가격으로 설치·시공합니다.</span></div></li>
      <li><i>5</i><div><b>신속한 A/S</b><span>고객만족은 물론 최적의 발전효율을 유지합니다.</span></div></li>
    </ul>
  </div>
</section>

<section class="block" id="history">
  <div class="block-head">
    <p class="eyebrow">History</p>
    <h2 class="sec-title">연혁</h2>
    <p class="sec-lead">설립 이후 준공한 주요 현장입니다. 전체 목록은 시공실적 페이지에서 확인할 수 있습니다.</p>
  </div>
  <ul class="timeline">
    <li><b>2024</b><ul>
      <li>인천북항산업단지 태양광발전소 준공 <span>5,212kW · 최대 단일 사업</span></li>
      <li>여의도 사학재단 · 마곡 CP 건물일체형(BIPV) 준공 <span>418.9kW · 163.9kW</span></li>
      <li>가평 위곡 리파워링 공사 준공 <span>137kW</span></li>
    </ul></li>
    <li><b>2023</b><ul>
      <li>여주 다업햇빛두레 태양광발전소 준공 <span>999.6kW</span></li>
      <li>횡성 말구리썬일렉트릭 태양광발전소 준공 <span>1,000kW</span></li>
      <li>음성 하이퍼윈도우 · 화천 강남 태양광발전소 준공</li>
    </ul></li>
    <li><b>2022</b><ul>
      <li>화천 연운 · 위라리 · 제이에너지 태양광발전소 준공 <span>합계 2,426kW</span></li>
      <li>원주 혁신센터 지붕형 태양광 준공 <span>315.4kW</span></li>
    </ul></li>
    <li><b>2021</b><ul>
      <li>고흥 태양광발전소 준공 <span>3,000kW</span></li>
      <li>화천 삼화진 · 원주 법천리 · 소상 · 영월 영승 태양광발전소 준공</li>
    </ul></li>
    <li><b>2020</b><ul>
      <li>주식회사 가온이엔지 설립 <span>9월 9일 · 강원 원주</span></li>
      <li>연천 선곡리 태양광발전소 준공 <span>770kW · 첫 준공 현장</span></li>
    </ul></li>
  </ul>
</section>

<section class="block" id="license">
  <div class="block-head">
    <p class="eyebrow">License &amp; Certification</p>
    <h2 class="sec-title">보유 면허·등록</h2>
    <p class="sec-lead">입찰 참가 및 계약에 필요한 등록·면허 서류는 요청 시 사본으로 제공합니다.</p>
  </div>
  <div class="cert">
    <div class="cert-card"><small>등록</small><b>전기공사업 등록</b><span>전기공사업법에 따른 전기공사업 등록 (등록번호 확인 중)</span></div>
    <div class="cert-card"><small>법인</small><b>법인 사업자등록</b><span>사업자등록번호 512-86-02034 · 2020년 9월 설립 법인</span></div>
    <div class="cert-card"><small>서류</small><b>지명원 · 실적증명</b><span>공사지명원, 법인 등기부등본, 인감증명서 등 입찰 서류 구비</span></div>
  </div>
</section>

<section class="block" id="location">
  <div class="block-head">
    <p class="eyebrow">Location</p>
    <h2 class="sec-title">오시는 길</h2>
  </div>
  <div class="map-box">
    <ul class="info-list">
      <li><span>주소</span><span>강원특별자치도 원주시 서원대로 479-3</span></li>
      <li><span>대표전화</span><span>000-0000-0000</span></li>
      <li><span>팩스</span><span>000-0000-0000</span></li>
      <li><span>이메일</span><span>info@gaoneng.co.kr</span></li>
      <li><span>업무시간</span><span>평일 09:00–18:00 (주말·공휴일 휴무)</span></li>
    </ul>
    <div>
      <div class="map-frame"><iframe title="오시는 길 지도" src="https://www.google.com/maps?q=%EA%B0%95%EC%9B%90%ED%8A%B9%EB%B3%84%EC%9E%90%EC%B9%98%EB%8F%84%20%EC%9B%90%EC%A3%BC%EC%8B%9C%20%EC%84%9C%EC%9B%90%EB%8C%80%EB%A1%9C%20479-3&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
      <p class="map-links"><a class="btn btn-outline" href="https://map.naver.com/p/search/%EA%B0%95%EC%9B%90%ED%8A%B9%EB%B3%84%EC%9E%90%EC%B9%98%EB%8F%84%20%EC%9B%90%EC%A3%BC%EC%8B%9C%20%EC%84%9C%EC%9B%90%EB%8C%80%EB%A1%9C%20479-3" target="_blank" rel="noopener">네이버 지도</a> <a class="btn btn-outline" href="https://map.kakao.com/link/search/%EA%B0%95%EC%9B%90%ED%8A%B9%EB%B3%84%EC%9E%90%EC%B9%98%EB%8F%84%20%EC%9B%90%EC%A3%BC%EC%8B%9C%20%EC%84%9C%EC%9B%90%EB%8C%80%EB%A1%9C%20479-3" target="_blank" rel="noopener">카카오맵</a></p>
    </div>
  </div>
</section>
"""
page('about.html', 1, '회사소개', '안전을 최우선으로, 현장 여건에 맞는 설계와 기술력으로 신뢰를 쌓아갑니다.', 'sub.jpg',
     None, about_body)

# ================= 2. 사업분야 (허브 + 상세 4페이지) =================
business_body = """
<section class="block">
  <div class="block-head">
    <p class="eyebrow">Business Areas</p>
    <h2 class="sec-title">네 가지 사업분야</h2>
    <p class="sec-lead">태양광 설계·시공, 전기·통신공사, 철강 구조물, 유지관리. 각 분야의 절차와 기준은 상세 페이지에서 확인할 수 있습니다.</p>
  </div>
  <div class="hub">
    <article class="proj"><div class="ph"><img src="img/goheung.jpg" alt="" loading="lazy"></div>
      <div class="proj-body"><h3>태양광 설계·시공</h3><p>현장조사와 발전량 검토에서 시작해 배치·구조·전기 설계, 인허가 도면, 시공과 준공 검사까지 발전소 건설 전 과정을 수행합니다.</p><a class="more" href="business-epc.html">설계·시공 절차 보기 →</a></div></article>
    <article class="proj"><div class="ph"><img src="img/wonju.jpg" alt="" loading="lazy"></div>
      <div class="proj-body"><h3>전기·통신공사</h3><p>접속함·인버터·수배전 설비, 한전 계통연계와 사용 전 검사까지, 전기설비 규정에 따라 안전하게 시공합니다.</p><a class="more" href="business-electric.html">계통연계 절차 보기 →</a></div></article>
    <article class="proj"><div class="ph"><img src="img/chungju.jpg" alt="" loading="lazy"></div>
      <div class="proj-body"><h3>철강 구조물</h3><p>아연도금·포스맥 등 내식성 소재의 구조물을 제작하고, 숙련 인력이 신속하고 정확하게 구조물 공사를 수행합니다.</p><a class="more" href="business-steel.html">소재와 설계 기준 보기 →</a></div></article>
    <article class="proj"><div class="ph"><img src="img/mungyeong.jpg" alt="" loading="lazy"></div>
      <div class="proj-body"><h3>유지관리 · A/S</h3><p>신속한 A/S 대응으로 최적의 발전효율을 유지합니다. 노후 발전소의 모듈·인버터를 교체하는 리파워링 실적이 있습니다.</p><a class="more" href="business-om.html">점검 항목 보기 →</a></div></article>
  </div>
</section>
"""
page('business.html', 2, '사업분야', '설계부터 전기·구조물·유지관리까지, 태양광 발전설비에 필요한 공종을 한 회사에서 수행합니다.', 'hero.jpg', None, business_body)

# ---- 2-1 태양광 설계·시공 ----
epc_body = """
<section class="block">
  <div class="two">
    <div class="prose">
      <p class="eyebrow">Overview</p>
      <h2 class="sec-title">설계가 발전소의 수익을 정합니다</h2>
      <p>태양광 발전소의 수익은 설계 단계에서 대부분 결정됩니다. 같은 부지라도 경사각·방위각·어레이 간격에 따라 연간 발전량이 달라지고, 구조물 형식과 계통연계 방식에 따라 공사비가 달라집니다. 설계와 시공을 한 회사가 맡으면 설계에서 정한 조건이 현장에서 그대로 구현되고, 현장 조건이 바뀔 때(지반 상태, 지붕 구조, 한전 선로 여유 등) 설계 수정이 바로 공정에 반영됩니다.</p>
      <p>가온이엔지는 현장 여건에 맞는 설계와 기술력을 바탕으로 태양광 설계·시공을 수행하는 전문기업입니다.</p>
    </div>
    <div class="photo"><img src="img/goheung.jpg" alt="지상형 태양광발전소 시공 현장" loading="lazy"></div>
  </div>
</section>

<section class="block">
  <div class="block-head">
    <p class="eyebrow">Design Process</p>
    <h2 class="sec-title">설계 절차</h2>
  </div>
  <ol class="flow">
    <li><div><b>현장조사</b><span>부지 경계·경사·지반, 지붕형은 지붕 구조와 노후도, 주변 건물·수목에 의한 음영, 인근 한전 선로의 연계 여유 용량을 확인합니다.</span></div></li>
    <li><div><b>발전량 검토</b><span>지역 일사량 데이터를 기반으로 경사각·방위각을 조정하며 연간 발전량을 시뮬레이션하고, 음영 손실과 계통 제약을 반영한 설치 용량을 결정합니다.</span></div></li>
    <li><div><b>배치 · 구조 설계</b><span>어레이 간격(동지 기준 음영 회피)과 구조물 형식을 정하고, 풍하중·적설하중을 검토해 기초 형식을 결정합니다.</span></div></li>
    <li><div><b>전기 설계</b><span>모듈 스트링 구성, 인버터 용량과 대수, 접속함·수배전반 구성을 단선도로 작성하고 케이블 굵기와 보호장치를 산정합니다.</span></div></li>
    <li><div><b>인허가 도면</b><span>발전사업허가, 개발행위허가, 사용 전 검사에 필요한 도면과 계산서를 작성해 기관 제출을 지원합니다.</span></div></li>
  </ol>
</section>

<section class="block">
  <div class="block-head">
    <p class="eyebrow">Construction</p>
    <h2 class="sec-title">시공 공정</h2>
    <p class="sec-lead">태양광 발전소 시공은 다섯 공종으로 진행됩니다. 가온이엔지의 역무범위입니다.</p>
  </div>
  <div class="process" style="margin-top:0">
    <div class="step"><h3>토목공사</h3><p>경사·레벨 측정 장비로 부지를 정지하고 기초를 시공합니다.</p></div>
    <div class="step"><h3>구조물 제작</h3><p>아연도금·포스맥 등 내식성 소재로 구조물을 제작합니다.</p></div>
    <div class="step"><h3>구조물 공사</h3><p>숙련 인력이 구조물을 설치하고 모듈을 고정합니다.</p></div>
    <div class="step"><h3>전기공사</h3><p>전기설비 규정에 따라 접속함·인버터·수배전 설비를 시공합니다.</p></div>
    <div class="step"><h3>계통연계 · 시운전</h3><p>한전 고압케이블을 연결하고 사용 전 검사 후 시운전합니다.</p></div>
  </div>
</section>

<section class="block">
  <div class="block-head">
    <p class="eyebrow">Types</p>
    <h2 class="sec-title">설치 유형별 시공 포인트</h2>
    <p class="sec-lead">태양광 발전소는 설치 장소에 따라 네 유형으로 나뉘고, 유형마다 설계와 시공에서 챙겨야 할 점이 다릅니다.</p>
  </div>
  <div class="types">
    <article class="type"><div class="photo"><img src="img/yeoju.jpg" alt="" loading="lazy"></div><div class="type-body">
      <h3>지상형 (토지)</h3><p>부지 경사와 지반 조건에 맞는 기초 선정이 핵심입니다. 배수 계획이 없으면 우기에 기초 세굴이 생깁니다.</p>
      <ul><li>콘크리트 독립기초 또는 스파이럴 파일 기초</li><li>어레이 간격은 동지 기준 음영으로 결정</li><li>준공 실적: 고흥 3,000kW · 인천북항 5,212kW 등</li></ul></div></article>
    <article class="type"><div class="photo"><img src="img/wonju.jpg" alt="" loading="lazy"></div><div class="type-body">
      <h3>지붕형 (공장·건물)</h3><p>지붕 구조의 하중 여유와 방수가 핵심입니다. 지붕 재질(판넬·슬레이트·콘크리트)에 따라 고정 방식이 달라집니다.</p>
      <ul><li>구조 안전성 검토 후 클램프·앵커 방식 선정</li><li>관통부 방수와 지붕 보수 범위 사전 합의</li><li>준공 실적: 원주 혁신센터 315.4kW · 음성 하이퍼윈도우 234kW</li></ul></div></article>
    <article class="type"><div class="photo"><img src="img/boryeong.jpg" alt="" loading="lazy"></div><div class="type-body">
      <h3>수상형 (저수지·담수)</h3><p>부력체와 계류(앵커) 설계가 핵심입니다. 수위 변동과 풍파를 견디면서 어레이 간격을 유지해야 합니다.</p>
      <ul><li>내식성 소재와 부력체 내구성 검토</li><li>수위 변동 범위에 맞춘 계류 설계</li><li>육상 수전설비까지 케이블 경로 확보</li><li>시공 사진: 보령화력 수상태양광</li></ul></div></article>
    <article class="type"><div class="photo"><img src="img/yeouido.jpg" alt="" loading="lazy"></div><div class="type-body">
      <h3>건물일체형 (BIPV)</h3><p>모듈이 외장재를 겸하므로 건축 설계 단계부터 협업합니다. 수직면 설치라 발전량보다 외관·방수·안전이 우선 검토 대상입니다.</p>
      <ul><li>커튼월·외장 시공사와 공정 조율</li><li>수직 설치 조건의 발전량 검토</li><li>준공 실적: 여의도 사학재단 418.9kW · 마곡 CP 163.9kW</li></ul></div></article>
  </div>
  <p style="margin-top:2rem"><a class="btn btn-outline" href="projects.html">시공실적 전체 보기</a></p>
</section>
"""
page('business-epc.html', 2, '태양광 설계·시공', '현장조사부터 준공 검사까지, 발전소 건설 전 과정을 한 팀이 수행합니다.', 'goheung.jpg', None, epc_body, crumb='사업분야')

# ---- 2-2 전기·통신공사 ----
electric_body = """
<section class="block">
  <div class="two">
    <div class="prose">
      <p class="eyebrow">Overview</p>
      <h2 class="sec-title">모듈에서 한전 계통까지</h2>
      <p>태양광 발전소에서 전기공사는 모듈에서 생산한 직류를 교류로 바꿔 한전 계통까지 보내는 모든 설비를 다룹니다. 접속함·인버터·수배전반·케이블·접지·보호장치가 여기에 포함되며, 전기사업법과 한국전기설비규정(KEC)을 따라야 하고 전기공사업 등록 업체만 시공할 수 있습니다.</p>
      <p>가온이엔지는 전기공사업 등록 기업으로, 전기설비 규정에 따른 설계·시공과 한전과의 고압케이블 연결 및 시운전을 수행합니다.</p>
    </div>
    <div class="photo"><img src="img/wonju.jpg" alt="지붕형 태양광 전기설비" loading="lazy"></div>
  </div>
</section>

<section class="block">
  <div class="block-head">
    <p class="eyebrow">Grid Connection</p>
    <h2 class="sec-title">계통연계 절차</h2>
  </div>
  <ol class="flow">
    <li><div><b>한전 연계 협의</b><span>설치 용량과 연계 지점을 한전에 신청해 선로 여유 용량과 연계 방식을 확정합니다. 선로 여유가 없으면 용량 조정이나 선로 보강이 필요합니다.</span></div></li>
    <li><div><b>수전·수배전 설비</b><span>일반적으로 100kW 미만은 저압(380V) 연계, 그 이상은 특고압(22.9kV) 연계로 변압기·차단기(VCB)를 갖춘 수전설비가 필요합니다. 최종 방식은 한전 협의로 결정됩니다.</span></div></li>
    <li><div><b>케이블 포설 · 접지</b><span>직류·교류 케이블을 전압강하 기준 이내로 산정해 포설하고, 구조물·설비 접지와 피뢰 설비를 시공합니다.</span></div></li>
    <li><div><b>사용 전 검사</b><span>한국전기안전공사가 절연·접지·보호장치 동작을 검사합니다. 합격 후 한전과 계통연계 일정을 잡습니다.</span></div></li>
    <li><div><b>계통연계 · 시운전</b><span>한전 고압케이블을 연결하고 인버터를 계통에 동기화해 발전을 시작합니다. 초기 발전 데이터로 설계 발전량과 비교 검증합니다.</span></div></li>
  </ol>
</section>

<section class="block">
  <div class="two">
    <div>
      <p class="eyebrow">Scope</p>
      <h2 class="sec-title">태양광 전기공사의 구성</h2>
      <ul class="checks">
        <li>접속함 · 인버터 설치, 직류/교류 배선</li>
        <li>수배전반 · 변압기 · 차단기 등 수전설비</li>
        <li>접지 · 피뢰 · 서지 보호 설비</li>
        <li>한전 계통연계 고압케이블 공사</li>
        <li>발전 모니터링 · 통신설비</li>
        <li>사용 전 검사 및 정기검사 대응</li>
      </ul>
    </div>
    <div>
      <p class="eyebrow">Monitoring</p>
      <h2 class="sec-title">발전 모니터링</h2>
      <p class="sec-lead">인버터별 발전량·전압·전류를 통신설비로 수집해 원격에서 확인하는 설비입니다. 고장이나 발전량 저하를 조기에 발견하는 유지관리의 출발점입니다.</p>
      <p class="note">모니터링 시스템 구성은 발전소 규모와 발주처 요구(RTU 연동, 전력거래소 계량 등)에 따라 달라집니다.</p>
    </div>
  </div>
</section>
"""
page('business-electric.html', 2, '전기·통신공사', '모듈에서 생산한 전기가 한전 계통에 연결되기까지의 설비와 절차를 안내합니다.', 'wonju.jpg', None, electric_body, crumb='사업분야')

# ---- 2-3 철강 구조물 ----
steel_body = """
<section class="block">
  <div class="two">
    <div class="prose">
      <p class="eyebrow">Overview</p>
      <h2 class="sec-title">구조물이 발전소의 수명을 정합니다</h2>
      <p>태양광 모듈의 설계 수명은 25년 이상입니다. 그 기간 동안 모듈을 바람·눈·부식으로부터 지탱하는 것이 구조물입니다. 구조물이 부식되거나 볼트가 풀리면 모듈이 멀쩡해도 발전소를 세워야 합니다. 그래서 구조물은 소재 선택과 하중 설계가 시공 품질 자체입니다.</p>
      <p>가온이엔지는 아연도금 및 포스맥 등 경쟁력 있는 소재의 구조물을 사용해 제작하고, 숙련된 인력을 투입해 신속하고 정확하게 구조물 공사를 수행합니다.</p>
    </div>
    <div class="photo"><img src="img/chungju.jpg" alt="지붕형 태양광 구조물" loading="lazy"></div>
  </div>
</section>

<section class="block">
  <div class="block-head">
    <p class="eyebrow">Materials</p>
    <h2 class="sec-title">구조물 소재</h2>
  </div>
  <div class="table-wrap">
  <table class="spec">
    <thead><tr><th>소재</th><th>특징</th><th>주로 쓰는 곳</th></tr></thead>
    <tbody>
      <tr><th>용융아연도금 강재</th><td>강재 표면에 아연을 입혀 부식을 막는 가장 일반적인 방식. 비용 효율이 높고 강성이 좋으나, 절단·용접부의 도금 손상에 주의해야 합니다.</td><td>지상형 기둥·보, 대규모 발전소</td></tr>
      <tr><th>포스맥 (PosMAC)</th><td>아연·마그네슘·알루미늄 합금 도금 강판. 일반 아연도금보다 내식성이 크게 높고 절단면 자가 보호 성능이 있어 해안·고습 지역에 유리합니다.</td><td>해안·수상 인접 부지, 퍼린·레일 부재</td></tr>
      <tr><th>알루미늄</th><td>가볍고 녹이 슬지 않아 지붕 하중 여유가 적을 때 유리하나 강재보다 비용이 높습니다.</td><td>지붕형 레일·클램프</td></tr>
    </tbody>
  </table>
  </div>
</section>

<section class="block">
  <div class="two">
    <div>
      <p class="eyebrow">Design Criteria</p>
      <h2 class="sec-title">구조물 설계 기준</h2>
      <ul class="checks">
        <li>풍하중 · 적설하중: 건축구조기준(KDS)의 지역별 기본풍속과 기본적설하중 적용</li>
        <li>지상형 기초: 지반 조사 결과에 따라 콘크리트 독립기초 또는 스파이럴 파일 선정</li>
        <li>지붕형: 기존 지붕 구조의 허용 하중 검토 후 설치 용량과 고정 방식 결정</li>
        <li>수상형: 부력체 내구성, 수위 변동 범위, 계류 하중 검토</li>
        <li>볼트 체결 토크 관리와 준공 후 점검 기준</li>
      </ul>
    </div>
    <div class="photo"><img src="img/field2.jpg" alt="지상형 태양광 구조물" loading="lazy"></div>
  </div>
</section>
"""
page('business-steel.html', 2, '철강 구조물', '태양광 구조물의 소재와 설계 기준, 설치 유형별 구조물 방식을 안내합니다.', 'chungju.jpg', None, steel_body, crumb='사업분야')

# ---- 2-4 유지관리 ----
om_body = """
<section class="block">
  <div class="two">
    <div class="prose">
      <p class="eyebrow">Overview</p>
      <h2 class="sec-title">발전량은 관리하는 만큼 나옵니다</h2>
      <p>준공 직후의 발전량이 25년 동안 유지되지는 않습니다. 모듈 표면 오염, 주변 수목 성장으로 인한 음영, 인버터 고장, 접속함 발열, 구조물 볼트 풀림이 조금씩 발전량을 깎습니다. 인버터 한 대가 멈춘 것을 한 달 뒤에 발견하면 그 달 수익의 상당 부분이 사라집니다.</p>
      <p>가온이엔지는 A/S에 신속하게 대응해 고객만족은 물론 최적의 발전효율을 유지합니다.</p>
    </div>
    <div class="photo"><img src="img/mungyeong.jpg" alt="태양광발전소 유지관리" loading="lazy"></div>
  </div>
</section>

<section class="block">
  <div class="block-head">
    <p class="eyebrow">Inspection</p>
    <h2 class="sec-title">정기점검 항목</h2>
  </div>
  <div class="table-wrap">
  <table class="spec">
    <thead><tr><th>구분</th><th>점검 내용</th><th>일반적인 점검 방법</th></tr></thead>
    <tbody>
      <tr><th>모듈</th><td>표면 오염 · 파손 · 변색, 핫스팟(국부 과열), 정션박스 상태</td><td>육안, 열화상 카메라, 스트링별 전압·전류 측정</td></tr>
      <tr><th>구조물</th><td>볼트 풀림 · 부식 · 변형, 기초 침하 · 세굴, 지붕형 고정부 누수</td><td>육안, 토크 점검</td></tr>
      <tr><th>접속함 · 인버터</th><td>단자 발열, 퓨즈 · 서지보호기 상태, 인버터 효율 · 경보 이력, 냉각팬 · 필터</td><td>열화상, 인버터 로그 분석</td></tr>
      <tr><th>전기설비</th><td>절연저항, 접지저항, 차단기 · 계전기 동작, 케이블 피복 상태</td><td>절연저항계, 접지저항계</td></tr>
      <tr><th>발전 데이터</th><td>인버터별 · 스트링별 발전량 편차, 설계 발전량 대비 실적</td><td>모니터링 데이터 분석</td></tr>
    </tbody>
  </table>
  </div>
  <p class="note">점검 주기는 발전소 규모와 계약 조건에 따라 정해지며, 전기안전관리법에 따른 정기검사가 별도로 있습니다.</p>
</section>

<section class="block">
  <div class="two">
    <div>
      <p class="eyebrow">A/S</p>
      <h2 class="sec-title">일반적인 고장 대응 절차</h2>
      <ol class="flow">
        <li><div><b>접수</b><span>전화 · 모니터링 경보로 이상 접수</span></div></li>
        <li><div><b>원격 진단</b><span>모니터링 데이터로 고장 범위(인버터 · 스트링 · 계통) 1차 판단</span></div></li>
        <li><div><b>현장 조치</b><span>부품 교체 · 재결선 · 설정 변경 등 조치 후 발전 재개 확인</span></div></li>
        <li><div><b>보고</b><span>원인 · 조치 내용 · 재발 방지 방안 보고</span></div></li>
      </ol>
    </div>
    <div>
      <p class="eyebrow">Repowering</p>
      <h2 class="sec-title">리파워링</h2>
      <p class="sec-lead">10년 이상 된 발전소는 모듈 효율 저하와 인버터 노후로 발전량이 눈에 띄게 줄어듭니다. 구조물과 계통연계 설비는 그대로 두고 모듈·인버터만 최신 제품으로 교체하면, 같은 부지에서 설치 용량과 발전량을 늘릴 수 있습니다.</p>
      <ul class="checks">
        <li>기존 구조물의 하중 여유와 부식 상태 검토</li>
        <li>신규 모듈 규격에 맞는 구조물 보강 · 스트링 재구성</li>
        <li>용량 변경 시 인허가 변경 필요</li>
        <li>준공 실적: 가평 위곡 리파워링 137kW (2024)</li>
      </ul>
    </div>
  </div>
</section>
"""
page('business-om.html', 2, '유지관리 · A/S', '발전효율을 유지하는 정기점검 항목과 고장 대응, 노후 발전소 리파워링을 안내합니다.', 'mungyeong.jpg', None, om_body, crumb='사업분야')

# ================= 3. 시공실적 =================
rows = []
for i, (name, kw, date, note) in enumerate(sorted(PROJECTS, key=lambda p: p[2], reverse=True), 1):
    yr = date[:4]
    kw_s = f"{kw:,.1f}".rstrip('0').rstrip('.') if kw != int(kw) else f"{int(kw):,}"
    rows.append(f'<tr data-year="{yr}"><td class="c">{len(PROJECTS)-i+1}</td><td>{html.escape(name)}</td><td class="num">{kw_s}</td><td class="c">{date}</td><td class="c">{note}</td></tr>')
years = sorted({p[2][:4] for p in PROJECTS}, reverse=True)
filters = '<button type="button" data-year="all" aria-pressed="true">전체</button>' + ''.join(f'<button type="button" data-year="{y}" aria-pressed="false">{y}</button>' for y in years)

projects_body = f"""
<section class="block" id="list">
  <div class="summary">
    <div><b>{len(PROJECTS)}<small>건</small></b><span>준공 실적 (2020–2024)</span></div>
    <div><b>{total_kw/1000:.1f}<small>MW</small></b><span>누적 시공 용량</span></div>
    <div><b>5,212<small>kW</small></b><span>최대 단일 사업 (인천북항)</span></div>
    <div><b>2<small>건</small></b><span>건물일체형 BIPV</span></div>
  </div>
  <div class="block-head" style="margin-bottom:1.2rem">
    <p class="eyebrow">Project List</p>
    <h2 class="sec-title">시공 실적 목록</h2>
  </div>
  <div class="filters" id="filters">{filters}</div>
  <div class="table-wrap">
    <table class="ptable" id="ptable">
      <thead><tr><th style="width:4em;text-align:center">연번</th><th>프로젝트명</th><th style="text-align:right">용량 (kW)</th><th style="text-align:center">준공일</th><th style="text-align:center">비고</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table>
  </div>
  <p class="note">실적증명서·준공 서류는 입찰 참가 시 요청에 따라 제공합니다.</p>
</section>

<section class="block" id="gallery">
  <div class="block-head">
    <p class="eyebrow">Site Photos</p>
    <h2 class="sec-title">시공 현장</h2>
  </div>
  <div class="gallery">
    <figure><div class="photo"><img src="img/goheung.jpg" alt="" loading="lazy"></div><figcaption><b>고흥 태양광발전소</b>3,000kW · 지상형</figcaption></figure>
    <figure><div class="photo"><img src="img/yeouido.jpg" alt="" loading="lazy"></div><figcaption><b>여의도 사학재단</b>418.9kW · BIPV</figcaption></figure>
    <figure><div class="photo"><img src="img/magok.jpg" alt="" loading="lazy"></div><figcaption><b>마곡 CP</b>163.9kW · BIPV</figcaption></figure>
    <figure><div class="photo"><img src="img/wonju.jpg" alt="" loading="lazy"></div><figcaption><b>원주 혁신센터</b>315.4kW · 지붕형</figcaption></figure>
    <figure><div class="photo"><img src="img/yeoju.jpg" alt="" loading="lazy"></div><figcaption><b>여주 다업햇빛두레</b>999.6kW · 지상형</figcaption></figure>
    <figure><div class="photo"><img src="img/mungyeong.jpg" alt="" loading="lazy"></div><figcaption><b>문경 서일태양광</b>1,000kW · 지상형</figcaption></figure>
    <figure><div class="photo"><img src="img/chungju.jpg" alt="" loading="lazy"></div><figcaption><b>충주 세아특수강</b>2,400kW · 지붕형</figcaption></figure>
    <figure><div class="photo"><img src="img/boryeong.jpg" alt="" loading="lazy"></div><figcaption><b>보령화력 수상태양광</b>1,200kW · 수상형</figcaption></figure>
    <figure><div class="photo"><img src="img/field2.jpg" alt="" loading="lazy"></div><figcaption><b>여주 썬발전협동조합</b>지상형</figcaption></figure>
  </div>
</section>
<script>
(function(){{
  var f=document.getElementById('filters'),rows=document.querySelectorAll('#ptable tbody tr');
  f.addEventListener('click',function(e){{var b=e.target.closest('button');if(!b)return;
    f.querySelectorAll('button').forEach(function(x){{x.setAttribute('aria-pressed',x===b?'true':'false')}});
    var y=b.dataset.year;rows.forEach(function(r){{r.hidden=!(y==='all'||r.dataset.year===y)}})}});
}})();
</script>
"""
page('projects.html', 3, '시공실적', f'99.5kW 소규모 발전소부터 5MW급 산업단지 발전소, 건물일체형(BIPV)까지 {len(PROJECTS)}개 현장을 준공했습니다.', 'goheung.jpg',
     None, projects_body)

# ================= 4. 사업절차 =================
process_body = """
<section class="block" id="procedure">
  <div class="two">
    <div>
      <p class="eyebrow">Procedure</p>
      <h2 class="sec-title">태양광 발전사업 진행절차</h2>
      <p class="sec-lead">발전사업 허가부터 공급인증서(REC) 거래까지, 발전소 한 곳이 수익을 내기까지 거치는 열 단계입니다. 가온이엔지는 허가·검사 단계의 서류 준비와 기관 대응을 함께 지원합니다.</p>
      <table class="overview" aria-label="발전사업 허가 기관">
        <tr><th>3MW 초과</th><td>산업통상부</td></tr>
        <tr><th>200kW 초과 ~ 3MW 이하</th><td>도청 (광역자치단체)</td></tr>
        <tr><th>200kW 이하</th><td>시·군·구청</td></tr>
      </table>
      <p class="note">허가 기관은 설비 용량 기준으로 나뉩니다. 전기사업법상 발전사업 허가 기준.</p>
    </div>
    <ol class="flow">
      <li><div><b>발전사업 허가</b><span>용량에 따라 산업통상부 · 도청 · 시군구청에 신청. 사업계획서, 부지 사용권 증빙, 계통연계 검토 결과 등을 첨부하며, 부지 조건에 따라 개발행위허가·산지/농지 전용이 별도로 필요합니다.</span></div></li>
      <li><div><b>발전소 건설</b><span>전기사업법에 따라 자기자본으로 상업발전소 건설 (정부지원금 없음). 토목 → 구조물 → 모듈·전기 → 계통연계 순으로 진행합니다.</span></div></li>
      <li><div><b>사용 전 검사</b><span>한국전기안전공사가 설비의 안전성을 검사. 합격 후에만 계통에 연결할 수 있습니다.</span></div></li>
      <li><div><b>전력수급 계약 체결</b><span>한국전력공사(PPA) 또는 전력거래소(시장 거래)와 계약. 소규모 발전소는 대부분 한전 PPA를 선택합니다.</span></div></li>
      <li><div><b>사업개시 신고</b><span>사업개시 신고 수리</span></div></li>
      <li><div><b>설비확인</b><span>한국에너지공단에 설비확인 신청</span></div></li>
      <li><div><b>전력공급</b><span>한국전력공사 또는 전력거래소로 발전 전력 공급</span></div></li>
      <li><div><b>공급인증서(REC) 발급</b><span>공급 전력량에 대해 인증서 발급, 발급 수수료 납부</span></div></li>
      <li><div><b>거래시스템 등록 및 매매</b><span>인증서를 거래시스템에 등록, 구매자와 가격 합의 시 매매 체결</span></div></li>
      <li><div><b>이행신고</b><span>공급의무자가 인증서를 정부에 제출해 의무 이행</span></div></li>
    </ol>
  </div>
</section>
"""
page('process.html', 4, '사업절차', '태양광 발전소가 허가부터 수익 발생까지 거치는 열 단계를 안내합니다.', 'field2.jpg', None, process_body)
