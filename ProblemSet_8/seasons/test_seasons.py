import pytest
from datetime import date, timedelta
from seasons import calculate_minutes_since_birth, convert_minutes_to_text

def test_calculate_minutes_since_birth():
    # Assuming today's date is 2023-10-31 for the sake of the examples.
    today = date(2023, 10, 31)

    # Test for one year ago
    one_year_ago = (today - timedelta(days=365)).isoformat()
    assert calculate_minutes_since_birth(one_year_ago) == 525600

    # Test for two years ago
    two_years_ago = (today - timedelta(days=730)).isoformat()
    assert calculate_minutes_since_birth(two_years_ago) == 1051200

    # Test for future date
    one_day_ahead = (today + timedelta(days=1)).isoformat()
    assert calculate_minutes_since_birth(one_day_ahead) == -1440  # 24 hours * 60 minutes = 1440 minutes

def test_convert_minutes_to_text():
    assert convert_minutes_to_text(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_minutes_to_text(1051200) == "One million, fifty-one thousand, two hundred minutes"
    assert convert_minutes_to_text(-1440) == "Minus one thousand, four hundred forty minutes"

def test_future_date():
    # Assuming today's date is 2023-10-31 for the sake of the example.
    today = date(2023, 10, 31)

    # Test for one day in the future
    one_day_ahead = (today + timedelta(days=1)).isoformat()
    assert calculate_minutes_since_birth(one_day_ahead) == -1440  # 24 hours * 60 minutes = 1440 minutes

# We don't test main() as the task specified only testing functions besides main.
