from app.game import Game

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='''Words searcher game''')
    parser.add_argument('--board-size', type=int, default=15, help='game board size')
    parser.add_argument('--words-path', type=str, default='./src/resources/words.txt',
                        help='path to file with words to find')

    args = parser.parse_args()
    board_size = args.board_size
    words_path = args.words_path

    game = Game(board_size, words_path)
    board, words = game.start()

    print("The current board is :\n{}".format(board))
    print("Founded words: {}".format(words))


if __name__ == '__main__':
    main()
