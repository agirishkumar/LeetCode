class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        a = []
        for i in rectangles:
            a.append(min(i))
        c=Counter(a)
        larg=max(c.keys())
        return c[larg]
            
        