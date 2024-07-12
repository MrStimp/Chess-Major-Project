import unittest

import chess
from PuzzleGenerator import PuzzleGenerator


class TestPuzzleGenerator(unittest.TestCase):
    puzzle_generator = PuzzleGenerator()

    """
    Tests that a difficulty 1 test has the correct number of moves.
    """
    def test_puzzle_generator_difficulty1(self):
        puzzle, puzzleMoves = self.puzzle_generator.generate_puzzle(1)
        self.assertEqual(len(puzzleMoves), 2)

    """
    Tests that a difficulty 2 test has the correct number of moves.
    """
    def test_puzzle_generator_difficulty2(self):
        puzzle, puzzleMoves = self.puzzle_generator.generate_puzzle(2)
        self.assertEqual(len(puzzleMoves), 4)

    """
    Tests that a difficulty 3 test has the correct number of moves.
    """
    def test_puzzle_generator_difficulty3(self):
        puzzle, puzzleMoves = self.puzzle_generator.generate_puzzle(3)
        self.assertEqual(len(puzzleMoves), 6)


if __name__ == '__main__':
    unittest.main()