import pytest
from hamcrest import assert_that, equal_to, has_entries

from app.prefix_dict import PrefixDict


def test_prefix_dict_correct_prefixes():
    dictionary = PrefixDict.make_dict(["car", "loft"])

    assert_that(len(dictionary.words), equal_to(8))
    assert_that(dictionary.words, has_entries(
        c=equal_to(False),
        ca=equal_to(False),
        car=equal_to(True),
        l=equal_to(False),
        lo=equal_to(False),
        lof=equal_to(False),
        loft=equal_to(True),
    ))


def test_prefix_dict_raises_error_on_empty_words_list():
    with pytest.raises(ValueError) as excinfo:
        PrefixDict.make_dict([])

    assert_that("empty words list", equal_to(str(excinfo.value)))
