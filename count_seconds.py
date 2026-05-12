#!/usr/bin/env python3
"""Simple utility to count seconds in a year.

Usage examples:
  python count_seconds.py            # shows seconds for common and leap year
  python count_seconds.py --year 2024
  python count_seconds.py --days 365
"""

import argparse
import calendar

SECS_PER_DAY = 24 * 60 * 60


def seconds_in_days(days: int) -> int:
    return days * SECS_PER_DAY


def seconds_in_year(year: int) -> int:
    days = 366 if calendar.isleap(year) else 365
    return seconds_in_days(days)


def main():
    p = argparse.ArgumentParser(description="Count seconds in a year or given number of days.")
    p.add_argument("--year", "-y", type=int, help="Specify a year (handles leap years)")
    p.add_argument("--days", "-d", type=int, help="Specify number of days to count seconds for")
    args = p.parse_args()

    if args.year:
        secs = seconds_in_year(args.year)
        print(f"Year {args.year}: {'leap year' if calendar.isleap(args.year) else 'common year'}")
        print(f"Seconds: {secs:,}")
        return

    if args.days:
        secs = seconds_in_days(args.days)
        print(f"Days: {args.days}")
        print(f"Seconds: {secs:,}")
        return

    # Default: show both common and leap year values
    common = seconds_in_days(365)
    leap = seconds_in_days(366)
    print("Seconds in a common year (365 days):", f"{common:,}")
    print("Seconds in a leap year (366 days):", f"{leap:,}")


if __name__ == "__main__":
    main()
