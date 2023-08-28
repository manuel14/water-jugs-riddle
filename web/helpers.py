def division_remainder(a: int, b: int) -> int:
    """
    Iteratively apply mod operations until a is divisible by b

    """
    print(f"a {a}")
    print(f"b {b}")
    if b == 0:
        return a
    return division_remainder(b, a % b)
