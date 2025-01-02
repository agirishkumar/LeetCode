from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        max_beauty = 1  
        while r < len(nums):
            
            while r < len(nums) and nums[r] - nums[l] <= 2 * k: 
                r += 1
            
            max_beauty = max(max_beauty, r - l) 
            l += 1  
        return max_beauty