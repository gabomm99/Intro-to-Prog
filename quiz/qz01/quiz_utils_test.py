"""Test for responses for Quiz 01."""


__author__ = "730442926"


from typing import List
from quiz.qz01.quiz_utils import strs_to_floats, lookup, undelimit, avg_column
import pytest

def test_strs_to_float_case1() -> None:
    """Checks if a str list with three 'float like' values returns a float list with thos values."""
    assert strs_to_floats(["1.7", "2.76", "3.9"]) == [1.7, 2.76, 3.9]


def test_strs_to_float_case2() -> None:
    """Checks if a str list with four 'float like' values returns a float list with thos values."""
    assert strs_to_floats(["1.7", "2.0", "7.1", "11.1"]) == [1.7, 2.0, 7.1, 11.1]


def test_lookup_case1() -> None:
    """Checks if a str list with three values and a float list with three values!
    
    returns a float that represents the same index from the second list and  first list.
    """
    assert lookup(["hola", "como", "estas"], [1.0, 2.3, 5.7], "como") == 2.3


def test_lookup_case2() -> None:
    """Checks if a str list with six values and a float list with six values!
    
    returns a float that represents the same index from the second list and  first list.
    """
    assert lookup(["hola", "como", "estas", "grande", "vamos", "dale"], [1.0, 2.3, 5.7, 2.2, 6.3, 7.1], "vamos") == 6.3


def test_lookup_case3() -> None:
    """Checks if a str list with three values and a float list with four values!
    
    returns an error since lists are different length.
    """
    with pytest.raises(ValueError):
        lookup(["hi", "how", "are"], [1.0, 2.2, 3.3, 4.5], "how")


def test_lookup_case4() -> None:
    """Checks what happens when wourd is not in str List."""
    with pytest.raises(ValueError):
        lookup(["hi", "how", "are"], [1.0, 2.2, 3.3], "you")

def test_lookup_edge1() -> None:
    """What happens if one of the floats is 0.0!"""
    assert lookup(["hi", "how", "are"], [1.0, 0.0, 2.1], "how") == 0.0


def test_undelimit_case1() -> None:
    """Test if a str with ten characters and one comma, returns a list with two words."""
    assert undelimit("habla,juan") == ["habla", "juan"]


def test_undelimit_case2() -> None:
    """Test if a str with twenty-one characters and three commas, returns a list with four words."""
    assert undelimit("hello,gabriel,lets,go") == ["hello", "gabriel", "lets", "go"]

def test_undelimit_edge_case1() -> None:
    """Test if a str with three spaces and two commas returns a list with three spaces."""
    assert undelimit(" , , ") == [" ", " ", " "]


def test_avg_column_case1() -> None:
    """Check if a chart with three columns gives avg of asked column."""
    stats: List[str] = [
        "high,low,precipitation",
        "81.0,53.0,0.1",
        "70.0,52.0,0.1",
        "77.0,54.0,0.1",
        "66.0,44.0,0.1"
        ]
    assert avg_column(stats, "low") == 50.75

def test_avg_column_case2() -> None:
    stats: List[str] = [
        "high,low,precipitation",
        "81.0,53.0,0.1",
        "70.0,52.0,0.1",
        "77.0,54.0,0.1",
        "66.0,44.0,0.1"
        ]
    with pytest.raises(ValueError):
        avg_column(stats, "weather")


def test_avg_column_case3() -> None:
    """Check if a chart with three columns gives avg of asked column."""
    stats: List[str] = [
        "high,low,precipitation",
        "81.0,53.0,0.1",
        "70.0,52.0,0.1",
        "77.0,54.0,0.1",
        "66.0,44.0,0.1"
        ]
    assert avg_column(stats, "high") == 73.5
