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

def page(fn, idx, title, lead, visual, items, body):
    act = {k: (' class="on"' if k == idx else '') for k in (1, 2, 3, 4)}
    out = HEAD.format(title=title, lead=lead, visual=visual, lnb=lnb(items) if items else '',
                      a1=act[1], a2=act[2], a3=act[3], a4=act[4]) + body + FOOT
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
     [('greeting', '인사말'), ('overview', '회사개요'), ('history', '연혁'), ('license', '보유 면허'), ('location', '오시는 길')], about_body)

# ================= 2. 사업분야 =================
business_body = """
<section class="block" id="epc">
  <div class="biz-detail">
    <div>
      <p class="eyebrow">01 · Design &amp; Construction</p>
      <h2 class="sec-title">태양광 설계·시공</h2>
      <p class="sec-lead">현장조사와 발전량 검토부터 구조물·모듈·인버터 설치, 준공 검사까지 발전소 건설 전 과정을 수행합니다. 설계와 시공을 한 회사가 맡아 현장 변경에 즉시 대응합니다.</p>
      <ul class="checks">
        <li>현장조사 · 음영 분석 · 발전량 검토 · 배치 설계</li>
        <li>토목공사 (경사·레벨 측정, 부지 정지, 기초)</li>
        <li>구조물 설치 · 모듈 · 인버터 · 접속함 시공</li>
        <li>사용 전 검사 대응 및 준공</li>
      </ul>
      <div class="chips"><span class="chip">지상형</span><span class="chip">지붕형</span><span class="chip">수상형</span><span class="chip">건물일체형 BIPV</span><span class="chip">리파워링</span></div>
    </div>
    <div class="photo"><img src="img/goheung.jpg" alt="지상형 태양광발전소" loading="lazy"></div>
  </div>
</section>

<section class="block" id="electric">
  <div class="biz-detail">
    <div>
      <p class="eyebrow">02 · Electrical &amp; Telecom</p>
      <h2 class="sec-title">전기·통신공사</h2>
      <p class="sec-lead">전기공사업 등록 기업으로서 전기설비 규정에 따라 수배전 설비와 계통연계를 직접 시공합니다. 외주 없이 자체 인력이 수행해 공정 지연과 책임 공백을 줄입니다.</p>
      <ul class="checks">
        <li>수배전반 · 저압/고압 전기설비 시공</li>
        <li>한전 고압케이블 연결 및 계통연계</li>
        <li>시운전 · 사용 전 검사 (한국전기안전공사)</li>
        <li>모니터링 · 통신설비 구성</li>
      </ul>
    </div>
    <div class="photo"><img src="img/wonju.jpg" alt="지붕형 태양광 전기설비" loading="lazy"></div>
  </div>
</section>

<section class="block" id="steel">
  <div class="biz-detail">
    <div>
      <p class="eyebrow">03 · Steel Structure</p>
      <h2 class="sec-title">철강 구조물</h2>
      <p class="sec-lead">아연도금·포스맥(PosMAC) 등 내식성 소재로 태양광 구조물을 직접 제작·시공합니다. 지붕 형태와 지반 조건에 맞춘 구조물로 장기 안전성을 확보합니다.</p>
      <ul class="checks">
        <li>지상형 · 지붕형 · 수상형 구조물 설계 및 제작</li>
        <li>아연도금 · 포스맥 소재 적용</li>
        <li>숙련 인력 투입으로 신속하고 정확한 구조물 공사</li>
      </ul>
    </div>
    <div class="photo"><img src="img/chungju.jpg" alt="지붕형 태양광 구조물" loading="lazy"></div>
  </div>
</section>

<section class="block" id="om">
  <div class="biz-detail">
    <div>
      <p class="eyebrow">04 · Operation &amp; Maintenance</p>
      <h2 class="sec-title">유지관리 · A/S</h2>
      <p class="sec-lead">준공 후 정기점검과 신속한 A/S로 발전효율을 유지합니다. 수명이 다한 발전소의 모듈·인버터 교체(리파워링) 공사도 수행합니다.</p>
      <ul class="checks">
        <li>정기점검 · 발전량 모니터링</li>
        <li>고장 대응 및 부품 교체</li>
        <li>리파워링 (모듈·인버터 교체) 공사</li>
      </ul>
    </div>
    <div class="photo"><img src="img/mungyeong.jpg" alt="태양광발전소 유지관리" loading="lazy"></div>
  </div>
</section>
"""
page('business.html', 2, '사업분야', '설계부터 전기·구조물·유지관리까지, 태양광 발전설비에 필요한 공종을 한 회사에서 수행합니다.', 'hero.jpg',
     [('epc', '태양광 설계·시공'), ('electric', '전기·통신공사'), ('steel', '철강 구조물'), ('om', '유지관리')], business_body)

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
     [('list', '실적 목록'), ('gallery', '시공 현장')], projects_body)

# ================= 4. 사업절차 =================
process_body = """
<section class="block" id="scope">
  <div class="block-head">
    <p class="eyebrow">Scope of Work</p>
    <h2 class="sec-title">시공 역무범위</h2>
    <p class="sec-lead">가온이엔지가 직접 수행하는 다섯 공종입니다. 외주 없이 자체 인력이 진행해 공정을 단축하고 공사비를 낮춥니다.</p>
  </div>
  <div class="process" style="margin-top:0">
    <div class="step"><h3>토목공사</h3><p>경사·레벨 측정 장비를 동원해 최적의 토목공사 구축</p></div>
    <div class="step"><h3>구조물 제작</h3><p>아연도금 · 포스맥 등 경쟁력 있는 소재로 구조물 제작</p></div>
    <div class="step"><h3>구조물 공사</h3><p>숙련 인력을 투입해 신속하고 정확한 구조물 공사</p></div>
    <div class="step"><h3>전기공사</h3><p>전기설비 규정에 따른 정확하고 안전한 설계 및 시공</p></div>
    <div class="step"><h3>계통연계 · 시운전</h3><p>한전과의 고압케이블 연결 작업 및 시운전</p></div>
  </div>
</section>

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
      <li><div><b>발전사업 허가</b><span>용량에 따라 산업통상부 · 도청 · 시군구청에 허가 신청</span></div></li>
      <li><div><b>발전소 건설</b><span>전기사업법에 따라 자기자본으로 상업발전소 건설 (정부지원금 없음)</span></div></li>
      <li><div><b>사용 전 검사</b><span>한국전기안전공사 검사</span></div></li>
      <li><div><b>전력수급 계약 체결</b><span>한국전력공사 또는 전력거래소와 계약</span></div></li>
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
page('process.html', 4, '사업절차', '시공 역무범위와 태양광 발전사업이 진행되는 열 단계를 안내합니다.', 'field2.jpg',
     [('scope', '시공 역무범위'), ('procedure', '발전사업 진행절차')], process_body)
