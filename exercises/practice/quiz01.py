

from typing import List, Tuple

def orderPrice(order: List[str], menu: List[str], prices: List[float]) -> float:
    check: float = 0
    for item in order:
        not_in_menu: bool = False
        for i in range(len(menu)):
            if item == menu[i]:
                check += prices[i]
                not_in_menu = True 
        if not_in_menu == False:
            check += 2.00
    return check


def sortScores(scores: List[int]) -> List[int]:
    if len(scores) == 0:
        return []
    mutating_list: List[int] = scores
    ordered_scores: List[int] = []
    for grade in range(len(scores)):
        num_to_add: int = min_helper(mutating_list)
        ordered_scores.append(mutating_list[num_to_add])
        mutating_list.pop(num_to_add)
    return ordered_scores


def min_helper(num_list: List[int]) -> int:
    min_num: int = num_list[0]
    min_ind: int = 0
    for n in range(len(num_list)):
        if num_list[n] < min_num:
            min_num = num_list[n]
            min_ind = n
    return min_ind


def scoreStats(scores: List[int]) -> Tuple[int, int]:
    arranged_list: List[int]= sortScores(scores)
    mean_denominator: float = len(arranged_list)
    sum_of_values: float = 0
    meadian: float = 0
    mean: float = 0
    midpoint_odd: int = round(len(arranged_list)/2)
    if mean_denominator % 2 == 0:
        meadian = (arranged_list[midpoint_odd] + arranged_list[midpoint_odd - 1]) / 2
    else:
        meadian = arranged_list[midpoint_odd - 1 ]
    for n in arranged_list:
        sum_of_values += n
    mean = sum_of_values/mean_denominator
    return (round(mean), round(meadian))



def multiplyTable(table_of: int, every: int, end_at: int) -> List[int]:
    final_table: List[int] = []
    if every == 0:
        return final_table
    if end_at == 0:
        return final_table
    for num in range(1, end_at + 1, every):
        new_num: int = table_of * num
        final_table.append(new_num)
    return final_table