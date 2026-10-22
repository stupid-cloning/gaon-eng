# -*- coding: utf-8 -*-
"""㈜가온이엔지 홈페이지 전체 페이지 생성 스크립트.
   실행: python3 build.py  → index.html 포함 13개 HTML 생성.
   공통 틀(헤더·푸터·연락처)은 이 파일만 고치면 전 페이지에 반영된다."""
import html

# ---------------------------------------------------------------- 공통 정보
TEL = "000-0000-0000"          # TODO 가온이엔지 대표전화
FAX = "000-0000-0000"          # TODO
EMAIL = "info@gaoneng.co.kr"   # TODO
ADDR = "강원특별자치도 원주시 서원대로 479-3"
ADDR_Q = "%EA%B0%95%EC%9B%90%ED%8A%B9%EB%B3%84%EC%9E%90%EC%B9%98%EB%8F%84%20%EC%9B%90%EC%A3%BC%EC%8B%9C%20%EC%84%9C%EC%9B%90%EB%8C%80%EB%A1%9C%20479-3"

MENU = [
    ("회사소개", "about-greeting.html", [("인사말", "about-greeting.html"), ("회사개요 · 연혁", "about-overview.html"),
                                      ("보유 면허", "about-license.html"), ("오시는 길", "about-location.html")]),
    ("사업분야", "business.html", [("지상형 발전소", "business-ground.html"), ("지붕형 · 공공시설", "business-roof.html"),
                                 ("BIPV · 수상 · 리파워링", "business-special.html"), ("유지관리 · A/S", "business-om.html")]),
    ("시공실적", "projects.html", [("실적 목록", "projects.html"), ("시공 현장 사진", "projects-gallery.html")]),
    ("사업절차", "process.html", []),
]

def gnb(current):
    out = []
    for title, href, subs in MENU:
        on = ' class="on"' if current in [h for _, h in subs] + [href] else ''
        if subs:
            items = ''.join('<li><a href="%s"%s>%s</a></li>' % (h, ' class="on"' if h == current else '', t) for t, h in subs)
            out.append(f'<li class="has-sub"><a href="{href}"{on}>{title}</a><ul class="sub">{items}</ul></li>')
        else:
            out.append(f'<li><a href="{href}"{on}>{title}</a></li>')
    return ''.join(out)

def head(title, current, visual=None, lead=None, crumb=None):
    sub = ''
    if visual:
        crumb_html = f'<a href="index.html">HOME</a> &rsaquo; ' + (f'{crumb} &rsaquo; ' if crumb else '') + title
        sub = f'''<section class="subvisual"><img src="img/{visual}" alt="" width="1400" height="1050"><div class="wrap">
  <p class="crumb">{crumb_html}</p><h1>{title}</h1><p>{lead or ""}</p></div></section>'''
    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title if title != '㈜가온이엔지' else '㈜가온이엔지 | 태양광 발전소 설계·시공'}{'' if title == '㈜가온이엔지' else ' | ㈜가온이엔지'}</title>
<meta name="description" content="{lead or "태양광 발전소 설계·시공 전문 전기공사업체 ㈜가온이엔지"}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="topbar"><div class="wrap"><span>대표전화 <strong>{TEL}</strong> · 평일 09:00–18:00</span><span class="r">{ADDR}</span></div></div>
<header class="header" id="header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="가온이엔지 홈"><span class="brand-mark" aria-hidden="true"></span><span class="brand-text"><b>㈜가온이엔지</b><span>GAON ENG</span></span></a>
  <button class="menu-toggle" id="menuToggle" aria-expanded="false" aria-controls="nav">메뉴</button>
  <nav class="nav" id="nav"><ul class="gnb">{gnb(current)}</ul><a href="contact.html" class="btn btn-primary nav-cta">문의하기</a></nav>
</div></header>
{sub}
<main>
'''

FOOT = f'''</main>
<footer class="footer"><div class="wrap">
  <div class="footer-top">
    <div class="brand"><span class="brand-mark" aria-hidden="true"></span><span class="brand-text"><b>㈜가온이엔지</b><span>GAON ENG</span></span></div>
    <div class="footer-links"><a href="about-greeting.html">회사소개</a><a href="business.html">사업분야</a><a href="projects.html">시공실적</a><a href="process.html">사업절차</a><a href="contact.html">문의하기</a></div>
  </div>
  <div class="footer-info"><span>주식회사 가온이엔지</span><span>대표 김현국</span><span>사업자등록번호 512-86-02034</span><span>{ADDR}</span><span>TEL {TEL}</span></div>
  <div>© 2026 GAON ENG Co., Ltd. All rights reserved.</div>
</div></footer>
<script src="site.js"></script>
</body>
</html>
'''

def page(fn, title, body, visual=None, lead=None, crumb=None):
    open(fn, 'w', encoding='utf-8').write(head(title, fn, visual, lead, crumb) + body + FOOT)
    print(fn)

def tabs(items, idp):
    """items: [(label, html)] → 탭 UI. 첫 탭이 기본 표시."""
    btns = ''.join(f'<button type="button" role="tab" id="{idp}-t{i}" aria-controls="{idp}-p{i}" aria-selected="{"true" if i == 0 else "false"}">{l}</button>' for i, (l, _) in enumerate(items))
    panels = ''.join(f'<div role="tabpanel" id="{idp}-p{i}" aria-labelledby="{idp}-t{i}"{"" if i == 0 else " hidden"}>{h}</div>' for i, (_, h) in enumerate(items))
    return f'<div class="tabs" data-tabs><div class="tablist" role="tablist">{btns}</div>{panels}</div>'

CTA = f'''
<section class="cta"><div class="wrap">
  <div><p class="eyebrow" style="color:#8fb6ff">Contact</p><h2>태양광 발전소 시공 문의</h2><p>사업 검토 단계의 상담부터 지명원·실적증명 자료 요청까지, 전화 또는 이메일로 연락 주시면 담당자가 안내해 드립니다.</p></div>
  <div class="contact-grid"><div><small>TEL</small><b>{TEL}</b></div><div><small>FAX</small><b>{FAX}</b></div><div class="full"><small>E-MAIL</small><b>{EMAIL}</b></div><div class="full"><a class="btn btn-ghost" href="contact.html">문의 안내 페이지</a></div></div>
</div></section>
'''

TRADES = """
<section class="block reveal" id="trades">
  <div class="block-head"><p class="eyebrow">Scope of Work</p><h2 class="sec-title">직접 수행 공종</h2>
  <p class="sec-lead">토목 · 구조물 제작 · 구조물 공사 · 전기 · 계통연계를 한 회사가 맡습니다. 공종 사이의 대기와 조율이 사라져 공정이 짧아지고, 그만큼 공사비가 낮아집니다.</p></div>
  <div class="process" style="margin-top:0">
    <div class="step"><h3>토목공사</h3><p>경사·레벨 측정 장비를 동원해 최적의 토목공사를 구축합니다.</p></div>
    <div class="step"><h3>구조물 제작</h3><p>아연도금·포스맥 등 경쟁력 있는 소재로 구조물을 제작합니다.</p></div>
    <div class="step"><h3>구조물 공사</h3><p>숙련 인력을 투입해 신속하고 정확하게 설치합니다.</p></div>
    <div class="step"><h3>전기공사</h3><p>전기설비 규정에 따라 정확하고 안전하게 설계·시공합니다. 전기공사업 등록 기업.</p></div>
    <div class="step"><h3>계통연계 · 시운전</h3><p>한전과의 고압케이블 연결 작업과 시운전까지 마무리합니다.</p></div>
  </div>
</section>
"""

# ---------------------------------------------------------------- 실적 데이터
PROJECTS = [
    # (프로젝트명, kW, 준공일, 설치유형, 발주구분)
    ("연천 선곡리 태양광발전소", 770, "2020.12.31", "지상형", ""),
    ("화천 삼화진 태양광발전소", 648, "2021.04.30", "지상형", ""),
    ("원주 법천리 태양광발전소", 597, "2021.09.30", "지상형", ""),
    ("영월 영승태양광발전소", 99.5, "2021.10.10", "지상형", ""),
    ("소상 태양광발전소", 300, "2021.10.31", "", ""),
    ("고흥 태양광발전소", 3000, "2021.12.31", "지상형", ""),
    ("화천 연운태양광발전소", 1000, "2022.08.31", "지상형", ""),
    ("원주 혁신센터", 315.4, "2022.10.25", "지붕형", "공공시설"),
    ("화천 제이에너지 태양광발전소", 437, "2022.12.31", "지상형", ""),
    ("화천 위라리 태양광발전소", 989, "2022.12.31", "지상형", ""),
    ("횡성 말구리썬일렉트릭 태양광발전소", 1000, "2023.02.28", "지상형", ""),
    ("화천 강남 태양광발전소", 99.9, "2023.06.29", "지상형", ""),
    ("음성 하이퍼윈도우", 234, "2023.11.30", "지붕형", "기업"),
    ("여주 다업햇빛두레 태양광발전소", 999.6, "2023.12.31", "지상형", ""),
    ("가평 위곡 리파워링", 137, "2024.02.28", "리파워링", ""),
    ("여의도 사학재단", 418.9, "2024.08.23", "BIPV", "공공시설"),
    ("마곡 CP", 163.9, "2024.08.23", "BIPV", ""),
    ("인천북항산업단지 태양광발전소", 5212, "2024.12.29", "", ""),
]
TOTAL_KW = sum(p[1] for p in PROJECTS)

def kw_fmt(kw):
    return f"{kw:,.1f}".rstrip('0').rstrip('.') if kw != int(kw) else f"{int(kw):,}"

# ================================================================ 메인
index_body = f'''
<section class="hero" id="top">
  <div class="slides" data-slider>
    <img class="hero-img is-on" src="img/hero.jpg" alt="" width="1280" height="960">
    <img class="hero-img" src="img/field2.jpg" alt="" width="873" height="652">
    <img class="hero-img" src="img/goheung.jpg" alt="" width="900" height="675">
  </div>
  <div class="wrap">
    <div>
      <p class="hero-kicker">강원 원주 · 전기공사업 등록 · 태양광 시공 전문</p>
      <h1>태양광 발전소,<br>토목부터 계통연계까지 <em>직접 시공</em>합니다</h1>
      <p class="hero-lead">소규모 발전사업자의 수백 kW급 발전소부터 공공시설·공장 지붕, 5MW 산업단지, 건물일체형(BIPV)까지. 다섯 공종을 한 회사가 맡아 빠르고 경제적으로 짓습니다.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="projects.html">시공실적</a><a class="btn btn-ghost" href="business.html">사업분야</a></div>
      <div class="dots" data-dots aria-hidden="true"></div>
    </div>
    <aside class="stat-card" aria-label="주요 현황">
      <h3>COMPANY AT A GLANCE</h3>
      <div class="stats">
        <div class="stat"><b>5<small>공종</small></b><span>토목·구조물·전기·계통연계 직접 수행</span></div>
        <div class="stat"><b>5.2<small>MW</small></b><span>최대 단일 사업 (인천북항산업단지)</span></div>
        <div class="stat"><b>4<small>유형</small></b><span>지상 · 지붕 · BIPV · 수상 준공 경험</span></div>
        <div class="stat"><b>18<small>건</small></b><span>준공 실적 · 2020년 설립</span></div>
      </div>
      <p class="stat-note">공공시설 · 기업 공장 · 발전사업자 발주 시공 경험</p>
    </aside>
  </div>
</section>

<section class="section reveal" id="business"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">Business</p><h2 class="sec-title">사업분야</h2>
  <p class="sec-lead">소규모 발전사업자의 지상형 발전소가 주력이고, 공공시설·공장 지붕형, BIPV·수상·리파워링까지 네 유형 모두 준공 실적이 있습니다.</p></div></div>
  <div class="biz">
    <article class="biz-card"><div class="biz-icon"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="11" rx="1"/><path d="M3 10.5h18M9 5v11M15 5v11M12 16v3M8 19h8"/></svg></div>
      <h3>지상형 발전소</h3><p>개인·협동조합·SPC 발전사업자의 수백 kW~수 MW급 발전소를 토목부터 계통연계까지 직접 시공합니다.</p><a href="business-ground.html">자세히 보기 →</a></article>
    <article class="biz-card"><div class="biz-icon"><svg viewBox="0 0 24 24"><path d="M4 20h16M6 20V9l6-5 6 5v11M10 20v-6h4v6"/></svg></div>
      <h3>지붕형 · 공공시설</h3><p>공공건물·공장·창고 지붕. 구조 안전성과 방수를 먼저 검토하고 운영 중인 시설에 지장 없이 시공합니다.</p><a href="business-roof.html">자세히 보기 →</a></article>
    <article class="biz-card"><div class="biz-icon"><svg viewBox="0 0 24 24"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg></div>
      <h3>BIPV · 수상 · 리파워링</h3><p>건물 외장 일체형, 저수지 수상형, 노후 발전소 모듈·인버터 교체. 일반 시공과 다른 공정이 필요한 유형입니다.</p><a href="business-special.html">자세히 보기 →</a></article>
    <article class="biz-card"><div class="biz-icon"><svg viewBox="0 0 24 24"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.4 2.4-2.1-2.1z"/></svg></div>
      <h3>유지관리 · A/S</h3><p>준공 후 정기점검과 신속한 고장 대응으로 발전효율을 유지합니다.</p><a href="business-om.html">자세히 보기 →</a></article>
  </div>
</div></section>

<section class="section soft reveal" id="process"><div class="wrap">
  <p class="eyebrow">Why Gaon</p><h2 class="sec-title">직접 수행 공종</h2>
  <p class="sec-lead">토목 · 구조물 제작 · 구조물 공사 · 전기 · 계통연계를 한 회사가 맡습니다. 공종 사이의 대기와 조율이 사라져 공정이 짧아지고, 그만큼 공사비가 낮아집니다.</p>
  <div class="process">
    <div class="step"><h3>토목공사</h3><p>경사·레벨 측정 장비를 동원한 부지 정지와 기초 공사</p></div>
    <div class="step"><h3>구조물 제작</h3><p>아연도금·포스맥 등 내식성 소재 구조물 제작</p></div>
    <div class="step"><h3>구조물 공사</h3><p>숙련 인력 투입으로 신속하고 정확한 구조물 설치</p></div>
    <div class="step"><h3>전기공사</h3><p>전기설비 규정에 따른 모듈·인버터·수배전 설비 시공</p></div>
    <div class="step"><h3>계통연계 · 시운전</h3><p>한전 고압케이블 연결, 사용 전 검사 및 시운전</p></div>
  </div>
</div></section>

<section class="section reveal" id="projects"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">Projects</p><h2 class="sec-title">주요 시공실적</h2>
  <p class="sec-lead">소규모 발전사업자의 발전소부터 공공시설 지붕, 5MW 산업단지, BIPV까지 18개 현장을 준공했습니다.</p></div>
  <a class="btn btn-outline" href="projects.html">전체 실적</a></div>
  <div class="projects">
    <article class="proj"><div class="ph"><img src="img/goheung.jpg" alt="고흥 태양광발전소 전경" loading="lazy"></div><div class="proj-body"><div><h3>고흥 태양광발전소</h3><p class="meta">전남 고흥 · 2021.12 준공</p></div><span class="kw">3,000<small>kW</small></span></div></article>
    <article class="proj"><div class="ph"><img src="img/yeouido.jpg" alt="여의도 사학재단 BIPV 외관" loading="lazy"></div><div class="proj-body"><div><h3>여의도 사학재단<span class="tag">BIPV</span></h3><p class="meta">서울 영등포 · 공공시설 · 2024.08 준공</p></div><span class="kw">418.9<small>kW</small></span></div></article>
    <article class="proj"><div class="ph"><img src="img/wonju.jpg" alt="원주 혁신센터 지붕형 태양광" loading="lazy"></div><div class="proj-body"><div><h3>원주 혁신센터</h3><p class="meta">강원 원주 · 공공시설 · 2022.10 준공</p></div><span class="kw">315.4<small>kW</small></span></div></article>
    <article class="proj"><div class="ph"><img src="img/yeoju.jpg" alt="여주 다업햇빛두레 태양광발전소" loading="lazy"></div><div class="proj-body"><div><h3>여주 다업햇빛두레 태양광발전소</h3><p class="meta">경기 여주 · 2023.12 준공</p></div><span class="kw">999.6<small>kW</small></span></div></article>
    <article class="proj"><div class="ph"><img src="img/boryeong.jpg" alt="수상태양광 발전설비" loading="lazy"></div><div class="proj-body"><div><h3>보령화력 수상태양광</h3><p class="meta">충남 보령 · 수상형</p></div><span class="kw">1,200<small>kW</small></span></div></article>
    <article class="proj"><div class="ph"><img src="img/magok.jpg" alt="마곡 CP BIPV 외관" loading="lazy"></div><div class="proj-body"><div><h3>마곡 CP<span class="tag">BIPV</span></h3><p class="meta">서울 강서 · 2024.08 준공</p></div><span class="kw">163.9<small>kW</small></span></div></article>
  </div>
</div></section>

<section class="section soft reveal" id="about"><div class="wrap about">
  <div class="about-text"><p class="eyebrow">Company</p><h2 class="sec-title">회사소개</h2>
    <p>주식회사 가온이엔지는 2020년 강원 원주에서 설립된 태양광 시공 전문 전기공사업체입니다. 강원 영서권을 중심으로 소규모 발전사업자의 지상형 발전소를 지어왔고, 공공시설과 기업 공장 지붕형을 거쳐 2024년에는 5.2MW 산업단지와 서울 BIPV 2건을 준공했습니다.</p>
    <p style="margin-top:1.6rem"><a class="btn btn-outline" href="about-greeting.html">회사소개</a></p></div>
  <div class="photo"><img src="img/field2.jpg" alt="지상형 태양광발전소 시공 현장" loading="lazy"></div>
</div></section>
''' + CTA
page('index.html', '㈜가온이엔지', index_body)

# ================================================================ 회사소개
page('about-greeting.html', '인사말', '''
<section class="block reveal"><div class="wrap two">
  <div class="prose"><p class="eyebrow">CEO Message</p><h2 class="sec-title">인사말</h2>
    <p class="quote" style="margin-top:1.4rem">항상 안전을 생각하고 가치를 더욱 높이는<br>신뢰받는 동반자가 되겠습니다.</p>
    <p>주식회사 가온이엔지는 2020년도에 설립되어 태양광 발전사업을 영위하고 있는 회사입니다.</p>
    <p>친환경 에너지를 추구하며, 현장 여건에 맞는 설계와 기술력을 바탕으로 태양광 공사를 만들어가고 있습니다.</p>
    <p>주식회사 가온이엔지에 많은 관심과 응원 부탁드리며, 최선을 다하여 고객 만족으로 보답 드리겠습니다. 감사합니다.</p>
    <p class="sign">주식회사 가온이엔지<b>대표이사 김현국</b></p></div>
  <div class="photo"><img src="img/field2.jpg" alt="지상형 태양광발전소 시공 현장" loading="lazy"></div>
</div></section>
''' + CTA, 'sub.jpg', '안전을 최우선으로, 현장 여건에 맞는 설계와 기술력으로 신뢰를 쌓아갑니다.', '회사소개')

overview_tab = '''
<div class="two">
  <div><table class="overview" style="margin-top:0">
    <tr><th>회사명</th><td>주식회사 가온이엔지 (GAON ENG Co., Ltd.)</td></tr><tr><th>대표자</th><td>김현국</td></tr>
    <tr><th>설립일</th><td>2020년 9월 9일</td></tr><tr><th>사업자등록번호</th><td>512-86-02034</td></tr>
    <tr><th>사업종류</th><td>태양광 / 전기·통신공사 (전기공사업 등록)</td></tr><tr><th>소재지</th><td>''' + ADDR + '''</td></tr>
  </table></div>
  <ul class="strengths" aria-label="경쟁력">
    <li><i>1</i><div><b>신속하고 정확한 시공</b><span>공정을 줄여 공사비를 최소화합니다.</span></div></li>
    <li><i>2</i><div><b>숙련된 기술인력</b><span>견고하고 안전한 공사를 수행합니다.</span></div></li>
    <li><i>3</i><div><b>다양한 현장 경험</b><span>예상 밖 현장 상황에도 노하우로 신속히 대처합니다.</span></div></li>
    <li><i>4</i><div><b>품질과 가격 경쟁력</b><span>최고 품질 자재를 경쟁력 있는 가격으로 설치·시공합니다.</span></div></li>
    <li><i>5</i><div><b>신속한 A/S</b><span>고객만족은 물론 최적의 발전효율을 유지합니다.</span></div></li>
  </ul>
</div>'''
history_tab = '''
<ul class="timeline">
  <li><b>2024</b><ul><li>인천북항산업단지 태양광발전소 준공 <span>5,212kW · 최대 단일 사업</span></li><li>여의도 사학재단 · 마곡 CP 건물일체형(BIPV) 준공 <span>418.9kW · 163.9kW</span></li><li>가평 위곡 리파워링 공사 준공 <span>137kW</span></li></ul></li>
  <li><b>2023</b><ul><li>여주 다업햇빛두레 태양광발전소 준공 <span>999.6kW</span></li><li>횡성 말구리썬일렉트릭 태양광발전소 준공 <span>1,000kW</span></li><li>음성 하이퍼윈도우 공장 지붕형 · 화천 강남 태양광발전소 준공</li></ul></li>
  <li><b>2022</b><ul><li>화천 연운 · 위라리 · 제이에너지 태양광발전소 준공 <span>합계 2,426kW</span></li><li>원주 혁신센터 지붕형 태양광 준공 <span>315.4kW · 공공시설</span></li></ul></li>
  <li><b>2021</b><ul><li>고흥 태양광발전소 준공 <span>3,000kW</span></li><li>화천 삼화진 · 원주 법천리 · 소상 · 영월 영승 태양광발전소 준공</li></ul></li>
  <li><b>2020</b><ul><li>주식회사 가온이엔지 설립 <span>9월 9일 · 강원 원주</span></li><li>연천 선곡리 태양광발전소 준공 <span>770kW · 첫 준공 현장</span></li></ul></li>
</ul>'''
page('about-overview.html', '회사개요 · 연혁', '''
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Overview &amp; History</p><h2 class="sec-title">회사개요 · 연혁</h2></div>
''' + tabs([('회사개요', overview_tab), ('연혁', history_tab)], 'ov') + '''
</div></section>
''' + CTA, 'sub.jpg', '태양광 설계·시공, 전기·통신공사, 철강 구조물을 수행하는 전기공사업 등록 법인입니다.', '회사소개')

page('about-license.html', '보유 면허', '''
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">License &amp; Certification</p><h2 class="sec-title">보유 면허 · 등록</h2>
  <p class="sec-lead">입찰 참가 및 계약에 필요한 등록·면허 서류는 요청 시 사본으로 제공합니다.</p></div>
  <div class="cert">
    <div class="cert-card"><small>등록</small><b>전기공사업 등록</b><span>전기공사업법에 따른 전기공사업 등록 (등록번호 확인 중)</span></div>
    <div class="cert-card"><small>법인</small><b>법인 사업자등록</b><span>사업자등록번호 512-86-02034 · 2020년 9월 설립 법인</span></div>
    <div class="cert-card"><small>서류</small><b>지명원 · 실적증명</b><span>공사지명원, 법인 등기부등본, 인감증명서 등 입찰 서류 구비</span></div>
  </div>
</div></section>
''' + CTA, 'sub.jpg', '전기공사업 등록 기업으로 공공·민간 발주 공사에 참여합니다.', '회사소개')

MAP = f'''<div class="map-frame"><iframe title="오시는 길 지도" src="https://www.google.com/maps?q={ADDR_Q}&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
<p class="map-links"><a class="btn btn-outline" href="https://map.naver.com/p/search/{ADDR_Q}" target="_blank" rel="noopener">네이버 지도</a> <a class="btn btn-outline" href="https://map.kakao.com/link/search/{ADDR_Q}" target="_blank" rel="noopener">카카오맵</a></p>'''
INFO = f'''<ul class="info-list">
  <li><span>주소</span><span>{ADDR}</span></li><li><span>대표전화</span><span>{TEL}</span></li><li><span>팩스</span><span>{FAX}</span></li>
  <li><span>이메일</span><span>{EMAIL}</span></li><li><span>업무시간</span><span>평일 09:00–18:00 (주말·공휴일 휴무)</span></li></ul>'''
page('about-location.html', '오시는 길', f'''
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Location</p><h2 class="sec-title">오시는 길</h2></div>
  <div class="map-box">{INFO}<div>{MAP}</div></div>
</div></section>
''' + CTA, 'sub.jpg', ADDR, '회사소개')

# ================================================================ 문의
page('contact.html', '문의하기', f'''
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Contact</p><h2 class="sec-title">문의 안내</h2>
  <p class="sec-lead">태양광 발전소 시공 상담, 견적, 지명원·실적증명 자료 요청은 전화 또는 이메일로 연락 주십시오.</p></div>
  <div class="contact-cards">
    <div class="cert-card"><small>TEL</small><b style="font-size:1.4rem">{TEL}</b><span>평일 09:00–18:00</span></div>
    <div class="cert-card"><small>E-MAIL</small><b style="font-size:1.1rem;word-break:break-all">{EMAIL}</b><span>자료 요청 · 견적 문의</span></div>
    <div class="cert-card"><small>FAX</small><b style="font-size:1.4rem">{FAX}</b><span>서류 송부</span></div>
  </div>
  <div class="map-box" style="margin-top:3rem">{INFO}<div>{MAP}</div></div>
</div></section>
''', 'hero.jpg', '전화 또는 이메일로 연락 주시면 담당자가 안내해 드립니다.')

# ================================================================ 사업분야
materials = '''
<div class="table-wrap"><table class="spec"><thead><tr><th>소재</th><th>특징</th><th>주로 쓰는 곳</th></tr></thead><tbody>
  <tr><th>용융아연도금 강재</th><td>강재 표면에 아연을 입혀 부식을 막는 가장 일반적인 방식. 비용 효율이 높고 강성이 좋습니다.</td><td>지상형 기둥·보</td></tr>
  <tr><th>포스맥 (PosMAC)</th><td>아연·마그네슘·알루미늄 합금 도금 강판. 일반 아연도금보다 내식성이 높고 절단면 자가 보호 성능이 있어 해안·고습 지역에 유리합니다.</td><td>해안·수상 인접 부지, 레일 부재</td></tr>
  <tr><th>알루미늄</th><td>가볍고 녹이 슬지 않아 지붕 하중 여유가 적을 때 유리하나 강재보다 비용이 높습니다.</td><td>지붕형 레일·클램프</td></tr>
</tbody></table></div>
<ul class="checks"><li>풍하중·적설하중: 건축구조기준(KDS)의 지역별 기본풍속·기본적설하중 적용</li><li>지상형 기초: 지반 조건에 따라 콘크리트 독립기초 또는 스파이럴 파일</li><li>지붕형: 기존 지붕 구조의 허용 하중 검토 후 고정 방식 결정</li></ul>'''
grid = '''
<ol class="flow">
  <li><div><b>한전 연계 협의</b><span>설치 용량과 연계 지점을 신청해 선로 여유 용량과 연계 방식 확정</span></div></li>
  <li><div><b>수전 · 수배전 설비</b><span>일반적으로 100kW 미만은 저압, 그 이상은 특고압(22.9kV) 연계로 변압기·차단기를 갖춘 수전설비 필요</span></div></li>
  <li><div><b>케이블 포설 · 접지</b><span>전압강하 기준 이내로 케이블 산정, 접지·피뢰 설비 시공</span></div></li>
  <li><div><b>사용 전 검사</b><span>한국전기안전공사의 절연·접지·보호장치 검사</span></div></li>
  <li><div><b>계통연계 · 시운전</b><span>고압케이블 연결, 인버터 동기화, 초기 발전 데이터 검증</span></div></li>
</ol>'''
page('business.html', '사업분야', '''
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Business Areas</p><h2 class="sec-title">사업분야</h2>
  <p class="sec-lead">소규모 발전사업자의 지상형 발전소가 주력이고, 공공시설·공장 지붕형, 건물일체형(BIPV)·수상형·리파워링까지 네 유형 모두 준공 실적이 있습니다.</p></div>
  <div class="hub">
    <article class="proj"><div class="ph"><img src="img/yeoju.jpg" alt="" loading="lazy"></div><div class="proj-body"><h3>지상형 발전소</h3><p>개인·협동조합·SPC 발전사업자의 수백 kW~수 MW급 발전소. 토목부터 계통연계까지 직접 시공하고 허가·검사 절차를 함께 챙깁니다.</p><a class="more" href="business-ground.html">자세히 보기 →</a></div></article>
    <article class="proj"><div class="ph"><img src="img/wonju.jpg" alt="" loading="lazy"></div><div class="proj-body"><h3>지붕형 · 공공시설</h3><p>공공건물·공장·창고 지붕에 설치하는 발전소. 지붕 구조 안전성과 방수를 먼저 검토하고, 운영 중인 시설에 지장 없이 시공합니다.</p><a class="more" href="business-roof.html">자세히 보기 →</a></div></article>
    <article class="proj"><div class="ph"><img src="img/yeouido.jpg" alt="" loading="lazy"></div><div class="proj-body"><h3>BIPV · 수상형 · 리파워링</h3><p>건물 외장과 일체화된 BIPV, 저수지 수상형, 노후 발전소의 모듈·인버터 교체. 일반 시공과 다른 설계·공정이 필요한 유형입니다.</p><a class="more" href="business-special.html">자세히 보기 →</a></div></article>
    <article class="proj"><div class="ph"><img src="img/mungyeong.jpg" alt="" loading="lazy"></div><div class="proj-body"><h3>유지관리 · A/S</h3><p>준공 후 정기점검과 신속한 고장 대응으로 발전효율을 유지합니다.</p><a class="more" href="business-om.html">자세히 보기 →</a></div></article>
  </div>
</div></section>
<div class="wrap">''' + TRADES + '''</div>
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Structure &amp; Electrical</p><h2 class="sec-title">구조물 · 전기설비</h2>
  <p class="sec-lead">모듈은 제품이지만 구조물과 전기설비는 현장에서 만들어집니다. 25년 수명과 안전은 이 두 공종에서 결정됩니다.</p></div>
''' + tabs([('구조물 소재 · 설계 기준', materials), ('계통연계 절차', grid)], 'se') + '''
</div></section>
''' + CTA, 'hero.jpg', '소규모 발전사업자의 지상형 발전소부터 공공시설·공장 지붕, BIPV·수상·리파워링까지.')

design_steps = '''
<ol class="flow">
  <li><div><b>현장조사</b><span>부지 경계·경사·지반, 주변 건물·수목에 의한 음영, 인근 한전 선로의 연계 여유 용량을 확인합니다.</span></div></li>
  <li><div><b>발전량 검토</b><span>지역 일사량 데이터로 경사각·방위각을 조정하며 연간 발전량을 시뮬레이션하고, 음영 손실과 계통 제약을 반영해 설치 용량을 정합니다.</span></div></li>
  <li><div><b>배치 · 구조 설계</b><span>어레이 간격(동지 기준 음영 회피)과 구조물 형식을 정하고, 풍하중·적설하중을 검토해 기초 형식을 결정합니다.</span></div></li>
  <li><div><b>전기 설계</b><span>모듈 스트링 구성, 인버터 용량과 대수, 접속함·수배전반 구성을 단선도로 작성하고 케이블과 보호장치를 산정합니다.</span></div></li>
  <li><div><b>인허가 도면</b><span>발전사업허가, 개발행위허가, 사용 전 검사에 필요한 도면과 계산서를 작성합니다.</span></div></li>
</ol>
<p class="note">허가부터 REC 거래까지 전체 흐름은 <a href="process.html" style="color:var(--accent);font-weight:700">사업절차</a> 페이지에서 확인할 수 있습니다.</p>'''
site_cond = '''
<div class="types">
  <article class="type"><div class="photo"><img src="img/yeoju.jpg" alt="" loading="lazy"></div><div class="type-body"><h3>부지 경사 · 기초</h3><p>경사지는 토공량과 기초 형식이 공사비를 좌우합니다. 레벨 측정으로 절·성토를 최소화하고 지반에 맞는 기초를 고릅니다.</p><ul><li>콘크리트 독립기초 또는 스파이럴 파일</li><li>배수 계획 없으면 우기에 기초 세굴 발생</li></ul></div></article>
  <article class="type"><div class="photo"><img src="img/field2.jpg" alt="" loading="lazy"></div><div class="type-body"><h3>어레이 간격 · 음영</h3><p>간격을 좁히면 용량은 늘지만 겨울철 앞 열 그림자가 발전량을 깎습니다. 동지 기준 음영으로 간격을 정합니다.</p><ul><li>용량 극대화와 발전량의 균형</li><li>주변 수목 성장까지 고려</li></ul></div></article>
</div>'''
page('business-ground.html', '지상형 발전소', '''
<section class="block reveal"><div class="wrap two">
  <div class="prose"><p class="eyebrow">For Power Producers</p><h2 class="sec-title">지상형 발전소 시공</h2>
    <p>개인·협동조합·SPC가 짓는 수백 kW~1MW급 지상형 발전소가 가온이엔지의 주력입니다. 2020년 연천 770kW를 시작으로 강원 영서권(화천·원주·횡성·영월)과 경기·전남에서 지상형 발전소 12곳을 준공했고, 2021년 고흥 3MW, 2024년 인천북항산업단지 5.2MW까지 규모를 넓혔습니다.</p>
    <p>발전사업은 용량 구간에 따라 허가 기관, 한전 연계 방식, 공급인증서(REC) 가중치가 달라집니다. 설계 단계에서 이 조건을 함께 검토해, 같은 부지에서 수익이 가장 잘 나오는 용량과 배치를 잡습니다.</p></div>
  <div class="photo"><img src="img/goheung.jpg" alt="고흥 태양광발전소" loading="lazy"></div>
</div></section>
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Process</p><h2 class="sec-title">설계 · 시공 절차</h2></div>
''' + tabs([('설계 절차', design_steps), ('시공 공정', TRADES.replace('<section class="block reveal" id="trades">', '<div>').replace('</section>', '</div>')), ('부지 조건', site_cond)], 'gr') + '''
  <p style="margin-top:2rem"><a class="btn btn-outline" href="projects.html">지상형 준공 실적</a></p>
</div></section>
''' + CTA, 'goheung.jpg', '개인·협동조합·SPC 발전사업자의 수백 kW~수 MW급 지상형 발전소를 토목부터 계통연계까지 직접 시공합니다.', '사업분야')

roof_check = '''
<ol class="flow">
  <li><div><b>구조 안전성</b><span>지붕 구조(철골·트러스·슬래브)의 허용 하중 여유를 확인합니다. 여유가 적으면 경량 구조물·알루미늄 레일을 쓰거나 설치 용량을 줄입니다.</span></div></li>
  <li><div><b>지붕 재질 · 고정 방식</b><span>샌드위치판넬·슬레이트·콘크리트에 따라 클램프(무타공)·앵커(타공) 방식이 달라집니다. 타공 시 관통부 방수가 핵심입니다.</span></div></li>
  <li><div><b>노후도 · 보수 범위</b><span>지붕 자체가 노후했으면 발전소보다 지붕 보수가 먼저입니다. 보수 범위와 비용 분담을 사전에 정합니다.</span></div></li>
  <li><div><b>수전 설비 연계</b><span>건물의 기존 수전설비(변압기·분전반) 여유 용량을 확인하고 자가소비형·전량판매형 중 연계 방식을 정합니다.</span></div></li>
  <li><div><b>시공 중 안전 · 조업</b><span>추락 방지 설비, 자재 양중 계획, 조업·업무 시간을 피한 공정표를 발주처와 합의합니다.</span></div></li>
</ol>'''
roof_cases = '''
<div class="gallery">
  <figure><div class="photo"><img src="img/wonju.jpg" alt="" loading="lazy"></div><figcaption><b>원주 혁신센터</b>315.4kW · 공공시설 · 2022</figcaption></figure>
  <figure><div class="photo"><img src="img/chungju.jpg" alt="" loading="lazy"></div><figcaption><b>충주 세아특수강</b>2,400kW · 공장 지붕</figcaption></figure>
  <figure><div class="photo"><img src="img/mungyeong.jpg" alt="" loading="lazy"></div><figcaption><b>문경 서일태양광</b>1,000kW</figcaption></figure>
</div>'''
page('business-roof.html', '지붕형 · 공공시설', '''
<section class="block reveal"><div class="wrap two">
  <div class="prose"><p class="eyebrow">For Public &amp; Industrial Buildings</p><h2 class="sec-title">지붕형 발전소</h2>
    <p>공공건물·공장·창고 지붕형 발전소는 땅을 사지 않아도 되고 건물의 전기요금을 줄여줍니다. 대신 시설이 운영 중인 상태에서 공사하므로, 지붕 구조의 안전성 검토와 방수, 작업 동선과 안전관리가 지상형보다 훨씬 까다롭습니다.</p>
    <p>가온이엔지는 원주 혁신센터(315.4kW) 등 공공시설과 음성 하이퍼윈도우(234kW) 등 기업 공장 지붕형 발전소를 준공했습니다. 공공기관 발주 공사의 서류·검사 절차와 공장의 조업 조건을 모두 경험했습니다.</p></div>
  <div class="photo"><img src="img/wonju.jpg" alt="원주 혁신센터 지붕형 태양광" loading="lazy"></div>
</div></section>
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Process</p><h2 class="sec-title">검토 · 시공 · 현장</h2></div>
''' + tabs([('지붕 검토 항목', roof_check), ('시공 공정', TRADES.replace('<section class="block reveal" id="trades">', '<div>').replace('</section>', '</div>')), ('시공 현장', roof_cases)], 'rf') + '''
</div></section>
''' + CTA, 'wonju.jpg', '공공건물·공장·창고 지붕에 설치하는 발전소. 구조 안전성과 방수를 먼저 검토하고, 운영 중인 시설에 지장 없이 시공합니다.', '사업분야')

bipv = '''<div class="two"><div class="photo"><img src="img/yeouido.jpg" alt="" loading="lazy"></div><div class="prose"><h3 style="font-size:1.2rem">건물일체형 BIPV</h3><p>모듈이 외장재(커튼월·스팬드럴)를 겸합니다. 발전량보다 외관·방수·화재 안전이 먼저이고, 건축 설계 단계부터 외장 시공사와 공정을 맞춰야 합니다. 수직면 설치라 발전량 검토 기준도 다릅니다.</p><ul class="checks"><li>여의도 사학재단 418.9kW (2024)</li><li>마곡 CP 163.9kW (2024)</li></ul></div></div>'''
floating = '''<div class="two"><div class="photo"><img src="img/boryeong.jpg" alt="" loading="lazy"></div><div class="prose"><h3 style="font-size:1.2rem">수상형</h3><p>저수지·담수 위에 부력체를 띄우고 계류(앵커)로 고정합니다. 수위 변동과 풍파를 견디면서 어레이 간격을 유지해야 하고, 모든 부재가 상시 습기에 노출되므로 내식성 소재가 필수입니다.</p><ul class="checks"><li>부력체 내구성 · 계류 하중 검토</li><li>육상 수전설비까지 케이블 경로</li><li>보령화력 수상태양광 시공 참여</li></ul></div></div>'''
repower = '''<div class="two"><div class="photo"><img src="img/field2.jpg" alt="" loading="lazy"></div><div class="prose"><h3 style="font-size:1.2rem">리파워링</h3><p>10년 이상 된 발전소는 모듈 효율 저하와 인버터 노후로 발전량이 눈에 띄게 줄어듭니다. 구조물과 계통연계 설비는 두고 모듈·인버터만 최신 제품으로 바꾸면 같은 부지에서 용량과 발전량이 늘어납니다.</p><ul class="checks"><li>기존 구조물 하중 여유 · 부식 상태 검토</li><li>신규 모듈 규격에 맞는 보강 · 스트링 재구성</li><li>용량 변경 시 인허가 변경 필요</li><li>가평 위곡 리파워링 137kW (2024)</li></ul></div></div>'''
page('business-special.html', 'BIPV · 수상 · 리파워링', '''
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Special Types</p><h2 class="sec-title">특수 유형</h2>
  <p class="sec-lead">2024년 서울 여의도·마곡에서 건물일체형(BIPV) 2건, 가평에서 리파워링 1건을 준공했고 보령화력 수상태양광 시공에 참여했습니다. 세 유형 모두 일반 지상·지붕형과 다른 공정을 요구합니다.</p></div>
''' + tabs([('BIPV', bipv), ('수상형', floating), ('리파워링', repower)], 'sp') + '''
</div></section>
<div class="wrap">''' + TRADES + '''</div>
''' + CTA, 'yeouido.jpg', '건물 외장과 일체화된 BIPV, 저수지 수상형, 노후 발전소 리파워링.', '사업분야')

inspection = '''
<div class="table-wrap"><table class="spec"><thead><tr><th>구분</th><th>점검 내용</th><th>일반적인 점검 방법</th></tr></thead><tbody>
  <tr><th>모듈</th><td>표면 오염 · 파손 · 변색, 핫스팟(국부 과열), 정션박스 상태</td><td>육안, 열화상 카메라, 스트링별 전압·전류 측정</td></tr>
  <tr><th>구조물</th><td>볼트 풀림 · 부식 · 변형, 기초 침하 · 세굴, 지붕형 고정부 누수</td><td>육안, 토크 점검</td></tr>
  <tr><th>접속함 · 인버터</th><td>단자 발열, 퓨즈 · 서지보호기 상태, 인버터 효율 · 경보 이력, 냉각팬 · 필터</td><td>열화상, 인버터 로그 분석</td></tr>
  <tr><th>전기설비</th><td>절연저항, 접지저항, 차단기 · 계전기 동작, 케이블 피복 상태</td><td>절연저항계, 접지저항계</td></tr>
  <tr><th>발전 데이터</th><td>인버터별 · 스트링별 발전량 편차, 설계 발전량 대비 실적</td><td>모니터링 데이터 분석</td></tr>
</tbody></table></div>
<p class="note">점검 주기는 발전소 규모와 계약 조건에 따라 정해지며, 전기안전관리법에 따른 정기검사가 별도로 있습니다.</p>'''
as_flow = '''
<ol class="flow">
  <li><div><b>접수</b><span>전화 · 모니터링 경보로 이상 접수</span></div></li>
  <li><div><b>원격 진단</b><span>모니터링 데이터로 고장 범위(인버터 · 스트링 · 계통) 1차 판단</span></div></li>
  <li><div><b>현장 조치</b><span>부품 교체 · 재결선 · 설정 변경 등 조치 후 발전 재개 확인</span></div></li>
  <li><div><b>보고</b><span>원인 · 조치 내용 · 재발 방지 방안 보고</span></div></li>
</ol>'''
page('business-om.html', '유지관리 · A/S', '''
<section class="block reveal"><div class="wrap two">
  <div class="prose"><p class="eyebrow">Operation &amp; Maintenance</p><h2 class="sec-title">유지관리 · A/S</h2>
    <p>준공 직후의 발전량이 25년 동안 유지되지는 않습니다. 모듈 표면 오염, 주변 수목 성장으로 인한 음영, 인버터 고장, 접속함 발열, 구조물 볼트 풀림이 조금씩 발전량을 깎습니다. 인버터 한 대가 멈춘 것을 한 달 뒤에 발견하면 그 달 수익의 상당 부분이 사라집니다.</p>
    <p>가온이엔지는 A/S에 신속하게 대응해 고객만족은 물론 최적의 발전효율을 유지합니다.</p></div>
  <div class="photo"><img src="img/mungyeong.jpg" alt="태양광발전소 유지관리" loading="lazy"></div>
</div></section>
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Inspection &amp; Response</p><h2 class="sec-title">점검 · 대응</h2></div>
''' + tabs([('정기점검 항목', inspection), ('고장 대응 절차', as_flow)], 'om') + '''
</div></section>
''' + CTA, 'mungyeong.jpg', '정기점검과 신속한 고장 대응으로 발전효율을 유지합니다.', '사업분야')

# ================================================================ 시공실적
rows = []
for i, (name, kw, date, typ, owner) in enumerate(sorted(PROJECTS, key=lambda p: p[2], reverse=True), 1):
    badge = f'<span class="tag tag-soft">{owner}</span>' if owner else ''
    rows.append(f'<tr data-type="{typ}"><td class="c">{len(PROJECTS)-i+1}</td><td>{html.escape(name)}{badge}</td><td class="c">{typ}</td><td class="num">{kw_fmt(kw)}</td><td class="c">{date}</td></tr>')
filters = '<button type="button" data-type="all" aria-pressed="true">전체</button>' + ''.join(f'<button type="button" data-type="{t}" aria-pressed="false">{t}</button>' for t in ["지상형", "지붕형", "BIPV", "리파워링"])
page('projects.html', '시공실적', f'''
<section class="block reveal"><div class="wrap">
  <div class="summary">
    <div><b>{len(PROJECTS)}<small>건</small></b><span>준공 실적 (2020–2024)</span></div>
    <div><b>{TOTAL_KW/1000:.1f}<small>MW</small></b><span>누적 시공 용량</span></div>
    <div><b>5,212<small>kW</small></b><span>최대 단일 사업 (인천북항산업단지)</span></div>
    <div><b>4<small>종</small></b><span>설치 유형 (지상·지붕·BIPV·리파워링)</span></div>
  </div>
  <div class="block-head" style="margin-bottom:1.2rem"><p class="eyebrow">Project List</p><h2 class="sec-title">실적 목록</h2></div>
  <div class="filters" id="filters">{filters}</div>
  <div class="table-wrap"><table class="ptable" id="ptable">
    <thead><tr><th style="width:4em;text-align:center">연번</th><th>프로젝트명</th><th style="text-align:center">유형</th><th style="text-align:right">용량 (kW)</th><th style="text-align:center">준공일</th></tr></thead>
    <tbody>{''.join(rows)}</tbody></table></div>
  <p class="note">공공시설·기업 표시는 발주처 구분입니다. 실적증명서·준공 서류는 요청에 따라 제공합니다.</p>
</div></section>
''' + CTA, 'goheung.jpg', f'소규모 발전사업자의 수백 kW급 발전소부터 공공시설 지붕, 5MW 산업단지, BIPV까지 {len(PROJECTS)}개 현장을 준공했습니다.')

page('projects-gallery.html', '시공 현장 사진', '''
<section class="block reveal"><div class="wrap">
  <div class="block-head"><p class="eyebrow">Site Photos</p><h2 class="sec-title">시공 현장</h2></div>
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
</div></section>
''' + CTA, 'yeoju.jpg', '지상형 · 지붕형 · BIPV · 수상형 시공 현장입니다.', '시공실적')

# ================================================================ 사업절차
page('process.html', '사업절차', '''
<section class="block reveal"><div class="wrap two">
  <div><p class="eyebrow">Procedure</p><h2 class="sec-title">태양광 발전사업 진행절차</h2>
    <p class="sec-lead">처음 발전소를 짓는 소규모 발전사업자를 위한 안내입니다. 발전사업 허가부터 공급인증서(REC) 거래까지, 발전소 한 곳이 수익을 내기까지 거치는 열 단계입니다.</p>
    <table class="overview" aria-label="발전사업 허가 기관"><tr><th>3MW 초과</th><td>산업통상부</td></tr><tr><th>200kW 초과 ~ 3MW 이하</th><td>도청 (광역자치단체)</td></tr><tr><th>200kW 이하</th><td>시·군·구청</td></tr></table>
    <p class="note">허가 기관은 설비 용량 기준으로 나뉩니다. 전기사업법상 발전사업 허가 기준.</p></div>
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
</div></section>
''' + CTA, 'field2.jpg', '태양광 발전소가 허가부터 수익 발생까지 거치는 열 단계를 안내합니다.')
