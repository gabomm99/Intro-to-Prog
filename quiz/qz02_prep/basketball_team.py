from typing import List, Dict

def find_avg_score(players: Dict[str, List[int]]) -> Dict[str,int]:
    summary_stats: Dict[str,int] = {}
    for name in players:
        i = 0
        score_sum: int = 0
        while i < len(players[name]):
            score_sum += (players[name])[i]
            i += 1
        avg = int(score_sum/len(players[name]))
        summary_stats[name] = avg


    return summary_stats


def join_salary_data(players: Dict[int, str], salaries: Dict[int, int]) -> Dict[str, int]:
    name_salry: Dict[str, int] = {}
    for key in players:
        if key in salaries:
            name_salry[players[key]] = salaries[key]
        else:
            name_salry[players[key]] = -1

    return name_salry


def highest_and_lowest(items: Dict[str, int]) -> Dict[str, str]:
    max: int = -1 
    max_key: str = ""
    min: int = 50000
    min_key: str = ""
    for key in items:
        if max < items[key]:
            max = items[key]
            max_key = key
        if items[key] < min:
            min = items[key]
            min_key = key

    return {"max": max_key, "min": min_key}



def compare_scores(player: Dict[str, List[int]], num_games: int) -> str:
    consistent_player: str = ""
    frequency_max_score: List[str] = []
    return consistent_player


def for_proof(nombres: List[str], diccionario: Dict[str, int], word: str) -> None:

    for name in nombres:
        print(name)

    for nam in diccionario:
        print(nam)

    for let in word:
        print(let)
        

            



