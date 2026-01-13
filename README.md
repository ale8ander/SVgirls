# MCP World Bank Employment Server

**[한국어 README](README_KR.md)**

A Model Context Protocol (MCP) server that provides access to World Bank employment data across different sectors.

## Features

This server provides three main tools for querying World Bank employment data:

### 1. `get_employment_by_sector`
Returns sector-wise employment distribution (Services, Agriculture, Industry).

**Parameters:**
- `country` (str): ISO 2 or 3-letter country code (e.g., 'US', 'KR', 'IND')
- `year` (int): Four-digit year (1991 or later)

**Returns:**
- Employment percentages for Services, Agriculture, and Industry sectors
- Summary showing total percentage (should be ~100%)
- Indicator codes and metadata

**Example:**
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
Returns the employment-to-population ratio.

**Parameters:**
- `country` (str): ISO 2 or 3-letter country code
- `year` (int): Four-digit year (1991 or later)

**Returns:**
- Employment to population ratio (% of population ages 15+)

### 3. `get_unemployment_rate`
Returns the unemployment rate.

**Parameters:**
- `country` (str): ISO 2 or 3-letter country code
- `year` (int): Four-digit year (1991 or later)

**Returns:**
- Unemployment rate (% of total labor force)

## Installation

### Prerequisites
- Python 3.10 or higher
- `pip` (comes with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/ale8ander/SVgirls.git
cd SVgirls
```

2. Create and activate a virtual environment (IMPORTANT!):

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

3. Install dependencies:
```bash
pip install mcp httpx
```

**OR** if you have `uv` installed:
```bash
uv sync
```

### Verify Installation

Test if the server works:
```bash
python main.py
```

You should see MCP server initialization. Press Ctrl+C to stop.

## Running the Server

### Option 1: STDIO Mode (for Claude Desktop or CLI)

```bash
uv run main.py
```

### Option 2: HTTP Server Mode (for web applications)

```bash
uv run main_http.py
```

The server will start on `http://127.0.0.1:8001`:
- MCP endpoint: `http://127.0.0.1:8001/mcp`
- Health check: `http://127.0.0.1:8001/ping`

## Configuration for Claude Desktop

Add this MCP server to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`<br>
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`<br>
**Linux**: `~/.config/Claude/claude_desktop_config.json`<br>

### ⚠️ IMPORTANT: You MUST install dependencies first!

Before configuring Claude Desktop, make sure you:
1. ✅ Cloned the repository
2. ✅ Created a virtual environment (`.venv`)
3. ✅ Activated the virtual environment
4. ✅ Ran `pip install mcp httpx`
5. ✅ Tested with `python main.py`

### Option 1: Using venv Python (RECOMMENDED - Most Reliable)

```json
{
  "mcpServers": {
    "worldbank-employment": {
      "command": "/ABSOLUTE/PATH/TO/SVgirls/.venv/bin/python",
      "args": [
        "/ABSOLUTE/PATH/TO/SVgirls/main.py"
      ]
    }
  }
}
```

**Windows:** Use `.venv/Scripts/python.exe` instead of `.venv/bin/python`

```json
{
  "mcpServers": {
    "worldbank-employment": {
      "command": "C:/ABSOLUTE/PATH/TO/SVgirls/.venv/Scripts/python.exe",
      "args": [
        "C:/ABSOLUTE/PATH/TO/SVgirls/main.py"
      ]
    }
  }
}
```

### Option 2: Using `uv` (If you have uv installed)

```json
{
  "mcpServers": {
    "worldbank-employment": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/SVgirls",
        "run",
        "main.py"
      ]
    }
  }
}
```

**Important:** Replace `/ABSOLUTE/PATH/TO/SVgirls` with your actual project path.

**Path Examples:**

macOS/Linux:
- `/Users/yourname/projects/SVgirls/.venv/bin/python`
- `/home/yourname/SVgirls/.venv/bin/python`

Windows:
- `C:/Users/YourName/Documents/SVgirls/.venv/Scripts/python.exe`

### Finding Your Absolute Path

To find your project's absolute path, navigate to the project folder and run:

**macOS/Linux:**
```bash
pwd
```

**Windows (PowerShell):**
```powershell
pwd
```

**Windows (Command Prompt):**
```cmd
cd
```

After updating the configuration, **restart Claude Desktop** completely for changes to take effect.

## World Bank Indicators Used

- **SL.SRV.EMPL.ZS**: Employment in services (% of total employment)
- **SL.AGR.EMPL.ZS**: Employment in agriculture (% of total employment)
- **SL.IND.EMPL.ZS**: Employment in industry (% of total employment)
- **SL.EMP.TOTL.SP.ZS**: Employment to population ratio, 15+, total (%)
- **SL.UEM.TOTL.ZS**: Unemployment, total (% of total labor force)

## Example Queries

Once configured with Claude Desktop, you can ask:

- "What was the employment distribution across sectors in South Korea in 2020?"
- "Compare the services sector employment between US and India in 2019"
- "Show me the unemployment rate for Japan from 2015 to 2020"
- "What's the employment-to-population ratio in Germany for 2022?"

## Data Source

All data is sourced from the [World Bank Open Data API](https://data.worldbank.org/).

## License

MIT

## Author

Created for World Bank employment data analysis

