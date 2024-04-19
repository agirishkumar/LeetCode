class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        ans = 0
        n = len(arr)
        step = gcd(n, k)
        for i in range(step):
            nums = arr[i::step]
            nums.sort()
            median_idx = len(nums)//2
            median = nums[median_idx]
            for num in nums[:median_idx]:
                ans += median - num
            for num in nums[median_idx:]:
                ans += num - median
        return ans
        