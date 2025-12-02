from aoc.utils.common import read_range

def rep_factor(block_len: int, k: int) -> int:
    """
    Compute the multiplier for repeating a prefix k times.
    Example: prefix=123, k=3 => number = 123123123 = prefix * rep_factor
    """
    return (10 ** (block_len * k) - 1) // (10 ** block_len - 1)


def get_prefix_bounds(lo: int, hi: int, block_len: int, k: int):
    """
    For total length L = block_len * k, find all prefixes P such that:
        int(str(P) * k) lies within [lo, hi].

    Returns (prefix_low, prefix_high) or (None, None).
    """
    L = block_len * k

    low_L = max(lo, 10 ** (L - 1))
    high_L = min(hi, 10 ** L - 1)

    if low_L > high_L:
        return None, None

    prefix_lo = 10 ** (block_len - 1)
    prefix_hi = 10 ** block_len - 1

    rf = rep_factor(block_len, k)

    p_start = max(prefix_lo, (low_L + rf - 1) // rf)
    p_end   = min(prefix_hi, high_L // rf)

    if p_start > p_end:
        return None, None

    return p_start, p_end


def find_invalid_sum(lo: int, hi: int) -> int:
    """
    For [lo, hi], find all numbers that are prefix repeated k times (k >= 2).
    Deduplicate using a set, because the same number can appear from multiple
    (block_len, k) combinations.
    """
    invalid_ids = set()

    lo_len = len(str(lo))
    hi_len = len(str(hi))

    for L in range(lo_len, hi_len + 1):
        lower_L = 10 ** (L - 1)
        upper_L = 10 ** L - 1

        if hi < lower_L or lo > upper_L:
            continue

        for block_len in range(1, L // 2 + 1):
            if L % block_len != 0:
                continue

            k = L // block_len
            if k < 2:
                continue

            prefix_range = get_prefix_bounds(lo, hi, block_len, k)
            if prefix_range == (None, None):
                continue

            prefix_low, prefix_high = prefix_range
            rf = rep_factor(block_len, k)

            for prefix in range(prefix_low, prefix_high + 1):
                invalid_ids.add(prefix * rf)

    return sum(invalid_ids)


def solve():
    ranges = read_range()
    total = 0

    for lo, hi in ranges:
        total += find_invalid_sum(lo, hi)

    print(f"The sum of all invalid IDs: {total}")


if __name__ == "__main__":
    solve()
