from math import inf


class AI:

    def __init__(self, ai_symbol="O", human_symbol="X"):
        self.ai = ai_symbol
        self.human = human_symbol

    def minimax(self, board, maximizing):

        if board.check_winner(self.ai):
            return 1

        if board.check_winner(self.human):
            return -1

        if board.is_full():
            return 0

        if maximizing:

            best_score = -inf

            for move in board.available_moves():

                board.board[move] = self.ai

                score = self.minimax(board, False)

                board.board[move] = " "

                best_score = max(best_score, score)

            return best_score

        else:

            best_score = inf

            for move in board.available_moves():

                board.board[move] = self.human

                score = self.minimax(board, True)

                board.board[move] = " "

                best_score = min(best_score, score)

            return best_score

    def best_move(self, board):

        best_score = -inf
        move = None

        for possible_move in board.available_moves():

            board.board[possible_move] = self.ai

            score = self.minimax(board, False)

            board.board[possible_move] = " "

            if score > best_score:
                best_score = score
                move = possible_move

        return move