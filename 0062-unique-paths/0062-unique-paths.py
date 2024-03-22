class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Total number of movements required
        p = m + n - 2
        # Number of movements to be downwards or to the right
        q = min(m - 1, n - 1)
        # Initialize the result
        res = 1
        # Calculate C(p, q) using combinations formula
        for i in range(q):
            res *= (p - i)
            res //= (i + 1)
        return res