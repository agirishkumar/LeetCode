class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        charcaters_s = {}

        for i in s:
            if i in charcaters_s:
                charcaters_s[i] += 1
            else:
                charcaters_s[i] = 1
        
        for i in t:
            if i not in charcaters_s or charcaters_s[i] == 0:
                return False
            else:
                charcaters_s[i] -=1
            
        return True

        


        

        