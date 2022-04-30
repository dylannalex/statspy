from distribution import tools


def binomial(k, n, p):
    """
    k: number of successes
    n: number of independent experiments
    p: probability of success
    """
    q = 1 - p
    comb = tools.binomial_coefficient(n, k)
    return comb * (p**k) * (q ** (n - k))
