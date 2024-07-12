import chess

from PuzzleGenerator import PuzzleGenerator


class Driver:
    """
    Driver class to handle game, it is what the user interacts with and is how the solution is displayed
    """

    """
    Initialises some default values needed for the game
    """
    puzzle_generator = PuzzleGenerator()
    difficulty = 0
    puzzle_moves = []

    def _get_turn(self, board):
        """
        Returns whose turn it is in string format
        :param board: current state of the board
        :return: "White" if it is whites turn, "Black" if is its blacks turn
        """
        if board.turn:
            return "White"
        else:
            return "Black"

    def start_menu(self):
        """
        Starts the game and displays the opening message
        """
        print("Welcome to the chess puzzle game!")  # Prints welcome message

        self.difficulty = int(input("Please select difficulty from these options"
                                    "\n 1. Easy Puzzle"
                                    "\n 2. Medium Puzzle"
                                    "\n 3. Hard Puzzle"
                                    "\n 4-10 Custom difficulty\n"))  # Gets difficulty input from user

        if self.difficulty > 10:  # Limits the user to a max difficultly
            self.difficulty = 10
        self._play_game()

    def _play_game(self):
        """
        The main code the user will interact with, displays the board and allows user to solve puzzle
        """
        new_puzzle, self.puzzle_moves = self.puzzle_generator.generate_puzzle(self.difficulty)  # Generates puzzle

        for i in range(0, len(self.puzzle_moves), 2):  # Loops over len of puzzle moves, but only needs to print out every 2 items
            print(new_puzzle)
            print(self._get_turn(new_puzzle) + " just played " + str(self.puzzle_moves[i]))  # Prints the move the opponent made
            new_puzzle.push(self.puzzle_moves[i])  # Pushes opponent move
            print(new_puzzle)  # Displays board after opponent move

            print(list(new_puzzle.legal_moves))  # Prints out a list of legal moves for the user to make, I did this because in current implementation it can be confusing using this notation
            move = self._get_valid_move(new_puzzle)
            new_puzzle.push(move)  # Pushes user move
            if new_puzzle.is_game_over(): # Checks if game is over, if true then break the loop so no more moves are pushed cause a crash
                break

        self._game_over_screen(new_puzzle)

    def _get_valid_move(self, board):
        """
        Checks that the users move is valid and then returns the value
        :param board: current state of the board
        :return: the move the user wishes to make
        """
        while True:  # Will loop continuously until the user inputs a legal move
            try:
                user_move = input("Enter your move from the list above > ")
                move = chess.Move.from_uci(user_move)
                if move in board.legal_moves:  # Checks if the move is in the legal moves
                    return move
                else:
                    print("Invalid move. Please try again. > ")
            except ValueError:  # Checks for a valueerror
                print("Invalid input format. Please enter a move in Standard Algebraic Notation. > ")

    def _game_over_screen(self, board):
        """
        Displays the final message after solving puzzle, also displays puzzle solution if requested.
        :param board: current state of board
        """
        if board.is_game_over():  # Checks if game is over.
            print("Puzzle solved!:)")
        else:
            print("Puzzle failed:(")

        playerChoice = input("View AI solution? "
                             "Y =  yes\n"
                             "Anything else = no\n")

        if playerChoice.lower() == "y":
            for i in range(self.difficulty * 2):  # Pops the moves made earlier to get board back to original puzzle state.
                board.pop()

            for i in range(len(self.puzzle_moves)):  # loops over puzzle moves
                print(self._get_turn(board) + " Turn " + str(self.puzzle_moves[i]))
                board.push(self.puzzle_moves[i])  # Pushes the puzzle move
                print(board)  # Displays the new state of board
                input("Press any key to continue...")  # Asks the user for an input to continue

        if self._continue_game():  # If true _play_game is called.
            self._play_game()

    def _continue_game(self):
        """
        Asks the user whether they want to continue the game or change the difficulty or quite
        :return: True if difficulty was changed or they wish to continue, False otherwise
        """
        choice = input("Do you wish to continue? or change difficulty? or quit?\n"
                       "Y to continue\n"
                       "C to change difficulty\n"
                       "Anything else to quit\n")

        if choice.lower() == "y":
            return True
        elif choice.lower() == "c":
            self.difficulty = int(input("Enter your difficulty: "))
            if self.difficulty > 10:
                self.difficulty = 10
            return True
        else:
            return False


def main():
    """
    Main function of the program.
    """
    driver = Driver()
    driver.start_menu()  # Calls start_menu() function to play game.


if __name__ == "__main__":
    main()
