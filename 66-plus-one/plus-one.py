class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        d = ''
        for i in digits:
            d += str(i)
        
        d = list(str(int(d)+1))

        for i in range(len(d)):
            d[i] = int(d[i])

        return d

