"""
https://projecteuler.net/problem=43
"""
import itertools

def generate_pandigital_nums() -> list[int]:
    permutations_list = list(itertools.permutations([i for i in range(10)]))
    return permutations_list

def is_divisible(v):
    primes = [2, 3, 5, 7, 11, 13, 17]
    i = 1
    while i < 8:
        val = 100*v[i] + 10*v[i+1] + v[i+2]
        if val % primes[i-1] != 0:
            return False
        i+=1
    
    return True

def get_num(v):
    return int("".join(map(str, v)))

def solve() -> int:
    l = generate_pandigital_nums()
    ans = 0
    for v in l:
        if v[0] == 0:
            continue
        if is_divisible(v):
            ans += get_num(v)
    
    return ans

if __name__ == "__main__":
    print(solve())


    
            
