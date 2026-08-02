class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def display(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print()

    def reset(self):
        self.board = [" " for _ in range(9)]

    def is_empty(self, position):
        return self.board[position] == " "

    def make_move(self, position, symbol):
        if self.is_empty(position):
            self.board[position] = symbol
            return True
        return False

    def available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == " "]

    def is_full(self):
        return " " not in self.board

    def check_winner(self, symbol):
        winning_positions = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        for combo in winning_positions:
            if all(self.board[pos] == symbol for pos in combo):
                return True

        return False