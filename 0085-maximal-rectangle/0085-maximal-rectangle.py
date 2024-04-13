class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        rows,cols = len(matrix), len(matrix[0])
        heights = [0]*(cols + 1)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            
            max_area = max(max_area, self.maxHistogramArea(heights))
            
        return max_area

    
    def maxHistogramArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        index = 0
        
        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
                max_area = max(max_area, area)
        
        return max_area

        
