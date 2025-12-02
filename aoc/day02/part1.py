from aoc.utils.common import read_range

def adjust_prefix_bounds(lo, hi):
    """
    Convert raw numeric range [lo, hi] into prefix bounds
    for numbers of form prefixprefix.
    """

    lo_len = len(str(lo))
    hi_len = len(str(hi))

    if lo_len % 2 != 0:
        lo = 10 ** lo_len

    if hi_len % 2 != 0:
        hi = 10 ** (hi_len - 1)-1


    L = len(str(hi))
    half_len = L // 2

    lo_str = str(lo)
    hi_str = str(hi)

    lo_pref, lo_tail = int(lo_str[:half_len]), int(lo_str[half_len:])
    hi_pref, hi_tail = int(hi_str[:half_len]), int(hi_str[half_len:])


    if lo_pref < lo_tail:
        lo_pref += 1


    if hi_pref > hi_tail:
        hi_pref -= 1

    return lo_pref, hi_pref


def sum_repeated_numbers(prefix_lo, prefix_hi):
    """
    Given prefix range [prefix_lo, prefix_hi],
    return sum of prefixprefix for all prefixes.
    """
    base = 10 ** len(str(prefix_lo))
    return sum((p * base + p) for p in range(prefix_lo, prefix_hi + 1))


def find_invalid_sum(lo, hi):
    """
    For a single [lo, hi] range, return sum of all repeated-digit invalid IDs.
    """
    lo_len = len(str(lo))
    hi_len = len(str(hi))


    if lo_len & 1 and hi_len & 1:
        return 0

    prefix_lo, prefix_hi = adjust_prefix_bounds(lo, hi)

    if prefix_lo > prefix_hi:
        return 0

    return sum_repeated_numbers(prefix_lo, prefix_hi)


def solve():
    ranges = read_range()
    total = 0

    for lo, hi in ranges:
        total += find_invalid_sum(lo, hi)

    print(f"The sum of all invalid IDs: {total}")


if __name__ == "__main__":
    solve()
