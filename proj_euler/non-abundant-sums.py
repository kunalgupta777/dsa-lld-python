"""
https://projecteuler.net/problem=23
"""

def divisors(num: int) -> list[int]:
    l = []
    for i in range(1, num):
        if num % i == 0:
            l.append(i)
    return l

def is_number_abundant(num: int) -> bool:
    return sum(divisors(num)) > num

def solve() -> int:
    nums = []
    for i in range(12, 28124):
        if is_number_abundant(i):
            nums.append(i)
    ans = set([i for i in range(1, 28124)])
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] > 28123:
                break
            else:
                if nums[i] + nums[j] in ans:
                    ans.remove(nums[i] + nums[j])
    
    return sum(list(ans))


if __name__ == "__main__":
    print(solve())