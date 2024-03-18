class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = [[]]
        for i in range(1,len(nums)+1):
            res = list(itertools.combinations(nums,i))
            temp.extend([list(combination) for combination in res])
        return temp
        