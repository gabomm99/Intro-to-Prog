"""Test for different utilitie functions like count, all, max, min, is_equal."""

__author__ = "730442926"


import pytest
from typing import List
from exercises.ex05.utils import count, all, max, is_equal, concat, sub, splice


def test_count_first() -> None:
    """Tests that count function yields 3 for a list with 3 ones."""
    assert count([1, 3, 4, 6, 1, 1], 1) == 3


def test_count_second() -> None:
    """Tests that count function yields 4 for a list with 4 twos."""
    assert count([1, 4, 5, 2, 7, 2, 5, 2, 2], 2) == 4


def test_edge_count_no_value() -> None:
    """What happens when the list is empty."""
    assert count([], 0) == 0


def test_edge_count() -> None:
    """Result when value given to count is not on list."""
    assert count([2, 3, 4, 5, 6, 7, 8], 1) == 0


def test_all_true() -> None:
    """Test if a list with only 1's returns True when all analyzes it."""
    assert all([1, 1, 1, 1, 1, 1], 1)


def test_all_False() -> None:
    """Checks if a list with one different value yields False."""
    assert not all([1, 2, 1, 1, 1, 1], 1)


def test_all_edge_case1() -> None:
    """What happens if list is empty."""
    assert not all([], 0)


def test_all_edge_case2() -> None:
    """How does the all function behaves with negative numbers."""
    assert all([-1, -1, -1, -1], -1)


def test_max_case1() -> None:
    """Tests wether 10 is given as max value when it actually is."""
    testing_value: int = 10
    assert max([1, 2, 4, 6, 8, 10]) == testing_value


def test_max_case2() -> None:
    """Checks if a list with no ascending order still recognizes the max value."""
    testing_value: int = 10
    assert max([1, 10, 3, 4, 1, 5, 4]) == testing_value


def test_max_edge_case1() -> None:
    """If the max value appears more than one, it still recoginizes it as one max value."""
    testing_value: int = 15
    assert max([1, 3, 3, 5, 7, 12, 15, 15]) == testing_value


def test_max_edge_case2() -> None:
    """What happens when the lists only has negative values."""
    testing_value: int = -1
    assert max([-3, -4, -2, -6, -1]) == testing_value 


def test_max_empty() -> None:
    """Calling max function and given an empty list raises a Velue Error."""
    with pytest.raises(ValueError):
        list_nothing: List[int] = []
        max(list_nothing)


def test_is_equal_case1() -> None:
    """Checks if two lists with equal values at every index yields True."""
    assert is_equal([1, 2, 3, 4], [1, 2, 3, 4])


def test_is_equal_case2() -> None:
    """Tests if two list with one different value at one index yields False."""
    assert not is_equal([1, 2, 4], [2, 2, 4]) 


def test_is_equal_edge_1() -> None:
    """What happens if three items are equal, but one list is one item longer."""
    assert not is_equal([1, 2, 4], [1, 2, 4, 3])


def test_is_equal_empty() -> None:
    """What happens if both lists are empty."""
    assert is_equal([], []) 


def test_concat_case1() -> None:
    """Check if concat concatanates all six values of two list with three values each."""
    expected_list: List[int] = [1, 2, 4, 2, 5, 6]
    assert concat([1, 2, 4], [2, 5, 6]) == expected_list


def test_concat_case2() -> None:
    """Test if concat concatanates a list with four values and three values."""
    expected_list: List[int] = [1, 2, 5, 6, 9, 10, 11]
    assert concat([1, 2, 5, 6], [9, 10, 11]) == expected_list


def test_concat_edge_case1() -> None:
    """What happens when both lists are empty."""
    expected_list: List[int] = []
    assert concat([], []) == expected_list


def test_concat_edge_case_2() -> None:
    """What happens if the first list is empty."""
    expected_list: List[int] = [1, 2, 4]
    assert concat([], [1, 2, 4]) == expected_list


def test_concat_edge_case3() -> None:
    """What happens if the second list is empty."""
    expected_list: List[int] = [1, 2, 3, 4]
    assert concat([1, 2, 3, 4], []) == expected_list


def test_sub_case1() -> None:
    """Test if a list with 6 values and range 1 to 6 returns a list withh the first 5 values."""
    expected_list: List[int] = [1, 2, 3, 4, 5]
    assert sub([1, 2, 3, 4, 5, 6], 0, 5) == expected_list


def test_sub_case2() -> None:
    """Test if a list with 3 values and range 1 to 3 returns a list with the first 2 values."""
    expected_list: List[int] = [1, 2]
    assert sub([1, 2, 3], 0, 2) == expected_list


def test_sub_edge_case1() -> None:
    """Test if a empty list returns an empty list."""
    expected_list: List[int] = []
    assert sub([], 1, 6) == expected_list


def test_sub_edge_case2() -> None:
    """Test if a list with start value bigger than length of list returns an empty list."""
    expected_list: List[int] = []
    assert sub([1, 2, 3, 4, 5, 6], 7, 9) == expected_list


def test_sub_edge_case3() -> None:
    """Test if a list with end value less than or equal to zero returns an empty list."""
    expected_list: List[int] = []
    assert sub([1, 2, 3, 4, 5, 6], -3, -1) == expected_list


def test_sub_edge_case4() -> None:
    """Test if a list with negative start value and end value greater than!

    lenght of list returns a list that starts from first index value and ends on last value.
    """
    expected_list: List[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub([1, 2, 3, 4, 5, 6, 7], -1, 8) == expected_list


def test_splice_case1() -> None:
    """Test if a list with 4 numbers and another with 3 numbers!

    inserts the second 3 numbers at a given index of 2.
    """
    expected_list: List[int] = [1, 2, 1, 2, 3, 3, 4]
    assert splice([1, 2, 3, 4], 2, [1, 2, 3]) == expected_list


def test_splice_case2() -> None:
    """Test if a list with 10 numbers and another with 12 numbers!

    inserts the second 3 numbers at a given index of 8.
    """
    expected_list: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 9, 10]
    assert splice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == expected_list


def test_splice_edge_case1() -> None:
    """Test if a list with 4 numbers and another with 3 numbers!

    inserts the second 3 numbers at index 0 when given negative index.
    """
    expected_list: List[int] = [1, 2, 3, 1, 2, 3, 4]
    assert splice([1, 2, 3, 4], -2, [1, 2, 3]) == expected_list


def test_splice_edge_case2() -> None:
    """What happens when the first list is empty."""
    expected_list: List[int] = [1, 2, 3]
    assert splice([], 2, [1, 2, 3]) == expected_list


def test_splice_edge_case3() -> None:
    """What happens if the second list is empty."""
    expected_list: List[int] = [1, 2, 3, 4]
    assert splice([1, 2, 3, 4], 2, []) == expected_list


def test_splice_edge_case4() -> None:
    """What happens if both lists are empty."""
    expected_list: List[int] = []
    assert splice([], 2, []) == expected_list