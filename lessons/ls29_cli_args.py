import sys

from typing import List, Dict


def main() -> None:
    """Entrypoint of program run as module."""
    args: Dict[str, str] = read_args()
    results: List[str] = search_file(args["file_path"], args["keyword"])
    show_res(results)



def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments and return in Dictionary."""
    if len(sys.argv) != 3:
        print("Usage: python -m lessons.ls29_cli_args [file] [keyword]")
        exit()
    return {
        "file_path": sys.argv[1],
        "keyword" :sys.argv[2]
    }


def search_file(file_path: str, keyword: str) -> List[str]:
    """Open & reads each line and returns a List of lines w/ keayword."""
    matches: List[str] = []
    file_door = open(file_path, "r", encoding="utf8")
    for line in file_door:
        if keyword in line:
            matches.append(line)
    file_door.close
    return matches


def show_res(matches: List[str]) -> None:
    """Print out all lines containing the search term and the total num of matches."""
    for line in matches:
        print(line.strip())
    print("Total matches: " + str(len(matches)))
# Run our program as a module with two comman-line arguments:
# 1. Name of the file to search
# 2. Search term we are looking for




if __name__ == "__main__":
    main()