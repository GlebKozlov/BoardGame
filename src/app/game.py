from app.direction import Direction
from app.prefix_dict import PrefixDict
from app.utils import timer, generate_board, load_words, generate_used_pattern


class Game:
    def __init__(self, board_size, words_path):
        if board_size < 2:
            raise ValueError("board size should be greater than 1")
        self.board_size = int(board_size)
        self.words_path = words_path
        self.founded_words = set()

    @timer
    def start(self):
        """
        Starts preconfigured in constructor game
        :return: created board and all founded words
        """
        board, word_dict = self.prepare_game()
        self.solve(board, word_dict)
        return board, self.founded_words

    @timer
    def prepare_game(self):
        """
        Creates board over requested size.
        Loads words and creates PrefixDict
        :return: board, prefix_dict
        """
        board = generate_board(self.board_size)
        words = load_words(self.words_path)
        dictionary = PrefixDict.make_dict(words)
        return board, dictionary

    @timer
    def solve(self, board, word_dict):
        """
        Uses for searching all possible words across the board
        :param board
        :param word_dict
        :return: set of the founded on board words
        """
        used = generate_used_pattern(self.board_size)

        [self.search(board, row, column, word_dict, used, "")
         for row in range(self.board_size)
         for column in range(self.board_size)]

    def search(self, board, row, column, word_dict, used, word, previous_move_direction=None, move_direction=None):
        """
        Iterates recursively over the board, over the each letter and tries to find match with provided words.
        Finds only words that consists of the letters are located in one direction. Line wrapping excluded.
        :param board: simple 2d array filled of lower case letters
        :param row: one board row
        :param column: one board column
        :param word_dict: words and prefixes dict
        :param used: 2d array with size as a board and uses for track already appended letters in each iteration
        :param word: current state of the word
        :param previous_move_direction: last used direction, required for handling direction wraps
        :param move_direction: current move direction
        """
        # check for direction 'wrapping'
        if len(word) >= 2 and move_direction is not None:
            if previous_move_direction != move_direction:
                return

        # check for board limits
        if column < 0 or column >= self.board_size or row < 0 or row >= self.board_size:
            return

        # check for already used letter
        if used[row][column]:
            return

        # append letter to previous
        letter = board[row][column]
        word += letter

        child = word_dict.get_child(word)
        if child is not None:
            # check if this word is full or piece
            if child.is_full_word:
                self.founded_words.add(word)

            used[row][column] = True

            # continue to search in one direction
            if move_direction is not None:
                row_move, column_move = Direction[move_direction].value
                if previous_move_direction is None:
                    previous_move_direction = move_direction
                self.search(board, row + row_move, column + column_move, child, used, word, previous_move_direction,
                            move_direction)

            # iterating and searching over all possible directions exclude current position
            for direction in Direction:
                row_move, column_move = direction.value
                move_direction = direction.name
                if row_move != 0 or column_move != 0:
                    self.search(board, row + row_move, column + column_move, child, used, word, previous_move_direction,
                                move_direction)

            used[row][column] = False
