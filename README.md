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

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/ale8ander/SVgirls.git
cd SVgirls
```

2. **Create virtual environment:**

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

3. **Install dependencies:**
```bash
pip install mcp httpx
```

4. **Test the installation:**
```bash
python main.py
```
Press Ctrl+C to stop. If no errors appear, installation is successful!

## Usage with Claude Desktop

Claude Desktop will automatically run the server when needed. You don't need to manually start it.

## Configuration for Claude Desktop

### 1. Find your project path

Navigate to the project folder and run:
```bash
pwd
```
Copy the full path (e.g., `/Users/yourname/projects/SVgirls`)

### 2. Edit Claude Desktop config file

Open the config file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### 3. Add this configuration

**macOS/Linux:**
```json
{
  "mcpServers": {
    "worldbank-employment": {
      "command": "/YOUR/PATH/TO/SVgirls/.venv/bin/python",
      "args": ["/YOUR/PATH/TO/SVgirls/main.py"]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "worldbank-employment": {
      "command": "C:/YOUR/PATH/TO/SVgirls/.venv/Scripts/python.exe",
      "args": ["C:/YOUR/PATH/TO/SVgirls/main.py"]
    }
  }
}
```

**Replace `/YOUR/PATH/TO/SVgirls` with the actual path from step 1.**

Example:
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

### 4. Restart Claude Desktop

Completely quit and restart Claude Desktop for changes to take effect.

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

