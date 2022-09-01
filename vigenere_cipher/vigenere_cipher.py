import re
p = re.compile('^[a-z]$')

M = "attack at dawn"
K = "lemon"
C = "lxfopv mh oeib"

offset_a = ord('a')
length_alphabet = ord('z') - offset_a + 1

def shift_character(char:str, key:str, sign:int)->int:
    """Return the character shifted by the key."""

    return chr((character_to_pos(char) + sign * character_to_pos(key)) % length_alphabet + offset_a)

def character_to_pos(char:str)->int:
    """Return the position of relative to Unicode code point of 'a'."""

    return ord(char) - offset_a

def is_alphabet(character:str) -> bool:
    """Return whether character is alphabet."""

    return p.match(character)

def encrypt_charater(arg:tuple[str, int])->str:
    """Return the character of the cipher encrypted by the key if char is alphabet."""

    char, key = arg
    return shift_character(char,key,1) if is_alphabet(char) else char

def encrypt_message(message: str, key: str)->str:
    """Return the cipher by the key."""
    repeated_key = make_reapeated_key(key,len(message))
    return ''.join(map(encrypt_charater,zip(message,repeated_key)))


def decrypt_charater(arg:tuple[str, int])->str:
    """Return the character of the cipher decrypted by the key if char is alphabet."""

    char, key = arg
    return shift_character(char,key,-1) if is_alphabet(char) else char

def decrypt_message(message: str, key: str)->str:
    """Return the cipher by the key."""

    repeated_key = make_reapeated_key(key,len(message))
    return ''.join(map(decrypt_charater,zip(message,repeated_key)))

def make_reapeated_key(key:str,length:int)->str:
    """Return the repeated key of the given length"""

    repeated_key = key
    while len(repeated_key) < length:
        repeated_key += key
    return repeated_key[:length]