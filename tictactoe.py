BLANK_SQUARE = '_'
MIN_BOARD_SIZE = 3
MAX_BOARD_SIZE = 20


class TicTacToe:

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [BLANK_SQUARE] * self.total_squares
        self.current_player = 'X'

    @property
    def total_squares(self):
        return self.board_size ** 2

    def print_board(self):
        print()
        for i in range(0, self.total_squares):
            print(self.board[i], end='  ')
            if i % self.board_size == self.board_size - 1:
                print()
                print()

    def make_move(self, position):
        if self.board[position] == BLANK_SQUARE:
            self.board[position] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
        else:
            print('Invalid move!')

    def check_winner(self):
        def is_winner(sequence):
            return len(set(sequence)) == 1 and sequence[0] != BLANK_SQUARE

        # Check rows and columns
        for i in range(self.board_size):
            row = self.board[i * self.board_size:(i + 1) * self.board_size]
            col = self.board[i::self.board_size]
            
            if is_winner(row):
                return row[0]
            if is_winner(col):
                return col[0]

        # Check diagonal 1 (top-left to bottom-right)
        if is_winner([self.board[i * self.board_size + i] for i in range(self.board_size)]):
            return self.board[0]

        # Check diagonal 2 (top-right to bottom-left)
        if is_winner([self.board[i * self.board_size + (self.board_size - 1 - i)] for i in range(self.board_size)]):
            return self.board[self.board_size - 1]

        return None

    def check_draw(self):
        return BLANK_SQUARE not in self.board

    def reset(self):
        self.board = [BLANK_SQUARE] * (self.total_squares)
        self.current_player = 'X'


# Main program starts here
while True:
    try:
        board_size = int(input(f'What board size do you want? ({MIN_BOARD_SIZE}-{MAX_BOARD_SIZE}): '))
        if MIN_BOARD_SIZE <= board_size <= MAX_BOARD_SIZE: break
    except ValueError:
        pass
    print(f"Invalid input! Please enter a board size between {MIN_BOARD_SIZE} and {MAX_BOARD_SIZE}.")

game = TicTacToe(board_size=board_size)

# Game loop
while game.check_winner() is None and not game.check_draw():
    game.print_board()
    try:
        position = int(input(f'Enter position (0 - {game.total_squares - 1}): '))
        if 0 <= position < game.total_squares:
            game.make_move(position)
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid input! Please enter a position between 0 and {game.total_squares - 1}.")

game.print_board()
