import unittest

import chess
from Driver import Driver
class DriverTests(unittest.TestCase):
    driver = Driver()

    """Test to see if the get turn function returns the correct value given a chess board"""
    def test_get_turn(self):
        board = chess.Board()
        self.assertEqual(self.driver._get_turn(board), "White")

        null_move = chess.Move.null()
        board.push(null_move)

        self.assertEqual(self.driver._get_turn(board), "Black")


    """Test to see if the test valid move function works when given a default board, and e2e4 is added"""
    def test_valid_move(self):
        board = chess.Board()

        self.assertEqual(self.driver._get_valid_move(board), chess.Move.from_uci('e2e4'))



if __name__ == '__main__':
    unittest.main()
