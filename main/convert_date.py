from datetime import datetime

def convert_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

# print(convert_date("2025-20-10"))