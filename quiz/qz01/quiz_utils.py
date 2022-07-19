"""Responses for Quiz 01."""


__author__ = "730442926"


from typing import List 


def strs_to_floats(str_list: List[str]) -> List[float]:
    """A function that takes a list of strs and transforms it in a list of floats."""
    new_list: List[float] = []
    for n in str_list:
        new_list.append(float(n))
    return new_list


def lookup(str_list: List[str], float_list: List[float], important_word: str) -> float:
    """A function that looks for a string value on first list and returns!

    the respective float value from list 2 when found it.
    """
    if len(str_list) != len(float_list):
        raise ValueError("Lenght of lists are not equal")
    important_value: float = 0
    for i in range(len(str_list)):
        if important_word == str_list[i]:
            important_value = float_list[i]
            return important_value
    if important_value == 0:
        raise ValueError("Word was not found")
    return important_value 


def undelimit(delimited_word: str) -> List[str]:
    """A function that creates a list with all the words separated by commas!

    on the delimited string.
    """
    normalizing_length_to_index: int = len(delimited_word) - 1
    new_list: List[str] = []
    word: str = ""
    for i in range(len(delimited_word)):
        if delimited_word[i] != ",":
            word += delimited_word[i]
        if i == normalizing_length_to_index:
            new_list.append(word)
        elif delimited_word[i] == ",":
            new_list.append(word)
            word = ""      
    return new_list


def avg_column(stat_chart: List[str], stat_of_interest: str) -> float:
    """A function that takes the average of a specific column on a stat chart."""
    mutating_list: List[str] = stat_chart
    undelim_list_nums: List[str] = []
    j: int = 1
    while j < len(stat_chart):
        undelim_list_nums += undelimit(stat_chart[j])
        mutating_list.pop(1)
    mutating_list = undelimit(mutating_list[0])
    undelim_list_float: List[float] = strs_to_floats(undelim_list_nums)
    organized_num_list: List[float] = []
    i: int = 0
    while len(mutating_list) - i > 0:
        sum_per_item: float = 0
        for n in range(i, len(undelim_list_nums) - i, len(mutating_list)):
            sum_per_item += undelim_list_float[n]
        organized_num_list.append(sum_per_item)
        i += 1
    numerator_of_avg: float = lookup(mutating_list, organized_num_list, stat_of_interest)
    denominator_of_average: float = len(undelim_list_float) / len(mutating_list)
    mean: float = numerator_of_avg / denominator_of_average
    return mean