class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split('.')
        l2 = version2.split('.')
        n = max(len(l1),len(l2))
        l1+=[0]*(n-len(l1))
        l2+=[0]*(n-len(l2))

        for i in range(n):
            if int(l1[i])>int(l2[i]):
                return 1
            elif int(l1[i])<int(l2[i]):
                return -1

        return 0
        
        