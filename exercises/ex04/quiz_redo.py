"""Quiz 00 redo, same exercises!"""


__author__ = "730442926"


LENGTH_TO_INDEX: int = 1
MIN_NUM_LETTERS: int = 3


def is_tar(word: str) -> bool:
    """Word has T, A, and R at the end?"""
    word.islower
    i: int = 0
    last_letter: int = len(word) - LENGTH_TO_INDEX
    if len(word) < MIN_NUM_LETTERS:
        return False
    if word[i] == "t" or word[i] == "T":
        i += 1
        if word[i] == "a" or word[i] == "A": 
            while word[i] == "a" or word[i] == "A":
                if i == last_letter:
                    return False
                i += 1
            if word[i] == "r" or word[i] == "R":
                if i == last_letter:
                    return True
            else:
                return False
        else:
            return False    
    return False


def boot(word: str, num1: int, num2: int) -> str:
    """Eliminating letters beteween range!"""
    i: int = 0 
    new_word: str = ""
    while i < len(word):
        if (num1 > i):
            letter_kept: str = word[i]
            new_word = new_word + letter_kept
            i = i + 1
        elif i > num2:
            letter_kept = word[i]
            new_word = new_word + letter_kept
            i = i + 1
        else: 
            i += 1
    return new_word
        

def sum_inputs() -> str:
    """Sum of numbers."""
    user_input: int = 0
    sum_num: int = 1
    while user_input != -1:
        user_input = int(input(" Enter an int, -1 to sum: "))
        sum_num = sum_num + user_input
    sum_string: str = "Sum is " + str(sum_num)
    return sum_string


def strip(word: str, side: str) -> str:
    """A function that erases spaces to the left or the right!"""
    output: str = ""
    side_undifined: str = "Has to be left or right"
    i: int = 0
    if side == "right":
        while word[i] == " ":
            output += word[i]
            i += 1
        while word[i] != " ":
            output += word[i]
            i += 1
        return output  
    if side == "left":
        while word[i] == " ":
            i += 1
        while i < len(word):  
            output = output + word[i]
            i += 1
        return output
    else:
        return side_undifined