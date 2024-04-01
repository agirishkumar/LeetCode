class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}

        for word in strs:
            count=[0]*26
            for letter in word:
                count[ord(letter)-ord("a")]+=1
            count=tuple(count)
            if count not in dic:
                dic[count]=[word]
            else:
                dic[count].append(word)
        return dic.values()
        