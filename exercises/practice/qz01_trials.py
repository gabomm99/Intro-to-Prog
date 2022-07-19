
from typing import List
from quiz.qz01.quiz_utils import undelimit, strs_to_floats, lookup
def avg_column(stat_chart: List[str], stat_of_interest: str) -> List[str] and List[str]:
    """A function that takes the average of a specific column on a stat chart."""
    mutating_list: List[str] = stat_chart
    undelim_list_nums: List[str] = []
    j: int = 1
    while j < len(stat_chart):
        undelim_list_nums += undelimit(stat_chart[j])
        mutating_list.pop(1)
    return mutating_list and undelim_list_nums


def avg_column_2(stat_chart: List[str], stat_of_interest: str) -> List[float]:
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
    return organized_num_list


def avg_column_3(stat_chart: List[str], stat_of_interest: str) -> float:
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
    denominator_of_average: float = (len(undelim_list_float)/len(mutating_list)) 
    mean: float = numerator_of_avg/denominator_of_average
    return mean