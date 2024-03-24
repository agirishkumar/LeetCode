class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
    
        prev = self.countAndSay(n-1)
        n = len(prev)
        res = ""
        count = 1
        
        for i in range(n):
            if i == n-1 or prev[i] != prev[i+1]:
                res += str(count) + prev[i]
                count = 1
            else:
                count += 1
        
        return res
        