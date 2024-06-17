class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxPer = 0
        for i in range(2,len(nums)):
            if nums[i] < nums[i-2] + nums[i-1]:
                maxPer = max(maxPer , nums[i-2] + nums[i-1]+ nums[i])
        return maxPer

        