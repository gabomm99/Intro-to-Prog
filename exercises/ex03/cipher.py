"""Cipher and Decipher Machine Improved!"""
__author__ = "730442926"


ASCII_NORMALIZING_NUM: int = 97
ALPHABET_LENGTH: int = 26
ASCII_CIPHERING: int = 1
ASCII_NORMALIZING_UPPER: int = 65


def encode_char(character: str) -> str:
    """Encode Character Function."""
    if character.islower():
        ascii_code: int = ord(character)
        normalized_code: int = ascii_code - ASCII_NORMALIZING_NUM
        encoded_code: int = (normalized_code + ASCII_CIPHERING) % ALPHABET_LENGTH + ASCII_NORMALIZING_NUM
        encoded_character: str = chr(encoded_code)
        return encoded_character
    else:
        ascii_code_upper: int = ord(character)
        normalized_code_upper: int = ascii_code_upper - ASCII_NORMALIZING_UPPER
        encoded_code_upper: int = (normalized_code_upper + ASCII_CIPHERING) % ALPHABET_LENGTH + ASCII_NORMALIZING_UPPER
        encoded_character_upper: str = chr(encoded_code_upper)
        return encoded_character_upper
        

def encode_str(word: str) -> str:
    """Generating encoded word."""
    i: int = 0
    sum_all_letters: str = ""
    while i < len(word):
        letter: str = encode_char(word[i])
        sum_all_letters = sum_all_letters + letter
        i = i + 1
    return sum_all_letters


def decode_char(character: str) -> str:
    """Decode Character Function."""
    if character.islower():
        ascii_decode: int = ord(character)
        normalized_decode: int = ascii_decode - ASCII_NORMALIZING_NUM
        decoded_code: int = (normalized_decode - ASCII_CIPHERING) % ALPHABET_LENGTH + ASCII_NORMALIZING_NUM
        decoded_character: str = chr(decoded_code)
        return decoded_character
    else:
        ascii_decode_up: int = ord(character)
        normalized_decode_upper: int = ascii_decode_up - ASCII_NORMALIZING_UPPER
        decoded_code_up: int = (normalized_decode_upper - ASCII_CIPHERING) % ALPHABET_LENGTH + ASCII_NORMALIZING_UPPER
        decoded_character_upper: str = chr(decoded_code_up)
        return decoded_character_upper


def decode_str(word: str) -> str:
    """Decoding encoded word."""
    i: int = 0
    sum_all_letters_decode: str = ""
    while i < len(word):
        letter: str = decode_char(word[i])
        sum_all_letters_decode = sum_all_letters_decode + letter
        i = i + 1
    return sum_all_letters_decode