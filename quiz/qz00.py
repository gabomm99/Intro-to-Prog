"""Response for Quiz 0"""
__authot__ = "730442926"


def is_tar(word: str) -> bool:
    """Word has T, A, and R at the end?"""
    if word[0] == "t":
        i: int = 1
        while word[i] == "a":
            i = i + 1
            if word[i] == "r":
                return True
    return False


def boot(word:str, num1: int, num2: int) -> str:
    """Eliminating letters beteween range"""
    new_word: str = ""
    i: int = 0 
    while i < len(word):
      if num1 > i > num2:
        letter_kept: str = word[i]
        new_word == new_word + letter_kept
      i = i + 1
    return new_word



def sum_inputs() -> str:
    """Sum of numbers."""
    user_input: str = input("Enter an int, -1 to sum: ")
    sum_num: int = 0
    sum_string: str = "Sum is "
    while  user_input != str(-1):
        user_input = input(" Enter an int, -1 to sum: ")
        sum_num = sum_num + int(user_input)
    return sum_string + str(sum_num)

