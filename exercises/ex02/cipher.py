"""Cipher and Decipher Machine!"""
__author__ = "730442926"


ASCII_NORMALIZING_NUM: int = 97
ALPHABET_LENGTH: int = 26
ASCII_CIPHERING: int = 1


def encode_char(character: str) -> str:
    """Encode Character Function."""
    lower_case_convert: str = character.lower()
    ascii_code: int = ord(lower_case_convert)
    normalized_code: int = ascii_code - ASCII_NORMALIZING_NUM
    encoded_code: int = (normalized_code + ASCII_CIPHERING) % ALPHABET_LENGTH + ASCII_NORMALIZING_NUM
    encoded_character: str = chr(encoded_code)
    return encoded_character


def encode_str(word: str) -> str:
    """Generating encoded word."""
    encoded_word: str = encode_char(word[0])
    encoded_word: str = encoded_word + encode_char(word[1])
    encoded_word: str = encoded_word + encode_char(word[2])
    encoded_word: str = encoded_word + encode_char(word[3])
    return encoded_word


def decode_char(character: str) -> str:
    """Decode Character Function."""
    lower_case_convert: str = character.lower()
    ascii_decode: int = ord(lower_case_convert)
    normalized_decode: int = ascii_decode - ASCII_NORMALIZING_NUM
    decoded_code: int = (normalized_decode - ASCII_CIPHERING) % ALPHABET_LENGTH + ASCII_NORMALIZING_NUM
    decoded_character: str = chr(decoded_code)
    return decoded_character


def decode_str(word: str) -> str:
    """Decoding encoded word."""
    decoded_word: str = decode_char(word[0])
    decoded_word: str = decoded_word + decode_char(word[1])
    decoded_word: str = decoded_word + decode_char(word[2])
    decoded_word: str = decoded_word + decode_char(word[3])
    return decoded_word     