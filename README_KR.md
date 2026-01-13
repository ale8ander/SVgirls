# MCP World Bank 고용 데이터 서버

World Bank의 고용 데이터에 접근할 수 있는 Model Context Protocol (MCP) 서버입니다.

## 기능

이 서버는 World Bank 고용 데이터를 조회하기 위한 3가지 주요 도구를 제공합니다:

### 1. `get_employment_by_sector`
산업별 고용 분포(서비스업, 농업, 제조업)를 반환합니다.

**파라미터:**
- `country` (str): ISO 2자 또는 3자 국가 코드 (예: 'US', 'KR', 'IND')
- `year` (int): 4자리 연도 (1991년 이후)

**반환값:**
- 서비스업, 농업, 제조업의 고용 비율
- 합계 요약 (약 100%가 되어야 함)
- 지표 코드 및 메타데이터

**예시:**
```json
{
  "country": "United States",
  "countryCode": "US",
  "year": 2020,
  "employment_by_sector": {
    "services": {
      "percentage": 79.5,
      "indicator": "SL.SRV.EMPL.ZS",
      "indicatorName": "Employment in services (% of total employment)"
    },
    "agriculture": {
      "percentage": 1.3,
      "indicator": "SL.AGR.EMPL.ZS",
      "indicatorName": "Employment in agriculture (% of total employment)"
    },
    "industry": {
      "percentage": 19.2,
      "indicator": "SL.IND.EMPL.ZS",
      "indicatorName": "Employment in industry (% of total employment)"
    }
  },
  "summary": {
    "total_percentage": 100.0,
    "note": "Percentages should sum to approximately 100%"
  }
}
```

### 2. `get_employment_ratio`
고용-인구 비율을 반환합니다.

**파라미터:**
- `country` (str): ISO 2자 또는 3자 국가 코드
- `year` (int): 4자리 연도 (1991년 이후)

**반환값:**
- 고용-인구 비율 (15세 이상 인구 대비 %)

### 3. `get_unemployment_rate`
실업률을 반환합니다.

**파라미터:**
- `country` (str): ISO 2자 또는 3자 국가 코드
- `year` (int): 4자리 연도 (1991년 이후)

**반환값:**
- 실업률 (전체 노동력 대비 %)

## 설치

### 사전 요구사항
- Python 3.10 이상

### 설정

1. **저장소 클론:**
```bash
git clone https://github.com/ale8ander/SVgirls.git
cd SVgirls
```

2. **가상환경 생성:**

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. **의존성 설치:**
```bash
pip install mcp httpx
```

4. **설치 확인:**
```bash
python main.py
```
Ctrl+C로 종료. 에러가 없으면 설치 성공!

## Claude Desktop에서 사용하기

Claude Desktop이 필요할 때 자동으로 서버를 실행합니다. 수동으로 시작할 필요 없습니다.

## Claude Desktop 설정

### 1. 프로젝트 경로 찾기

프로젝트 폴더에서 실행:
```bash
pwd
```
전체 경로 복사 (예: `/Users/yourname/projects/SVgirls`)

### 2. Claude Desktop 설정 파일 열기

설정 파일 위치:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 3. 설정 추가

**macOS/Linux:**
```json
{
  "mcpServers": {
    "worldbank-employment": {
      "command": "/당신의/경로/SVgirls/.venv/bin/python",
      "args": ["/당신의/경로/SVgirls/main.py"]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "worldbank-employment": {
      "command": "C:/당신의/경로/SVgirls/.venv/Scripts/python.exe",
      "args": ["C:/당신의/경로/SVgirls/main.py"]
    }
  }
}
```

**`/당신의/경로/SVgirls`를 1단계에서 복사한 실제 경로로 바꾸세요.**

예시:
```json
{
  "mcpServers": {
    "worldbank-employment": {
      "command": "/Users/john/projects/SVgirls/.venv/bin/python",
      "args": ["/Users/john/projects/SVgirls/main.py"]
    }
  }
}
```

### 4. Claude Desktop 재시작

Claude Desktop을 완전히 종료하고 다시 시작하세요.

## 사용된 World Bank 지표

- **SL.SRV.EMPL.ZS**: 서비스업 고용 (전체 고용의 %)
- **SL.AGR.EMPL.ZS**: 농업 고용 (전체 고용의 %)
- **SL.IND.EMPL.ZS**: 제조업 고용 (전체 고용의 %)
- **SL.EMP.TOTL.SP.ZS**: 고용-인구 비율, 15세 이상, 전체 (%)
- **SL.UEM.TOTL.ZS**: 실업률, 전체 (전체 노동력의 %)

## 예시 쿼리

Claude Desktop에 설정 후, 다음과 같이 질문할 수 있습니다:

- "2020년 한국의 산업별 고용 분포는 어땠어?"
- "2019년 미국과 인도의 서비스업 고용을 비교해줘"
- "2015년부터 2020년까지 일본의 실업률을 보여줘"
- "2022년 독일의 고용-인구 비율은?"

## 데이터 출처

모든 데이터는 [World Bank Open Data API](https://data.worldbank.org/)에서 제공됩니다.

## 테스트

서버가 제대로 작동하는지 테스트하려면:

```bash
python test_tools.py
```

이 스크립트는 세 가지 도구를 모두 테스트하고 실제 World Bank API에서 데이터를 가져옵니다.

## 문제 해결

### MCP 서버가 Claude Desktop에 연결되지 않는 경우:

1. **설정 파일 경로 확인**
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - 파일이 존재하고 올바른 JSON 형식인지 확인

2. **절대 경로 확인**
   ```bash
   # 프로젝트 폴더에서 실행
   pwd
   ```
   - 설정 파일의 경로와 일치하는지 확인

3. **Python/uv 설치 확인**
   ```bash
   which uv
   which python
   ```

4. **수동으로 서버 실행 테스트**
   ```bash
   cd /your/path/to/SVgirls
   uv run main.py
   # 또는
   python main.py
   ```
   - 오류가 나타나면 의존성을 다시 설치

5. **Claude Desktop 완전 재시작**
   - macOS: Cmd+Q로 완전 종료 후 재실행
   - Windows: 작업 관리자에서 프로세스 종료 후 재실행

6. **Claude Desktop 로그 확인**
   - Claude Desktop 메뉴 → Help → Show Logs
   - MCP 관련 오류 메시지 확인

## 라이선스

MIT

## 제작자

World Bank 고용 데이터 분석을 위해 제작됨
