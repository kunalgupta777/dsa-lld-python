"""
https://projecteuler.net/problem=26
"""

from decimal import Decimal, getcontext

# Set the global precision for all Decimal operations (e.g., to 28 digits)
getcontext().prec = 1000

def get_period(v) -> int:
    res = Decimal('1') / Decimal(str(v))
    return int(res)

def solve() -> int:
    max_period = 0
    for i in range(1, 1000):
        max_period = max(max_period, get_period(i))
    return max_period