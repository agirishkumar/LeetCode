class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        ans = 0
        st = []

        for r in range(n):
            while st and height[st[-1]] < height[r]:
                m = st.pop()

                if not st:
                    break

                l = st[-1]
                h = min(height[r] - height[m], height[l] - height[m])
                w = r - l - 1
                
                ans += h * w
            st.append(r)
        return ans
