"""Examples of sequences"""

from typing import Tuple
from typing import List

Color = Tuple[int, int, int]


def main() -> None:
    """Example of sequences"""
    a_list: List[int] = [110, 210, 211, 301, 311]
    print(a_list)

    #Access items using subscription notation:
    i: int = 0
    while i < len(a_list):
        print(a_list[i])
        i += 1

    names: List[str] = ["Gabo", "July","Juli"]
    print (names)

    names.append("Marc")
    print(names)



def brigther(a_color: Color) -> Color:
    """Return a brigther color"""
    red: int = int(a_color[0] * 1.1)
    green: int = int(a_color[1] * 1.1)
    blue: int = int(a_color[2] * 1.1)
    return(red, green, blue)
    


if __name__ == "__main__":
    main()

