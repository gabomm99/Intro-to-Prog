"""An example Python module."""

from typing import List

def total(xs: List[float]) -> float:
    """Total returns the sum of xs."""
    result: float = 0.0
    for x in xs:
        result += x
    return result



def join(xs: List[int], delimeter: str) -> str:
    """Produce a list with delimeters between items."""
    result: str = ""
    
    for x in xs:
        if result == "": 
            result = str(x)
        else:
            result += delimeter + str(x) 

    return result


def fill_range(low: int, high: int) -> List[int]:
    """A function that takes to integers and"""
    return_list: List[int] = []
    if low == high: 
        return_list = [low, high]
        return return_list
    for value in range(low, high + 1):
        return_list.append(value)
    
    return return_list



