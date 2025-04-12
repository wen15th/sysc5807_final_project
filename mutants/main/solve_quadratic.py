
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


import cmath

def x_solve_quadratic__mutmut_orig(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_1(a, b, c):
    if a != 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_2(a, b, c):
    if a == 1:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_3(a, b, c):
    if a == 0:
        raise ValueError("XXa cannot be zeroXX")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_4(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b * 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_5(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 3 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_6(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 + 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_7(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 5 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_8(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 / a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_9(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a / c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_10(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = None
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_11(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (+b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_12(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_13(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(None)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_14(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) * (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_15(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (3*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_16(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2/a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_17(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = None
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_18(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (+b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_19(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_20(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(None)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_21(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) * (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_22(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (3*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_23(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2/a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_24(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = None
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_25(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = None
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]

def x_solve_quadratic__mutmut_26(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = None
    return [root1, root2]

x_solve_quadratic__mutmut_mutants = {
'x_solve_quadratic__mutmut_1': x_solve_quadratic__mutmut_1, 
    'x_solve_quadratic__mutmut_2': x_solve_quadratic__mutmut_2, 
    'x_solve_quadratic__mutmut_3': x_solve_quadratic__mutmut_3, 
    'x_solve_quadratic__mutmut_4': x_solve_quadratic__mutmut_4, 
    'x_solve_quadratic__mutmut_5': x_solve_quadratic__mutmut_5, 
    'x_solve_quadratic__mutmut_6': x_solve_quadratic__mutmut_6, 
    'x_solve_quadratic__mutmut_7': x_solve_quadratic__mutmut_7, 
    'x_solve_quadratic__mutmut_8': x_solve_quadratic__mutmut_8, 
    'x_solve_quadratic__mutmut_9': x_solve_quadratic__mutmut_9, 
    'x_solve_quadratic__mutmut_10': x_solve_quadratic__mutmut_10, 
    'x_solve_quadratic__mutmut_11': x_solve_quadratic__mutmut_11, 
    'x_solve_quadratic__mutmut_12': x_solve_quadratic__mutmut_12, 
    'x_solve_quadratic__mutmut_13': x_solve_quadratic__mutmut_13, 
    'x_solve_quadratic__mutmut_14': x_solve_quadratic__mutmut_14, 
    'x_solve_quadratic__mutmut_15': x_solve_quadratic__mutmut_15, 
    'x_solve_quadratic__mutmut_16': x_solve_quadratic__mutmut_16, 
    'x_solve_quadratic__mutmut_17': x_solve_quadratic__mutmut_17, 
    'x_solve_quadratic__mutmut_18': x_solve_quadratic__mutmut_18, 
    'x_solve_quadratic__mutmut_19': x_solve_quadratic__mutmut_19, 
    'x_solve_quadratic__mutmut_20': x_solve_quadratic__mutmut_20, 
    'x_solve_quadratic__mutmut_21': x_solve_quadratic__mutmut_21, 
    'x_solve_quadratic__mutmut_22': x_solve_quadratic__mutmut_22, 
    'x_solve_quadratic__mutmut_23': x_solve_quadratic__mutmut_23, 
    'x_solve_quadratic__mutmut_24': x_solve_quadratic__mutmut_24, 
    'x_solve_quadratic__mutmut_25': x_solve_quadratic__mutmut_25, 
    'x_solve_quadratic__mutmut_26': x_solve_quadratic__mutmut_26
}

def solve_quadratic(*args, **kwargs):
    result = _mutmut_trampoline(x_solve_quadratic__mutmut_orig, x_solve_quadratic__mutmut_mutants, *args, **kwargs)
    return result 

solve_quadratic.__signature__ = _mutmut_signature(x_solve_quadratic__mutmut_orig)
x_solve_quadratic__mutmut_orig.__name__ = 'x_solve_quadratic'


