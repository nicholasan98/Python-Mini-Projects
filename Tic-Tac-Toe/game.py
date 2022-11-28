from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to represent 3x3 board
        self.current_winner = None # keeps track of winner

    def print_board(self):
        # this is getting the rows
        # i*3 is the first 3 rows, (i+1)*3 is for the next iteration of i and their 3 rows
        # range of 3 means there's 3 rows, so first row has 3, 2nd row has 3 and last row has 3
        # i goes from 0, 1 and 2, so the first iteration is going from 0:3 so it's 0 | 1 | 2
        # next one would be 1, so it's 3:6 so it's 3 | 4 | 5 etc.
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

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere, but we have to check rows, columns and diagonals
        # // means how many times 3 goes into square rounded down
        
        # check rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if these all fail
        return False


def play(game, x_player, o_player, print_game = True):
    # returns the winner of the game, or None means it's a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches the players
            # simplified ^^
            # if letter == 'X':
            #    letter = 'O'
            # else:
            #    letter = 'X'
        
        # tiny break to make a delay with the computer move
        time.sleep(0.8)
        
    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)