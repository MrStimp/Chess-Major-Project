import unittest

import chess

from Minimax import Evaluator, Minimax


class TestPieceEvaluation(unittest.TestCase):
    board = chess.Board()
    evaluator = Evaluator()

    def test_rook_in_corner(self):
        """
        Tests that the white Rook piece is evaluated to 0.0 if on square 7
        """
        piece = self.board.piece_at(7)
        self.assertEqual(self.evaluator._evaluate_piece_square(piece, 7), 0.0)

    def test_knight_on_square57(self):
        """
        Tests that the Knight piece is evaluated to -0.4 if on square 57
        """
        piece = self.board.piece_at(57)
        self.assertEqual(self.evaluator._evaluate_piece_square(piece, 57), -0.4)

    def test_knight_on_square21(self):
        """
        Tests that the Knight piece is evaluated to 0.1 if on square 21
        """
        self.board = chess.Board('3r4/8/8/8/8/5N2/8/8 w - - 1 1')
        piece = self.board.piece_at(21)

        self.assertEqual(self.evaluator._evaluate_piece_square(piece, 21), 0.1)

    def test_rook_on_square59(self):
        """
        Tests that the black Rook piece is evaluated to 0.5 if on square 59
        """
        self.board = chess.Board('3r4/8/8/8/8/5N2/8/8 w - - 1 1')
        piece = self.board.piece_at(59)
        self.assertEqual(self.evaluator._evaluate_piece_square(piece, 59), 0.5)

    def test_queen_on_square42(self):
        """
        Tests that the white queen piece is evaluated to 0.05 if on square 42
        """

        self.board = chess.Board('8/8/2Q5/8/8/8/8/8 w - - 0 1')
        piece = self.board.piece_at(42)
        self.assertEqual(self.evaluator._evaluate_piece_square(piece, 42), 0.05)

    def test_queen_on_square43(self):
        """
        Tests that the black queen piece is evaluated to 0.05 if on square 43
        """
        self.board = chess.Board('8/8/3q4/8/8/8/8/8 w - - 0 1')
        piece = self.board.piece_at(43)
        self.assertEqual(self.evaluator._evaluate_piece_square(piece, 43), 0.05)

    def test_bishop_on_square5(self):
        """
        Tests that the white bishop piece is evaluated to -0.1 if on square 5
        """
        self.board = chess.Board('8/8/8/8/8/8/8/5B2 w - - 0 1')
        piece = self.board.piece_at(5)
        self.assertEqual(self.evaluator._evaluate_piece_square(piece, 5), -0.1)

    def test_bishop_on_square18(self):
        """
        Tests that the black bishop piece is evaluated to 0.05 if on square 18
        """
        self.board = chess.Board('8/8/8/8/8/2b5/8/8 w - - 0 1')
        piece = self.board.piece_at(18)
        self.assertEqual(self.evaluator._evaluate_piece_square(piece, 18), 0.05)


    """
    Tests that a defualt board will be evaluated to 0 by the evaluation function"""
    def test_board_evaluation(self):
        self.board = chess.Board()
        self.assertEqual(self.evaluator.evaluate_board(self.board), 0)


    """
    Tests that the board will be evaluated to 1.05 if a black pawn is removed from square h7"""
    def test_board_evaluation2(self):
        self.board = chess.Board('rnbqkbnr/ppppppp1/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        self.assertEqual(self.evaluator.evaluate_board(self.board), 1.05)


    """Tests that the board will be evaluated to to 1.4 if a black pawn has been removed, a white pawn is moved to square e4, a white knight is moved to e5 and a black pawn is moved to square d5"""
    def test_board_evaluation3(self):
        self.board = chess.Board('rnbqkbnr/ppp2ppp/8/3pN3/4P3/8/PPPP1PPP/RNBQKB1R b KQkq - 0 3')
        self.assertEqual(self.evaluator.evaluate_board(self.board), 1.4)

class TestMinimax(unittest.TestCase):
    minmax = Minimax()
    evaluator = Evaluator()
    board = chess.Board()

    """ 
    Tests that tests the minimax algorithm with a test from chess.com
    """
    def test_random_puzzle(self):
        self.board = chess.Board('r1b2bkr/ppp3pp/2n5/3qp3/2B5/8/PPPP1PPP/RNB1K2R w - - 0 1')
        bestMove = chess.Move.from_uci("c4d5")
        minimaxBestMove = self.minmax.find_best_move(self.board, 3)
        self.assertEqual(minimaxBestMove, bestMove)

    """ 
    Tests that tests the minimax algorithm with a test from chess.com
    """
    def test_random_puzzle2(self):
        self.board = chess.Board('r3r3/pp3p1k/6pp/4b3/2BpP2q/PQ1P3P/1P3P2/2R3RK b - - 0 1')
        bestMove = chess.Move.from_uci("h4h3")
        minimaxBestMove = self.minmax.find_best_move(self.board, 3)
        self.assertEqual(minimaxBestMove, bestMove)

    """ 
    Tests that tests the minimax algorithm with a test from chess.com
    """
    def test_random_puzzle3(self):
        self.board = chess.Board('4r3/7R/6B1/8/5k2/1Pb2P2/2P3PP/1K6 b - - 0 1')
        bestMove = chess.Move.from_uci("e8e1")
        minimaxBestMove = self.minmax.find_best_move(self.board, 3)
        self.assertEqual(minimaxBestMove, bestMove)

        self.board.push(bestMove)

        bestMove = chess.Move.from_uci("b1a2")
        minimaxBestMove = self.minmax.find_best_move(self.board, 3)
        self.assertEqual(minimaxBestMove, bestMove)

        self.board.push(bestMove)

        bestMove = chess.Move.from_uci("e1a1")
        minimaxBestMove = self.minmax.find_best_move(self.board, 3)
        self.assertEqual(minimaxBestMove, bestMove)

    """ 
    Tests that tests the minimax algorithm with a test from chess.com, this test required more depth to find the correct answer
    """
    def test_random_puzzle4(self):
        self.board = chess.Board('7Q/7p/8/3K2q1/2P5/8/7k/8 w - - 0 1')
        bestMove = chess.Move.from_uci("h8e5")
        minimaxBestMove = self.minmax.find_best_move(self.board, 6)
        self.assertEqual(minimaxBestMove, bestMove)

    """ 
    Tests that tests the minimax algorithm with a test from chess.com
    """
    def test_random_puzzle5(self):
        self.board = chess.Board('5r2/4R2P/2p1R3/1pk5/p5B1/2PP2P1/PP4K1/5r2 b - - 0 1')
        bestMove = chess.Move.from_uci("f8f2")
        minimaxBestMove = self.minmax.find_best_move(self.board, 3)
        self.assertEqual(minimaxBestMove, bestMove)

        self.board.push(bestMove)

        bestMove = chess.Move.from_uci("g2h3")
        minimaxBestMove = self.minmax.find_best_move(self.board, 3)
        self.assertEqual(minimaxBestMove, bestMove)

        self.board.push(bestMove)

        bestMove = chess.Move.from_uci("f1h1")
        minimaxBestMove = self.minmax.find_best_move(self.board, 3)
        self.assertEqual(minimaxBestMove, bestMove)

if __name__ == '__main__':
    unittest.main()
