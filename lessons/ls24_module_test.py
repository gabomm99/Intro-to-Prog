"""An example of a test module in python"""

from lessons.ls24_module import fill_range, total
from lessons.ls24_module import join
from lessons.ls24_module import fill_range
from typing import List


def test_total_empty() -> None: 
    """Total of empty list should be zero"""
    assert total([]) == 0.0


def test_total_single_item() -> None:
    """Total of a single value should be the first item in the list"""
    assert total([110]) == 110.0


def test_total_with_many_items() -> None:
    """Total list of many items"""
    assert total([1,2,3]) == 6


def test_join_use_case() -> None:
    assert join([1, 2, 3], ", ") == "1, 2, 3"


def test_join_edge_case_single_item() -> None:
    assert join([1], ", ") == "1"


def test_join_edge_empty_delimiter() -> None:
    assert join([1, 2, 3], "") == "123"



def test_fill_range_use1() -> None:
    low_num: int = 1
    high_num: int = 3
    final_result: List[int] = [1, 2, 3]
    assert fill_range(low_num, high_num) == final_result


def test_fill_range_use2() -> None:
    low_num: int = 50
    high_num: int = 51
    final_result: List[int] = [50, 51]
    assert fill_range(low_num, high_num) == final_result


def test_fill_range_edge_novalue() -> None:
    low_num: int = 0
    high_num: int = 0
    final_result: List[int] = [0, 0]
    assert fill_range(low_num, high_num) == final_result


def test_fill_range_edge_negative() -> None:
    low_num: int = 7
    high_num: int = 3
    final_result: List[int] = []
    assert fill_range(low_num, high_num) == final_result  