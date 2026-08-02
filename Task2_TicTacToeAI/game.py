from board import Board
from ai import AI


class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.human = "X"
        self.computer = "O"

    def play(self):

        while True:

            self.board.display()

            # Human Turn
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                except ValueError:
                    print("❌ Please enter a valid number.")
                    continue

                if move not in range(9):
                    print("❌ Position must be between 1 and 9.")
                    continue

                if self.board.make_move(move, self.human):
                    break

                print("❌ Cell already occupied.")

            if self.board.check_winner(self.human):
                self.board.display()
                print("\n🎉 Congratulations! You Win!")
                break

            if self.board.is_full():
                self.board.display()
                print("\n🤝 Match Draw!")
                break

            # AI Turn
            print("\n🤖 AI is thinking...\n")

            ai_move = self.ai.best_move(self.board)

            self.board.make_move(ai_move, self.computer)

            if self.board.check_winner(self.computer):
                self.board.display()
                print("\n🤖 AI Wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("\n🤝 Match Draw!")
                break