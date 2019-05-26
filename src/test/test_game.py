import pytest
from hamcrest import equal_to, assert_that, contains_string, has_items

from app.game import Game
from app.prefix_dict import PrefixDict
from unittest.mock import MagicMock

from app.utils import load_words


@pytest.mark.parametrize("bord_size", [
    -1,
    0,
    1
])
def test_game_raise_error_when_board_size_less_than_2(bord_size):
    with pytest.raises(ValueError) as excinfo:
        Game(board_size=bord_size, words_path="")

    assert_that("board size should be greater than 1", equal_to(str(excinfo.value)))


def test_game_raise_error_when_words_path_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        game = Game(board_size=12, words_path="")
        game.start()

    assert_that(str(excinfo.value), contains_string("No such file or directory:"))


def test_game_search():
    game = Game(board_size=3, words_path="./test")
    game.prepare_game = MagicMock(return_value=(fake_board(),
                                                PrefixDict.make_dict(load_words("./src/test/resources/test_words.txt"))))
    board, words = game.start()

    expected_words = {'ay', 'bar', 'bay'}

    assert_that(len(board), equal_to(3))
    assert_that(board, equal_to(fake_board()))
    assert_that(len(expected_words), equal_to(3))
    assert_that(expected_words, has_items(*words))


def fake_board():
    return [['b', 'c', 'a'],
            ['a', 'a', 'r'],
            ['y', 'z', 'r']]
