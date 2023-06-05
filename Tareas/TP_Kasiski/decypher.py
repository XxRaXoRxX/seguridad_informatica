from functions import get_blocks, get_columns, _shift
import string

def _decypher(cyphertext, key):
    letters = string.ascii_uppercase
    shifts = [letters.index(letter) for letter in key]
    blocks = get_blocks(text=cyphertext,size=len(key))
    cols = get_columns(blocks)
    decyphered_blocks = to_blocks([_shift(col, shift) for col, shift in zip(cols, shifts)])
    decyphered = ''.join(decyphered_blocks)
    return decyphered

def to_blocks(cols):
    col_size = len(cols[0])
    blocks = []
    for letter in range(col_size):
        block = ''
        for col in range(len(cols)):
            block += cols[col][letter]
        blocks.append(block)
    return blocks