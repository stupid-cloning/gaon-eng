# ㈜가온이엔지 회사소개 홈페이지

정적 HTML 사이트. 빌드 과정 없이 GitHub Pages에서 그대로 서비스된다.

## 파일 구조
- `index.html` 메인 / `about.html` 회사소개 / `business.html` 사업분야 / `projects.html` 시공실적 / `process.html` 사업절차
- `style.css` 공통 스타일 (전 페이지 공유)
- `img/` 현장 사진
- `build_sub.py` 서브페이지 4개를 공통 틀로 다시 생성하는 스크립트 (헤더·푸터·연락처를 한 번에 바꿀 때 사용). 실행: `python3 build_sub.py`

## 수정 방법
1. 파일을 고친 뒤 커밋·푸시하면 1~2분 내 사이트에 반영된다.
2. 시공실적 추가: `build_sub.py`의 `PROJECTS` 목록에 한 줄 추가 후 실행 → `projects.html` 재생성. 메인(`index.html`)의 실적 카드·수치는 직접 수정.
3. 전화·이메일 등 연락처: `index.html`과 `build_sub.py` 두 곳의 `000-0000-0000`, `info@gaoneng.co.kr`을 교체 후 실행.

## 미확정 항목 (가온이엔지 확인 필요)
대표전화·팩스·이메일, 로고 원본, 전기공사업 등록번호, 2025~2026 실적, 갤러리 사진 중 실적표 미등재 현장의 시공 여부
