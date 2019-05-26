import pytest
from hamcrest import assert_that, equal_to, instance_of, is_

from app.direction import Direction
from app.utils import generate_board, generate_used_pattern

DEFAULT_2D_ARRAY = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]


@pytest.mark.parametrize("direction, exp", [
    (Direction.UP, 2),
    (Direction.DOWN, 8),
    (Direction.LEFT, 4),
    (Direction.RIGHT, 6),
    (Direction.LEFT_UP, 1),
    (Direction.LEFT_DOWN, 7),
    (Direction.RIGHT_DOWN, 9),
    (Direction.RIGHT_UP, 3),
])
def test_direction_moves(direction, exp):
    for idx in [1]:
        r, c = direction.value
        value = DEFAULT_2D_ARRAY[idx + r][idx + c]
        assert_that(value, equal_to(exp))


def test_generated_board():
    board = generate_board(size=2)

    assert_that(len(board), equal_to(2))
    for row in range(len(board)):
        for col in range(len(board)):
            assert_that(board[row][col], instance_of(str))
            assert board[row][col].islower()


def test_used_pattern_should_be_false_by_default():
    pattern = generate_used_pattern(size=2)
    for row in range(len(pattern)):
        for col in range(len(pattern)):
            assert_that(pattern[row][col], is_(False))
