# stock-data-mining

한국 거래소 사이트를 매일 같은 시간에 크롤링 해서 정보를 저장하고, 시각화하여 웹사이트로 제작, 배포합니다.

## 목표

- 새싹 LLM 기반 AI 앱 개발 과정에서 배운 스크래핑, 시각화, 데이터 전처리, 플라스크, 깃 사용법을 복습하고자 합니다.
- 팀 프로젝트를 진행하여 협업 프로세스를 익히고자 합니다.

## 기능

- 한국 거래소 사이트의 API를 이용하여 주식 데이터를 크롤링합니다.
- 크롤링을 모니터링하고, 크롤링이 중지되면 메일을 전송합니다.

## 역할 분담

- ~~경건웅: 데이터 크롤링, 플라스크 모델, 뷰, 깃 관리~~
- 박병준: 문서화, 플라스크, DB, 배포 프로세스, 데이터 크롤링, 깃 관리

## 기술 스택

- Git: 버전 관리 프로그램
- Python: 스크래핑, 모니터링 목적의 메일
- Flask: 웹 어플리케이션 서버
- Linux: 반복 작업을 위한 cron job, 배포를 위한 웹 서버
- AWS: 배포 환경 구축
- Slack: 모니터링, 워크플로우 자동화
- Notion: 문서화

## 아키텍쳐

한국 거래소 사이트 -> 스크래핑 -> DB <-> 플라스크 <-> 웹 서버

## 패키지 구조

```
├── scrape_stocks / Script to scrape the top 50 stocks
├── scrape_stock_prices / Script to scrape daily stock prices
├── scrape_stock_financials / Script to scrape stock financials
├── mail.py / Sends an email using Gmail's SMTP server
├── models.py / Database models for stock data
├── requirements.txt / List of package dependencies
└── README.md / Project documentation
```

## 실행 방법

1. Clone repository

```
git clone https://github.com/AlpacaMale/stock-data-mining.git
```

2. Change working directry

```
cd stock-data-mining
```

3. Install dependency

```
pip install -r requirements.txt
```

4. Write your env setup

_.env_

```
URL=''
ACCEPT='*/*'
ACCEPT_LANGUAGE='ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
CONNECTION='keep-alive'
CONTENT_TYPE='application/x-www-form-urlencoded'
COOKIE=''
ORIGIN=''
REFERER=''
USER_AGENT=''
DATABASE_URL="mysql://user:passwd@host:port/database"
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
SENDER_EMAIL="example@email.com"
RECEIVER_EMAIL="example@email.com"
PASSWORD="your password here"
```

5. Set environment path

```
echo 'export PATH=$(pwd):$PATH' >> ~/.bashrc
source ~/.bashrc

```

6. Grant execute permission to the file

```
chmod +x scrape_stocks scrape_stock_prices scrape_stock_financials
```

7. Execute scripts

```
scrape_stocks
scrape_stock_prices
scrpae_stock_financials

```

## 코드 컨벤션

### 깃

| 적용 대상 | 컨벤션                                       |
| --------- | -------------------------------------------- |
| feat      | 새로운 기능 추가                             |
| style     | 코드 스타일 수정 (기능 변경 없음)            |
| fix       | 버그 수정                                    |
| docs      | 문서 수정                                    |
| chore     | 기타 변경(빌드 과정,패키지 매니저 설정 등등) |

### 네이밍 규칙

| 적용 대상                    | 컨벤션           |
| ---------------------------- | ---------------- |
| Class, Exception             | PascalCase       |
| Function, Variable, DB Table | snake_case       |
| CSS Class                    | kebab-case       |
| Constant                     | UPPER_SNAKE_CASE |
| Indent                       | Tab              |
