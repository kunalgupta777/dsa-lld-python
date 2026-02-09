"""
https://projecteuler.net/problem=66
"""
from math import sqrt
from multiprocessing import Pool, cpu_count


def solve_for_d(d: int):
    # Skip perfect squares
    if sqrt(d) == int(sqrt(d)):
        return None

    y = 1
    while True:
        x = sqrt(1 + d * y * y)
        if x == int(x):
            # Return the first solution (d, x)
            return d, int(x)
        y += 1


def solve():
    ds = range(2, 1001)

    with Pool(processes=cpu_count()) as pool:
        results = pool.map(solve_for_d, ds)

    # Filter out skipped/unsolved entries
    results = [r for r in results if r is not None]

    # Print all (d, x) like your original code
    for d, x in results:
        print(d, x)

    # Find the maximum x
    _, max_x = max(results, key=lambda t: t[1])
    return max_x


if __name__ == "__main__":
    print("max_x =", solve())