
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from datetime import datetime

def x_convert_date__mutmut_orig(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_1(date_str):
    try:
        dt = datetime.strptime(None, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_2(date_str):
    try:
        dt = datetime.strptime(date_str, "XX%Y-%m-%dXX")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_3(date_str):
    try:
        dt = datetime.strptime( "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_4(date_str):
    try:
        dt = None
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_5(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("XXInvalid input formatXX")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_6(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year <= 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_7(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1901 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_8(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year >= 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_9(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2100:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_10(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 and dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_11(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("XXInvalid yearXX")

    return dt.strftime("%d/%m/%Y")

def x_convert_date__mutmut_12(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid input format")

    if dt.year < 1900 or dt.year > 2099:
        raise ValueError("Invalid year")

    return dt.strftime("XX%d/%m/%YXX")

x_convert_date__mutmut_mutants = {
'x_convert_date__mutmut_1': x_convert_date__mutmut_1, 
    'x_convert_date__mutmut_2': x_convert_date__mutmut_2, 
    'x_convert_date__mutmut_3': x_convert_date__mutmut_3, 
    'x_convert_date__mutmut_4': x_convert_date__mutmut_4, 
    'x_convert_date__mutmut_5': x_convert_date__mutmut_5, 
    'x_convert_date__mutmut_6': x_convert_date__mutmut_6, 
    'x_convert_date__mutmut_7': x_convert_date__mutmut_7, 
    'x_convert_date__mutmut_8': x_convert_date__mutmut_8, 
    'x_convert_date__mutmut_9': x_convert_date__mutmut_9, 
    'x_convert_date__mutmut_10': x_convert_date__mutmut_10, 
    'x_convert_date__mutmut_11': x_convert_date__mutmut_11, 
    'x_convert_date__mutmut_12': x_convert_date__mutmut_12
}

def convert_date(*args, **kwargs):
    result = _mutmut_trampoline(x_convert_date__mutmut_orig, x_convert_date__mutmut_mutants, *args, **kwargs)
    return result 

convert_date.__signature__ = _mutmut_signature(x_convert_date__mutmut_orig)
x_convert_date__mutmut_orig.__name__ = 'x_convert_date'



# print(convert_date("2025-20-10"))
