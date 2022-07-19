from quiz.qz02_prep.basketball_team import find_avg_score, highest_and_lowest
from typing import List, Dict
def test_1_find_avg_score() -> None:
    """find_avg_score(data) --> {"tom": 40, "jack": 50}.
    where data: Dict[str, List[int]] = {
        "tom": [10, 30, 80],
        "jack": [20, 50, 100, 30]
    }
    """
    data: Dict[str, List[int]] = {
        "tom": [10, 30, 80],
        "jack": [20, 50, 100, 30]
    }
    assert find_avg_score(data) == {"tom": 40, "jack": 50}


def test_2_find_avg_score() -> None:
    """find_avg_score(data) --> {"rick": 0, "selena": 40}.
    where data: Dict[str, List[int]] = {
        "rick": [],
        "selena": [20, 50, 100, 30, 40]
    }
    """
    data: Dict[str, List[int]] = {
        "rick": [],
        "selena": [20, 50, 100, 30, 40]
    }
    assert find_avg_score(data) == {"rick": 0, "selena": 48}



def test_1_highest_and_lowest() -> None:
    """highest_and_lowest(data) --> {"max": "mary", "min": "Amanda"}.
    data: Dict[str, int] = {"mary": 1000, "katherine": 350, "amanda": 400}
    """
    data: Dict[str, int] = {"mary": 1000, "katherine": 350, "amanda": 400}
    assert highest_and_lowest(data) == {"max": "mary", "min": "katherine"}