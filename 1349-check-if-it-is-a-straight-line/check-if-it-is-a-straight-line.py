class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True  
    
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        
        dx = x1 - x0
        dy = y1 - y0
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            
            if (y - y0) * dx != (x - x0) * dy:
                return False
        
        return True
        