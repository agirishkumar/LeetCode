class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' ']* 3 for _ in range(3)]

        for i,move in enumerate(moves):
            r,c = move
            if i%2 == 0:
                grid[r][c] = 'X'
            else:
                grid[r][c] = 'O'

        def check_winner(player):

            for i in range(3):
                if grid[i] == [player]*3 or [grid[j][i] for j in range(3)] == [player]*3:
                    return True

            if grid[0][0] == grid[1][1] == grid[2][2] == player or grid[0][2] == grid[1][1] == grid[2][0] == player:
                return True
            return False
        

        if check_winner('X'):
            return "A"
        elif check_winner('O'):
            return "B"
        elif len(moves) < 9:
            return "Pending"
        else:
            return "Draw"



        
        


        



        