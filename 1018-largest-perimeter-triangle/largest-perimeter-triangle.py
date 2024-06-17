class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        tot=0
       
        for i in range(len(nums)-2):
            if nums[i+1]+nums[i+2] >nums[i]:
                tot=nums[i] + nums[i+1] + nums[i+2]
                break
                
        return tot if tot else 0

        