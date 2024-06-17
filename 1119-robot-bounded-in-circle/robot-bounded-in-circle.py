class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initial position and direction
        x, y = 0, 0
        direction_index = 0  # Start facing North
        
        # Execute instructions
        for instruction in instructions:
            if instruction == 'G':
                dx, dy = directions[direction_index]
                x += dx
                y += dy
            elif instruction == 'L':
                direction_index = (direction_index - 1) % 4
            elif instruction == 'R':
                direction_index = (direction_index + 1) % 4
        
        # Check if robot returns to the original position or faces a different direction
        return (x == 0 and y == 0) or direction_index != 0


        