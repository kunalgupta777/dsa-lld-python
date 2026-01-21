"""
There is a three-digit combination lock (like a suitcase lock) .Find the number of distinct combinations that will open the lock.
Each digit rotates in a circular fashion, for example, 0, 1, 2, 3, ...,  (numOptions - 1), 0, 1, 2, ...

There are two lock combinations that can unlock this, one set by the user and the other is a bypass combination.

The tolerance of error is "tolerance", meaning as long as each digit is within "tolerance" of the set number, the lock will open. 
A tolerance of 0 requires an exact match for the combination.

For example, if numOptions is 10 and tolerance is 2, with the user and the bypass combinations of:
[0 1 2] -> 1 1 1 would open
[3 4 5]

then either [0 9 4] or [1 3 7] can open the lock, but [0 4 5] will not.

Write a function to output the number of distinct lock combinations (mathematical permutations, since order matters) that can open the lock.

Assuming tolerance <= num_options

"""


from itertools import combinations


def get_range(num, tolerance, num_options):
    """
    left <= num <= right
    num - tolerance = left
    num + tolerance = right
    wrap around if left and right become > num_options and < 0
    """
    rg = []
    if num - tolerance < 0:
        for i in range(num_options - (tolerance - num), num_options):
            rg.append(i)
        for i in range(num+1):
            rg.append(i)
    else:
        for i in range(num - tolerance, num+1):
            rg.append(i)
    
    if num + tolerance > num_options:
        for i in range(num+1, num_options):
            rg.append(i)
        for i in range(num + tolerance - num_options + 1):
            rg.append(i)
    else:
        for i in range(num+1, num+tolerance+1):
            rg.append(i)
    
    return sorted(list(set(rg)))


def generate_combinations(range):
    combs = set()
    for x in range[0]:
        for y in range[1]:
            for z in range[2]:
                combs.add((x, y, z))
    return combs

def get_all_unlock_combinations(user_unlock, bypass_unlock, num_options, tolerance):
    user_unlock_ranges = []
    bypass_unlock_ranges = []

    for num in user_unlock:
        user_unlock_ranges.append(get_range(num, tolerance, num_options))
    for num in bypass_unlock:
        bypass_unlock_ranges.append(get_range(num, tolerance, num_options))

    user_unlock_combinations = generate_combinations(user_unlock_ranges)
    bypass_unlock_combinations = generate_combinations(bypass_unlock_ranges)

    all_combinations = user_unlock_combinations.union(bypass_unlock_combinations)
    return [list(comb) for comb in all_combinations]


if __name__ == "__main__":
    user_unlock = [0, 1, 2]
    bypass_unlock = [3, 4, 5]
    num_options = 10
    tolerance = 2

    combinations = get_all_unlock_combinations(user_unlock, bypass_unlock, num_options, tolerance)
    for combination in sorted(combinations):
        print(combination)

    




