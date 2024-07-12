import chess
import chess.svg
import chess.engine


class Evaluator:
    """
    A class to evaluate the current state of the chess board
    """

    """
    These variables are used to store the piece square tables
    """
    pawnEvalWhite = [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        [0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1],
        [0.05, 0.05, 0.1, 0.25, 0.25, 0.1, 0.05, 0.05],
        [0.0, 0.0, 0.0, 0.2, 0.2, 0.0, 0.0, 0.0],
        [0.05, -0.05, -0.1, 0.0, 0.0, -0.1, -0.05, 0.05],
        [0.05, 0.1, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ]

    pawnEvalBlack = pawnEvalWhite[::-1]

    knightEval = [
        [-0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5],
        [-0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4],
        [-0.3, 0.0, 0.1, 0.15, 0.15, 0.1, 0.0, -0.3],
        [-0.3, 0.05, 0.15, 0.2, 0.2, 0.15, 0.05, -0.3],
        [-0.3, 0.0, 0.15, 0.2, 0.2, 0.15, 0.0, -0.3],
        [-0.3, 0.05, 0.1, 0.15, 0.15, 0.1, 0.05, -0.3],
        [-0.4, -0.2, 0.0, 0.05, 0.05, 0.0, -0.2, -0.4],
        [-0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5]
    ]

    bishopEvalWhite = [
        [-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2],
        [-0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1],
        [-0.1, 0.0, 0.05, 0.1, 0.1, 0.05, 0.0, -0.1],
        [-0.1, 0.05, 0.05, 0.1, 0.1, 0.05, 0.05, -0.1],
        [-0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.0, -0.1],
        [-0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1],
        [-0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.05, -0.1],
        [-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, 0.2]
    ]

    bishopEvalBlack = bishopEvalWhite[::-1]

    rookEvalWhite = [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05],
        [-0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05],
        [-0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05],
        [-0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05],
        [-0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05],
        [-0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05],
        [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
    ]

    rookEvalBlack = rookEvalWhite[::-1]

    evalQueen = [
        [-0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2],
        [-0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1],
        [-0.1, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1],
        [-0.05, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05],
        [0.0, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05],
        [-0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1],
        [-0.1, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, -0.1],
        [-0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2]
    ]

    kingEvalWhite = [
        [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
        [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
        [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
        [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
        [-0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2],
        [-0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1],
        [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2],
        [0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2]
    ]

    kingEvalBlack = kingEvalWhite[::-1]

    eval_tables = {
        chess.WHITE: {
            chess.PAWN: pawnEvalWhite,
            chess.BISHOP: bishopEvalWhite,
            chess.ROOK: rookEvalWhite,
            chess.KNIGHT: knightEval,
            chess.QUEEN: evalQueen,
            chess.KING: kingEvalWhite
        },
        chess.BLACK: {
            chess.PAWN: pawnEvalBlack,
            chess.BISHOP: bishopEvalBlack,
            chess.ROOK: rookEvalBlack,
            chess.KNIGHT: knightEval,
            chess.QUEEN: evalQueen,
            chess.KING: kingEvalBlack
        }
    }

    def _find_row_and_col(self, position):
        """
        Finds the row and col of the position.
        :param position: the position to find
        :return: row, col
        """
        row = 7 - position // 8
        col = position % 8

        return row, col

    def evaluate_board(self, board):
        """
        Evaluates the board using piece square tables, material balance and checkmate.
        :param board: current board state
        :return: evaluation
        """
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 90
        }

        evaluation = 0  # Initialises the evaluation variable
        for square in chess.SQUARES:  # Loops over the board
            piece = board.piece_at(square)  # Gets piece at the square
            if piece is not None:
                value = piece_values[piece.piece_type]  # gets the correct piece value from the piece_value dictionary
                if piece.color == chess.WHITE:  # Checks piece color
                    evaluation += value  # Adds the correct value to the evaluation variable
                    evaluation += self._evaluate_piece_square(piece, square)  # Adds the correct value to the evaluation variable
                else:
                    evaluation -= value  # Adds the correct value to the evaluation variable
                    evaluation -= self._evaluate_piece_square(piece, square)  # Adds the correct value to the evaluation variable

            evaluation = round(evaluation, 3)

        if board.is_checkmate() and board.turn == chess.BLACK:  # Checks if white has won
            evaluation += 90
        elif board.is_checkmate() and board.turn == chess.WHITE:  # Checks if black has won
            evaluation -= 90

        return evaluation

    def _evaluate_piece_square(self, piece, position):
        currentPosition = self._find_row_and_col(position)  # Uses _find_row_and_col function to get the row and column
        row = currentPosition[0]
        col = currentPosition[1]

        eval_table = self.eval_tables[piece.color][piece.piece_type]   # Gets the correct eval table from the dictionary

        return eval_table[row][col]  # Returns the correct value to be added to the evaluation variable.


class Minimax:
    """
    A class that implements the minimax algorithm
    """

    evaluator = Evaluator()  # Used for evaluating the board at a given state.

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        """
        The main function of the minimax algorithm is to search through the game tree and return the correct evaluation
        :param board: the current board state
        :param depth: the depth of the search
        :param alpha: the current alpha value for the alpha-beta pruning
        :param beta: the current beta value for the alpha-beta pruning
        :param maximizing_player: true or false to describe the current maximizing player
        :return: min_eval or max_eval based on the maximizing player
        """

        if depth == 0 or board.is_game_over():  # Base case, checks if depth is zero or the game is over
            return self.evaluator.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')  # Assign this to -inf for alpha beta pruning
            for move in board.legal_moves:  # Loops over the legal moves
                board.push(move)  # Pushes the move
                eval = self.minimax(board, depth - 1, alpha, beta, False)  # Recursive call, with maximizing player now being false
                board.pop()  # Pops the move to return the board to the original state
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:  # Where alpha-beta pruning takes place, if beta <= alpha, prune this branch
                    break
            return max_eval
        else:
            min_eval = float('inf')  # Assign this to +inf for alpha beta pruning
            for move in board.legal_moves:  # Loops over the legal moves
                board.push(move)   # Pushes the move
                eval = self.minimax(board, depth - 1, alpha, beta, True) # Recursive call, with maximizing player now being true
                board.pop()  # Pops the move to return the board to the original state
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:  # Where alpha-beta pruning takes place, if beta <= alpha, prune this branch
                    break

            return min_eval

    def find_best_move(self, board, depth):
        """
        Finds the best move for the current state and given depth
        :param board: Current state of board
        :param depth: current search depth
        :return: best_move found by search
        """

        best_move = None  # Set default value for best_move
        alpha = float('-inf')  # Assign alpha to -inf for alpha beta pruning
        beta = float('inf')  # Assign beta to +inf for alpha beta prunint

        maximizing_player = board.turn  # Gets the board turn, used so the minimax algorithm is called correctly

        if maximizing_player:
            max_eval = float('-inf') # Assign this to -inf for alpha beta pruning
            for move in board.legal_moves:  # Loops over the legal moves
                board.push(move)  # Pushes the move
                eval = self.minimax(board, depth - 1, alpha, beta, False)  # Initial minimax call
                board.pop()  # Pops the move to return the board to the original state
                if eval > max_eval: # Checks if the eval is bigger than the max_eval, if true, this new move is better than the previous one.
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
        else:
            min_eval = float('inf')  # Assign this to +inf for alpha beta pruning
            for move in board.legal_moves:  # Loops over the legal moves
                board.push(move)  # Pushes the move
                eval = self.minimax(board, depth - 1, alpha, beta, True) # Initial minimax call
                board.pop()  # Pops the move to return the board to the original state
                if eval < min_eval:  # Checks if the eval is smaller than the min_eval, if true, this new move is better than the previous one.
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)

        return best_move
