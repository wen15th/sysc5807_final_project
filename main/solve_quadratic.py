import cmath

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("a cannot be zero")
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root1 = f"{root1.real:.2f}{root1.imag:+.2f}j"
    root2 = f"{root2.real:.2f}{root2.imag:+.2f}j"
    return [root1, root2]
