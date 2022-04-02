from collections import Counter


def mean(x: list[float]) -> float:
    return sum(x) / len(x)


def mode(x: list[float]) -> list[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i in counts.keys() if counts[x_i] == max_count]


def _odd_median(x_sorted):
    return x_sorted[len(x_sorted) // 2]


def _even_median(x_sorted):
    len_x_sorted = len(x_sorted)
    return (x_sorted[len_x_sorted // 2] + x_sorted[len_x_sorted // 2 + 1]) / 2


def median(x):
    x_length = len(x)
    x_sorted = sorted(x)
    return _even_median(x_sorted) if x_length % 2 == 0 else _odd_median(x_sorted)
