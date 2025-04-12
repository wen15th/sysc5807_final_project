import pytest
from datetime import datetime
from allpairspy import AllPairs
from itertools import product
from typing import List, Tuple
from main.convert_date import convert_date


############################### Combinatorial Testing ###############################

def generate_pairwise_cases():
    years = [1900, 2099, 1899, 1901, 2089, 2100, 2025, "aaaa"]
    months = [0, 1, 2, 6, 12, 13, "bb"]
    days = [0, 1, 2, 15, 28, 29, 30, 31, 32, "cc"]

    parameters = [years, months, days]
    cases = []

    for y, m, d in AllPairs(parameters):
        try:
            date_str = f"{y:04d}-{m:02d}-{d:02d}"
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            if dt.year < 1900 or dt.year > 2099:
                expected = "Invalid year"
            else:
                expected = dt.strftime("%d/%m/%Y")
        except Exception:
            # fallback string when formatting fails
            date_str = f"{y}-{m}-{d}"
            expected = "Invalid input format"

        cases.append((date_str, expected))

    return cases

# Combinatorial Testing
@pytest.mark.parametrize("input_date, expected", generate_pairwise_cases())
def test_combinatorial_generated(input_date, expected):
    if "Invalid" in expected:
        with pytest.raises(ValueError) as exc_info:
            convert_date(input_date)
        assert str(exc_info.value) == expected
    else:
        assert convert_date(input_date) == expected


############################### Category-Partition Testing ###############################
"""
    Build date string by combining year, month and day，

    return:
        List of (category, input_str, expected_output)
"""
def generate_convert_date_cases_by_partition() -> List[Tuple[str, str, str]]:
    # value list
    # valid year / month / day, out of range, non-numerical
    years = [1900, 2099, 1899, 1901, 2089, 2100, 2025, "aaaa"]
    months = [0, 1, 2, 6, 12, 13, "bb"]
    days = [0, 1, 2, 15, 28, 29, 30, 31, 32, "cc"]
    cases = []
    for y, m, d in product(years, months, days):
        # constraints
        if not (str(y).isdigit() and str(m).isdigit() and str(d).isdigit()):
            continue
        try:
            y_str = f"{int(y):04d}"
            m_str = f"{int(m):02d}"
            d_str = f"{int(d):02d}"
            date_str = f"{y_str}-{m_str}-{d_str}"
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            # constraints
            if dt.year < 1900 or dt.year > 2099:
                expected = "Invalid year"
            else:
                expected = dt.strftime("%d/%m/%Y")
        except (ValueError, TypeError):
            # invalid combinations
            date_str = f"{y}-{m}-{d}"
            expected = "Invalid input format"
        # categories
        category = categorize_convert_date_case(expected)
        cases.append((category, date_str, expected))
    return cases


def categorize_convert_date_case(expected: str) -> str:
    if expected == "Invalid input format":
        return "invalid_format"
    elif expected == "Invalid year":
        return "invalid_years"
    else:
        return "valid_date"


@pytest.mark.parametrize("category, input_str, expected", generate_convert_date_cases_by_partition())
def test_convert_date_partitioned(category, input_str, expected):
    if category == "valid_date":
        assert convert_date(input_str) == expected
    else:
        with pytest.raises(ValueError) as exc_info:
            convert_date(input_str)
        assert str(exc_info.value) == expected