# test_tools.py
"""
Simple test script to verify the employment tools work correctly.
Run this after installing dependencies.
"""

import asyncio
import sys
sys.path.insert(0, '.')

from tools.employment_tools import (
    get_employment_by_sector,
    get_employment_ratio,
    get_unemployment_rate
)


async def test_employment_by_sector():
    """Test the get_employment_by_sector tool"""
    print("\n=== Testing get_employment_by_sector ===")

    # Test with United States, 2020
    result = await get_employment_by_sector("US", 2020)
    print(f"\nUS Employment by Sector (2020):")
    print(f"Country: {result.get('country')}")
    print(f"Year: {result.get('year')}")

    if 'employment_by_sector' in result:
        for sector, data in result['employment_by_sector'].items():
            percentage = data.get('percentage')
            if percentage is not None:
                print(f"  {sector.capitalize()}: {percentage:.2f}%")
            else:
                print(f"  {sector.capitalize()}: No data available")

    if 'summary' in result:
        print(f"\nTotal: {result['summary']['total_percentage']}%")

    return result


async def test_employment_ratio():
    """Test the get_employment_ratio tool"""
    print("\n=== Testing get_employment_ratio ===")

    # Test with South Korea, 2019
    result = await get_employment_ratio("KR", 2019)
    print(f"\nSouth Korea Employment Ratio (2019):")
    print(f"Country: {result.get('country')}")
    print(f"Ratio: {result.get('ratio')}%")
    print(f"Unit: {result.get('unit')}")

    return result


async def test_unemployment_rate():
    """Test the get_unemployment_rate tool"""
    print("\n=== Testing get_unemployment_rate ===")

    # Test with Japan, 2021
    result = await get_unemployment_rate("JP", 2021)
    print(f"\nJapan Unemployment Rate (2021):")
    print(f"Country: {result.get('country')}")
    print(f"Rate: {result.get('rate')}%")
    print(f"Unit: {result.get('unit')}")

    return result


async def main():
    """Run all tests"""
    print("Starting World Bank Employment Tools Tests...")
    print("=" * 60)

    try:
        await test_employment_by_sector()
        await test_employment_ratio()
        await test_unemployment_rate()

        print("\n" + "=" * 60)
        print("All tests completed successfully!")
        print("\nNote: If any data shows 'None', it means that specific")
        print("indicator is not available for that country/year combination.")

    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
