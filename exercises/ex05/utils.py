"""Creating a function that counts the amount of times a number appears in a list!"""


__author__ = "730442926"


from typing import List


def count(num_list: List[int], counted_value: int) -> int:
    """Given a integer, this function counts how many times that integer is in the list."""
    mode_count_value: int = 0
    for num in num_list:
        if num == counted_value:
            mode_count_value += 1
    return mode_count_value


def all(number_list: List[int], important_num: int) -> bool:
    """Function that evaluates whether all the values in a list are the same."""
    mode_count_value: int = 0
    for num in number_list:
        if num == important_num:
            mode_count_value += 1
    if len(number_list) > 0:
        if mode_count_value == len(number_list):
            return True
    return False


def max(number_list: List[int]) -> int:
    """A function that finds the maximum value in a specific list."""
    if len(number_list) == 0:
        raise ValueError("max() argument is an empty list")
    max_value: int = number_list[0]
    for num in number_list:
        if num >= max_value:
            max_value = num
    return max_value


def is_equal(list_1: List[int], list_2: List[int]) -> bool:
    """Function call that evaluates if all the elements at every index of two lists are equal."""
    index_list_2: int = 0
    true_assertions: int = 0
    if len(list_1) != len(list_2):
        return False
    for num in list_1:
        if num == list_2[index_list_2]:
            true_assertions += 1
        index_list_2 += 1
    if true_assertions == len(list_1):
        return True
    return False


def concat(list_1: List[int], list_2: List[int]) -> List[int]:
    """Function that concatanates two list, the items from the first and then the items from second."""
    final_list: List[int] = []
    for num in list_1:
        final_list.append(num)
    for num in list_2:
        final_list.append(num)
    return final_list


def sub(num_list: List[int], start_value: int, end_value: int) -> List[int]:
    """Function that creates a list with values between the range given!"""
    converting_lenght_to_index: int = len(num_list) - 1
    new_list: List[int] = []
    
    if start_value < 0:
        start_value = 0
    if end_value > converting_lenght_to_index:
        end_value = converting_lenght_to_index + 1
    if start_value > converting_lenght_to_index:
        return new_list
    if end_value <= 0:
        return new_list
    if len(num_list) == 0:
        return new_list
    i: int = 0 + start_value
    while start_value <= i < end_value:
        new_list.append(num_list[i])
        i += 1 
    return new_list


def splice(list_1: List[int], insert_index: int, list_2: List[int]) -> List[int]:
    """A function that appends the second list at a specific index of the first list."""
    part_1: List[int] = sub(list_1, 0, insert_index)
    part_2: List[int] = sub(list_2, 0, len(list_2))
    part_3: List[int] = sub(list_1, insert_index, len(list_1))
    combined_list_1: List[int] = concat(part_1, part_2)
    combined_list_fin: List[int] = concat(combined_list_1, part_3)
    return combined_list_fin