

# Cách 1: Tính toán cơ bản
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365

total_seconds = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_year

print("=" * 50)
print("CHƯƠNG TRÌNH ĐẾM GIÂY TRONG 1 NĂM")
print("=" * 50)
print(f"Giây trong 1 phút: {seconds_per_minute}")
print(f"Phút trong 1 giờ: {minutes_per_hour}")
print(f"Giờ trong 1 ngày: {hours_per_day}")
print(f"Ngày trong 1 năm: {days_per_year}")
print("-" * 50)
print(f"Tổng giây trong 1 năm: {total_seconds:,}")
print("=" * 50)

# Cách 2: Sử dụng thư viện datetime
from datetime import datetime, timedelta

year = 2024
start_date = datetime(year, 1, 1)
end_date = datetime(year, 12, 31)

diff = end_date - start_date
seconds_in_leap_year = diff.total_seconds() + 86400  # Cộng 1 ngày cuối năm

print(f"\nCách tính cho năm nhuận ({year}):")
print(f"Tổng giây: {int(seconds_in_leap_year):,}")

# Cách 3: Sử dụng timedelta
one_year = timedelta(days=365)
seconds_timedelta = one_year.total_seconds()

print(f"\nSử dụng timedelta (365 ngày):")
print(f"Tổng giây: {int(seconds_timedelta):,}")
