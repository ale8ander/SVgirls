# tools/employment_tools.py

import httpx
from typing import Any, Dict
from server import mcp


@mcp.tool()
async def get_employment_by_sector(country: str, year: int) -> Dict[str, Any]:
    """
    Return employment data by sector (Services, Agriculture, Industry) from World Bank.

    Args:
        country: ISO 2- or 3-letter country code (e.g., 'US', 'USA', 'KR', 'KOR').
        year: Four-digit year (>=1991).

    Returns:
        JSON dict with country, year, sector-wise employment percentages, and source info.
        Each sector includes the percentage of total employment and indicator code.
    """
    if not (2 <= len(country.strip()) <= 3):
        return {"error": "country must be ISO-2 or ISO-3 code (e.g., 'US' or 'USA')."}
    if not (1991 <= int(year) <= 2100):
        return {"error": "year must be between 1991 and 2100."}

    code = country.strip().upper()

    # World Bank Employment Indicators
    indicators = {
        "services": "SL.SRV.EMPL.ZS",      # Employment in services (% of total employment)
        "agriculture": "SL.AGR.EMPL.ZS",   # Employment in agriculture (% of total employment)
        "industry": "SL.IND.EMPL.ZS"       # Employment in industry (% of total employment)
    }

    results = {}
    errors = []
    country_name = None

    async with httpx.AsyncClient(headers={"User-Agent": "mcp-worldbank-employment/1.0"}) as client:
        for sector, indicator_code in indicators.items():
            url = (
                f"https://api.worldbank.org/v2/country/{code}"
                f"/indicator/{indicator_code}?date={year}:{year}&format=json"
            )

            try:
                resp = await client.get(url, timeout=20.0)

                if resp.status_code != 200:
                    errors.append(f"{sector}: HTTP {resp.status_code}")
                    continue

                data = resp.json()
                records = data[1] if isinstance(data, list) and len(data) > 1 and isinstance(data[1], list) else []
                entry = records[0] if records else None

                if entry:
                    # Extract country name from first successful response
                    if not country_name:
                        country_name = (entry.get("country") or {}).get("value", code)

                    value = entry.get("value")
                    indicator_name = (entry.get("indicator") or {}).get("value", f"{sector.capitalize()} employment")

                    results[sector] = {
                        "percentage": value,
                        "indicator": indicator_code,
                        "indicatorName": indicator_name
                    }
                else:
                    results[sector] = {
                        "percentage": None,
                        "indicator": indicator_code,
                        "message": f"No data available for {year}"
                    }

            except Exception as e:
                errors.append(f"{sector}: {str(e)}")

    # Build response
    response = {
        "country": country_name or code,
        "countryCode": code,
        "year": int(year),
        "employment_by_sector": results,
        "source": "World Bank Open Data",
        "api_base": f"https://api.worldbank.org/v2/country/{code}/indicator/"
    }

    if errors:
        response["errors"] = errors

    # Add summary if all data is available
    if all(results.get(s, {}).get("percentage") is not None for s in ["services", "agriculture", "industry"]):
        total = sum(results[s]["percentage"] for s in ["services", "agriculture", "industry"])
        response["summary"] = {
            "total_percentage": round(total, 2),
            "note": "Percentages should sum to approximately 100%"
        }

    return response


@mcp.tool()
async def get_employment_ratio(country: str, year: int) -> Dict[str, Any]:
    """
    Return the employment-to-population ratio from World Bank.

    Args:
        country: ISO 2- or 3-letter country code (e.g., 'US', 'USA', 'KR', 'KOR').
        year: Four-digit year (>=1991).

    Returns:
        JSON dict with employment-to-population ratio (% of population aged 15+).
    """
    if not (2 <= len(country.strip()) <= 3):
        return {"error": "country must be ISO-2 or ISO-3 code (e.g., 'US' or 'USA')."}
    if not (1991 <= int(year) <= 2100):
        return {"error": "year must be between 1991 and 2100."}

    code = country.strip().upper()
    indicator_code = "SL.EMP.TOTL.SP.ZS"  # Employment to population ratio, 15+, total (%)

    url = (
        f"https://api.worldbank.org/v2/country/{code}"
        f"/indicator/{indicator_code}?date={year}:{year}&format=json"
    )

    async with httpx.AsyncClient(headers={"User-Agent": "mcp-worldbank-employment/1.0"}) as client:
        resp = await client.get(url, timeout=20.0)

    if resp.status_code != 200:
        return {"error": f"World Bank request failed: HTTP {resp.status_code}", "api": url}

    data = resp.json()
    records = data[1] if isinstance(data, list) and len(data) > 1 and isinstance(data[1], list) else []
    entry = records[0] if records else None

    if not entry or entry.get("value") is None:
        return {
            "message": f"No employment ratio data found for {code} in {year}.",
            "countryCode": code,
            "year": year,
            "indicator": indicator_code,
            "api": url,
        }

    return {
        "country": (entry.get("country") or {}).get("value", code),
        "countryCode": code,
        "year": int(year),
        "indicator": indicator_code,
        "indicatorName": (entry.get("indicator") or {}).get("value", "Employment to population ratio"),
        "ratio": entry.get("value"),
        "unit": "% of total population ages 15+",
        "source": "World Bank Open Data",
        "api": url,
    }


@mcp.tool()
async def get_unemployment_rate(country: str, year: int) -> Dict[str, Any]:
    """
    Return the unemployment rate from World Bank.

    Args:
        country: ISO 2- or 3-letter country code (e.g., 'US', 'USA', 'KR', 'KOR').
        year: Four-digit year (>=1991).

    Returns:
        JSON dict with unemployment rate (% of total labor force).
    """
    if not (2 <= len(country.strip()) <= 3):
        return {"error": "country must be ISO-2 or ISO-3 code (e.g., 'US' or 'USA')."}
    if not (1991 <= int(year) <= 2100):
        return {"error": "year must be between 1991 and 2100."}

    code = country.strip().upper()
    indicator_code = "SL.UEM.TOTL.ZS"  # Unemployment, total (% of total labor force)

    url = (
        f"https://api.worldbank.org/v2/country/{code}"
        f"/indicator/{indicator_code}?date={year}:{year}&format=json"
    )

    async with httpx.AsyncClient(headers={"User-Agent": "mcp-worldbank-employment/1.0"}) as client:
        resp = await client.get(url, timeout=20.0)

    if resp.status_code != 200:
        return {"error": f"World Bank request failed: HTTP {resp.status_code}", "api": url}

    data = resp.json()
    records = data[1] if isinstance(data, list) and len(data) > 1 and isinstance(data[1], list) else []
    entry = records[0] if records else None

    if not entry or entry.get("value") is None:
        return {
            "message": f"No unemployment data found for {code} in {year}.",
            "countryCode": code,
            "year": year,
            "indicator": indicator_code,
            "api": url,
        }

    return {
        "country": (entry.get("country") or {}).get("value", code),
        "countryCode": code,
        "year": int(year),
        "indicator": indicator_code,
        "indicatorName": (entry.get("indicator") or {}).get("value", "Unemployment rate"),
        "rate": entry.get("value"),
        "unit": "% of total labor force",
        "source": "World Bank Open Data",
        "api": url,
    }
