import math


def binomial_coefficient(n: int, k: int) -> int:
    n_fac = math.factorial(n)
    k_fac = math.factorial(k)
    n_minus_k_fac = math.factorial(n - k)
    return n_fac / (k_fac * n_minus_k_fac)
