def k_sum(arr: list[int], k: int, target: int) -> list[list[int]]:
    n = len(arr)
    arr.sort()
    ans = set()

    def scan_tuples(count: int, start_idx: int, scanned_vals: list[int]) -> None:
        if count == 2:
            l, r = start_idx + 1, n - 1
            while l < r:
                val = sum(scanned_vals) + arr[l] + arr[r]
                if val == target:
                    ans.add(tuple(sorted(scanned_vals + [arr[l], arr[r]])))
                    l += 1
                    r -= 1
                elif val > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(start_idx + 1, n - count + 2):
                scan_tuples(count - 1, i, scanned_vals + [arr[i]])

    scan_tuples(k, 0, [])
    return [list(entry) for entry in ans]


if __name__ == "__main__":
    arr = [-5, 4, 5, -4, 9, 0, 0, 3, 6, -1, -8]
    k = 8
    target = 0
    tuples = k_sum(arr, k, target)
    for t in tuples:
        print(t)
