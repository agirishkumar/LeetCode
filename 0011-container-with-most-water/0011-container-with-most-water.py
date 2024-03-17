class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        i = 0
        j = len(height)-1

        while i<j:
            width = j-i
            h = 0

            if height[j] > height[i]:
                h = height[i]
                i += 1

            else:
                h = height[j]
                j -= 1

            area = width * h

            maxArea = max(maxArea, area)

        return maxArea





        