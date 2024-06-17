class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        increasing = True
        decreasing = True
        
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                increasing = False
            if nums[i+1] > nums[i]:
                decreasing = False
        
        return increasing or decreasing
        

        