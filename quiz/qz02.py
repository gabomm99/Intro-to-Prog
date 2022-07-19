"""Responses for code writting for Quiz 02!"""


__author__ = "730442926"


from typing import List, Dict


def abbreviate(names: List[str]) -> Dict[str, str]:
    """A function that abbreviates names by taking only the capital letters within the name!"""
    abbrevi_dictionary: Dict[str, str] = {}
    for word in names:
        new_value: str = single_str_help(word)
        abbrevi_dictionary[word] = new_value
    return abbrevi_dictionary


def single_str_help(name: str) -> str:
    """A helper finction that takes a single string and returns only the capital letters in it."""
    abbrevi_str: str = ""
    for letter in name:
        if letter.isupper():
            abbrevi_str += letter
    return abbrevi_str


def phonebook(phone_num: List[int], phone_owner: List[str]) -> Dict[int, str]:
    """A function that takes a list of phone numbers and matches them with their owners!

    through a Dictionary of integers and abbreviated strings.
    """
    if len(phone_num) != len(phone_owner):
        raise ValueError
    num_owner: Dict[int, str] = {}
    i: int = 0
    while i < len(phone_num):
        num_owner[phone_num[i]] = single_str_help(phone_owner[i])
        if num_owner[phone_num[i]] == "":
            num_owner.pop(phone_num[i])  
        i += 1
    return num_owner


def find_ppl_in_area(phone_name: Dict[int, str], area_code: int) -> List[str]:
    """A function that looks and groups together all the initials of the people with the!

    area code givin in the arguments!
    """
    area_co_length: int = 3
    if len(str(area_code)) != area_co_length:
        raise ValueError
    converted_area_co: str = str(area_code)
    ppl_around: List[str] = []
    for owner in phone_name:
        converted_key: str = str(owner)
        i: int = 0
        while i < area_co_length:
            if converted_key[i] == converted_area_co[i]:
                i += 1
                if i == area_co_length:
                    ppl_around.append(phone_name[owner])
            else:
                i += area_co_length    
    return ppl_around