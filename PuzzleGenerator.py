import chess
import random
from Minimax import Minimax


class PuzzleGenerator:
    """
    Puzzle generator class, uses minimax algorithm to find best moves.
    """
    minimax = Minimax()

    """
    A 2D list of openings that the algorithm will randomly choose.
    """
    openings = [
        ["e2e4", "c7c5"],  # Sicilian defense
        ["e2e4", "c7c6"],  # Caro-Kann defence
        ["e2e4", "d7d5", "e4d5", "d8d5"],  # Scandinavian defence
        ["e2e4", "d7d6", "d2d4", "g8f6"],  # Pirc defence
        ["e2e4", "e7e5", "f2f4"],  # Kings gambit
        ["e2e4", "e7e5", "g1f3", "b8c6", "d2d4"],  # Scotch Game
        ["d2d4", "d7d5", "c2c4", "c7c6"],  # Slav defence
        ["d2d4", "g8f6", "c2c4", "g7g6"],  # Kings Indian defence
        ["d2d4", "g8f6", "c2c4", "b2c3", "f8b4"],  # Nimzo defence
        ["d2d4", "g8f6", "c2c4", "g1f3", "b7b6"],  # Queens indian defence
        ["d2d4", "g8f6", "c2c4", "e7e6", "g2g3"],  # Catalan opening
        ["d2d4", "g8f6", "c2c4", "e7e6", "g1f3", "f8b4"],  # Bogo-Indian defence
        ["d2d4", "g8f6", "c2c4", "g7g6", "b1c3", "d7d5"],  # Grunfeld Defence
        ["d2d4", "g8f6", "c2c4", "c7c6", "d4d5", "b7b5"],  # Benko Gambit
        ["d2d4", "d7d5", "g1f3", "g8f6", "c1f4"],  # London system
        ["d2d4", "g8f6", "c2c4", "c7c5", "d4d5", "e7e6", "b1c3", "e6d5", "c4d5", "d7d6"],  # Benoni Defence
        ["d2d4", "d7d5"],  # Queen's gambit
        ["e2e4", "e7e5", "g1f3", "b8c6", "f1c4"],  # Italian game
        ["e2e4", "e7e6"],  # French defence
        ["e2e4", "e7e5", "g1f3", "b2c6", "f1b5"]  # Ruy Lopez
    ]

    def generate_puzzle(self, difficulty):
        """
        Generates the puzzles using random elements along with the minmax algorithm
        :param difficulty: the difficulty of the puzzle
        :return: board, the current puzzle state. puzzle_moves, the moves needed to play to get to end game.
        """
        board = chess.Board()  # Creates a new board
        opening = random.choice(self.openings)  # Chooses a random opening from the list

        for move in opening:  # Loops over the moves in the opening
            move = chess.Move.from_uci(move)  # Makes sure the move is valid
            board.push(move)  # Pushes the moves to the board

        for i in range(10):
            move = self.minimax.find_best_move(board, 4)  # Minimax plays moves to get to mid-game
            board.push(move)

        for i in range(10):
            legalMoves = list(board.legal_moves)
            move = random.choice(legalMoves)  # Plays random moves to get a random state of game
            board.push(move)

        while not board.is_game_over():  # Makes sure moves keep playing until the game is in a game over state.
            legalMoves = list(board.legal_moves)
            move = random.choice(legalMoves)  # One side plays random moves
            board.push(move)

            move = self.minimax.find_best_move(board, 3)  # Other side plays minimax moves
            board.push(move)

        puzzle_moves = []
        for i in range(difficulty * 2):
            popped_move = board.pop()  # Pops the moves of the board to generate puzzle
            puzzle_moves.append(popped_move)  # Adds these popped moves to puzzle_moves

        puzzle_moves = puzzle_moves[::-1]  # Reverses puzzle_moves so it is in the correct order
        return board, puzzle_moves

    def _search_checkmate(self, board, depth, moves=[]):
        if depth == 0:
            return None

        bestMove = self.minimax.find_best_move(board, 2)
        board.push(bestMove)
        if board.is_game_over():
            board.pop()
            return True
        else:
            self._search_checkmate(board, depth - 1)
        board.pop()
