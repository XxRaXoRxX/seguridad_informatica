from length import *
from decypher import _decypher
from key import *
from constants import *

def main():
    key_len = find_key_length(ENCODE, SEQ_LEN, MAX_KEY_LEN)
    key = restore_key(ENCODE, key_len)
    decyphered = _decypher(ENCODE, key)
    print('Chosen key length: '+str(key_len))
    print('Restored key: '+str(key))
    print('Plaintext: '+str(decyphered))

if __name__ == "__main__":
    main()