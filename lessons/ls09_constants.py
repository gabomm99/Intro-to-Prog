"""Some example of constants and functions"""

from random import choice 

VOWELS: str = "aeiouy"
CONSONANTS: str = "bcdfghjklmnpqrstuvwxz"



def random_letter(letters: str) -> str:
    """Given alphabet, select one letter"""
    letter: str = choice(letters)
    return letter

def random_word() -> str:
    """Generate random 4 letter word"""
    word: str 
    word = random_letter(CONSONANTS) 
    word = word + random_letter(VOWELS)
    word = word + random_letter(VOWELS)
    word = word + random_letter(CONSONANTS) 
    return word 


