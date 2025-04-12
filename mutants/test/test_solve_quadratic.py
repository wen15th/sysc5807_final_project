import pytest
import itertools
from itertools import product
from allpairspy import AllPairs
from main.solve_quadratic import solve_quadratic


############################### Combinatorial Testing ###############################
# Define value list for each parameter
a_values = [0, 1, 2]  # a == 0 should raise error
b_values = [-3, 0, 1]
c_values = [-1, 0, 2]
# a_values = range(-10, 11)  # a == 0 should raise error
# b_values = range(-10, 11)
# c_values = range(-10, 11)
pairwise_cases = list(AllPairs([a_values, b_values, c_values]))
@pytest.mark.parametrize("a, b, c", pairwise_cases)
def test_solve_quadratic_pairwise(a, b, c):
    try:
        result = solve_quadratic(a, b, c)
        assert verify_roots_match_delta_type(a, b, c, result)
    except ValueError as e:
        if a == 0:
            assert str(e) == 'a cannot be zero'
        else:
            raise RuntimeError(e)


############################### Category-Partition Testing ###############################

# Generate test cases by Category Partition
def generate_cases_by_category_partition():
    a_choices = [0, 1, 2]  # Zero (invalid), Valid non-zero
    b_choices = [-3, 0, 1]  # Negative, Zero, Positive
    c_choices = [-1, 0, 2]  # Zero, Positive
    cases = []
    for a, b, c in product(a_choices, b_choices, c_choices):
        print(a, b, c)
        if a == 0:
            expected = "error"  # constraint: should raise error
        else:
            expected = "valid"  # test delta-related root logic
        cases.append((a, b, c, expected))
    return cases

@pytest.mark.parametrize("a, b, c, expected", generate_cases_by_category_partition())
def test_solve_quadratic_from_category_partition(a, b, c, expected):
    if expected == "error":
        with pytest.raises(ValueError) as exc_info:
            solve_quadratic(a, b, c)
        assert str(exc_info.value) == 'a cannot be zero'
    else:
        result = solve_quadratic(a, b, c)
        assert verify_roots_match_delta_type(a, b, c, result)


def verify_roots_match_delta_type(a, b, c, roots):
    delta = b**2 - 4*a*c
    r1, r2 = roots
    # convert r1, r2 to complex format
    r1, r2 = complex(r1), complex(r2)
    if delta > 0:
        # r1, r2 are real roots, but their values are not same
        return r1.imag == 0 and r2.imag == 0 and r1.real != r2.real
    elif delta == 0:
        # r1, r2 are real roots, and they equal to each other
        return r1.imag == 0 and r2.imag == 0 and r1.real == r2.real
    else:  # delta < 0
        return r1.real == r2.real and r1.imag == -r2.imag and r1.imag != 0