class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        d = []
        for i in range(len(arr)-1):
            d.append(arr[i+1]-arr[i])
        
        if len(set(d)) == 1:
            return True
        return False