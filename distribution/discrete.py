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


def hypergeometric(x, N, n, k):
    """
    x: number of successes in n trials
    N: number of trials
    n: number of trials chosen from N
    k: number of successes in N trials
    """
    success_comb = tools.binomial_coefficient(k, x)
    failure_comb = tools.binomial_coefficient(N - k, n - x)
    total_comb = tools.binomial_coefficient(N, n)
    return success_comb * failure_comb / total_comb
