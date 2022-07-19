"""A program that analyzes atmospheric data from the JFK airport at Queenss, New York.

It uses the data to do basic opeations like average, minimum value, and maximum value.
"""


__author__ = "730442926"


import sys

from csv import DictReader

from typing import Dict, List


CLI_DIC_KEY_1: str = "FILE"
CLI_DIC_KEY_2: str = "COLUMN"
CLI_DIC_KEY_3: str = "OPERATION"
CLI_LIST_INDEX_1: int = 1
CLI_LIST_INDEX_2: int = 2
CLI_LIST_INDEX_3: int = 3
CLI_LIST_REQUIRED_LENGTH: int = 4
OPERATION_1: str = "list"
OPERATION_2: str = "min"
OPERATION_3: str = "max"
OPERATION_4: str = "avg"
OPERATION_5: str = "chart"
DATE_COLUMN_KEY: str = "DATE"
REPORT_COLUMN_KEY: str = "REPORT_TYPE"
REPORT_COLUMN_VALUE: str = "SOD  "
LENGTH_OF_DATES: int = 10


def main() -> None:
    """Entrypoint of program run as module. This program prints a list of floats!

    or minimum value! or maximum value! or average! of a column in a weather dataset.
    """
    args: Dict[str, str] = check_args()
    file_opened: DictReader = data_file_reader(args[CLI_DIC_KEY_1])
    column_of_interest: List[float] = list_operation(file_opened, args[CLI_DIC_KEY_2])
    if args[CLI_DIC_KEY_3] == OPERATION_1:
        print(column_of_interest)
    elif args[CLI_DIC_KEY_3] == OPERATION_2:
        min_value: float = min(column_of_interest)
        print(min_value)
    elif args[CLI_DIC_KEY_3] == OPERATION_3:
        max_value: float = max(column_of_interest)
        print(max_value)
    elif args[CLI_DIC_KEY_3] == OPERATION_4:
        avg_value: float = (sum(column_of_interest) / len(column_of_interest))
        print(avg_value)
    elif args[CLI_DIC_KEY_3] == OPERATION_5:
        file_opened_2: DictReader = data_file_reader(args[CLI_DIC_KEY_1])
        dates: List[str] = date_list(file_opened_2, args[CLI_DIC_KEY_2])
        chart_data(column_of_interest, args[CLI_DIC_KEY_2], dates)
    else:
        print(f"Invalid operation: {args[CLI_DIC_KEY_3]}")

 
def check_args() -> Dict[str, str]:
    """Check for valid arguments and return in Dictionary with CLI arguments and keys for each of them."""
    if len(sys.argv) != CLI_LIST_REQUIRED_LENGTH:
        print(f"Usage: python -m projects.pj01.weather [{CLI_DIC_KEY_1}] [{CLI_DIC_KEY_2}] [{CLI_DIC_KEY_3}]")
        exit()
    return {
        CLI_DIC_KEY_1: sys.argv[CLI_LIST_INDEX_1],
        CLI_DIC_KEY_2: sys.argv[CLI_LIST_INDEX_2],
        CLI_DIC_KEY_3: sys.argv[CLI_LIST_INDEX_3]
    }


def data_file_reader(file_path: str) -> DictReader:
    """Function that opens a data file and cretes dictionaries with columns and rows."""
    file_handle = open(file_path, "r", encoding="utf8")
    csv_reader: DictReader = DictReader(file_handle)
    file_handle.close
    return csv_reader


def list_operation(data_file: DictReader, column: str) -> List[float]:
    """Function that creates a list of floats of SOD readings for a specific column!

    And it also checks for the existence of the column in question!
    """
    results_list: List[float] = []
    for row in data_file:
        if column not in row:
            print(f"Invalid column: {column}")
            exit()
        if row[REPORT_COLUMN_KEY] == REPORT_COLUMN_VALUE:
            try:
                results_list.append(float(row[column]))
            except ValueError:
                ...
    return results_list


def chart_data(data: List[float], column: str, dates: List[str]) -> None:
    """A function that edits a list of dates and times plots a scatter plot of all the SOD!
    
    atmospheric data under a specific column!
    """
    import matplotlib.pyplot as plt
    edited_dates: List[str] = date_editor(dates)
    plt.scatter(edited_dates, data)
    plt.xticks(fontsize=4)
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.show()


def date_list(data_file: DictReader, column: str) -> List[str]:
    """Function that creates a list of str for the DATES of SOD readings in relation to a specific column!"""
    list_of_dates: List[str] = []
    results_list: List[float] = []
    for row in data_file:
        if row[REPORT_COLUMN_KEY] == REPORT_COLUMN_VALUE:
            try:
                results_list.append(float(row[column]))
                list_of_dates.append(row[DATE_COLUMN_KEY])
            except ValueError:
                ...
    return list_of_dates

    
def date_editor(dates_list: List[str]) -> List[str]:
    """A function that takes a list of dates and times, and changes it to only dates."""
    edited_dates: List[str] = []
    for date in dates_list:
        i = 0
        new_date: str = ""
        while i < LENGTH_OF_DATES:
            new_date += date[i]
            i += 1
        edited_dates.append(new_date)
    return edited_dates


if __name__ == "__main__":
    main()