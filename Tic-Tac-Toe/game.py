class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to represent 3x3 board
        self.current_winner = None # keeps track of winner

    def print_board(self):
        # this is getting the rows
        # i*3 is the first 3 rows, (i+1)*3 is for the next iteration of i and their 3 rows
        # range of 3 means there's 3 rows, so first row has 3, 2nd row has 3 and last row has 3
        for row in [self.board[i*3:(i+1)*3] for i in range (3)]:
            print('| ' + ' | '.join(row) + ' |')

    # static method cause it refers to no board, so does not need to call self
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds with which spot)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        # ^^ is a way to condense the entire for loop into a single line
        # enumerate tracks each object and gives it an assigned value
        # see below the # ['x', 'x', 'o'] example
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves