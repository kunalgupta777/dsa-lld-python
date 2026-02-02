"""
Longest Increasing Subsequence
"""
def lis_dp(nums: list[int]) -> tuple(int, list[int]):
    """
    O(n^2)
    """
    n = len(nums)
    dp = [(1, [nums[i]]) for i in range(n)]
    lis = []
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i][0] < dp[j][0] + 1:
                    dp[i] = (dp[j][0] + 1, dp[j][1] + [nums[i]])
                    lis = dp[i][1]
    return len(lis), lis


def lis_bs(nums: list[int]) -> int:
    """
    O(nlogn)
    """
    n = len(nums)
    tails = [nums[0]]
    for i in range(1, n):
        if nums[i] > tails[-1]:
            tails.append(nums[i])
        else:
            low = 0
            high = len(tails)-1
            while low <= high:
                mid = (low + high)//2
                if tails[mid] >= nums[i]:
                    high = mid - 1
                else:
                    low = mid + 1
            tails[low] = nums[i]
    return len(tails)

if __name__ == "__main__":
    nums = [1, 4, 8, 4, 10, 3, 11, 15, 14, 20]
    l, lis = lis_dp(nums=nums)
    print("LIS (DP) is:", l, lis)
    l2 = lis_bs(nums=nums)
    print("LIS (BS) is:", l2)