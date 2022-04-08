def truncate(number: float, after_comma_digits: int):
    n = str(number)
    if "." not in n:
        return n
    comma_index = n.find(".")
    decimals = len(n[comma_index + 1 :])
    if decimals < after_comma_digits:
        return n + "".join(["0" for _ in range(after_comma_digits - decimals)])
    return n[0 : comma_index + after_comma_digits + 1]
