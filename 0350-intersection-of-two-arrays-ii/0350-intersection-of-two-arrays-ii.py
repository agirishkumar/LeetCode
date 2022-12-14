class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = {}
        y = {}
        ans = []
        for i in nums1:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        for i in nums2:
            if i in y:
                y[i] += 1
            else:
                y[i] = 1
        for i in x:
            if i in y:
                for p in range(min(x[i],y[i])):
                    ans.append(i)
        return ans
        
        