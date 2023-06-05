from math import sqrt
import string

SEQ_LEN = 7
MAX_KEY_LEN = 8
EN_REL_FREQ = {'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228, 'G': 0.02015,
               'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749,
               'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 'U': 0.02758,
               'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074}
ES_REL_FREQ = {'A': 0.1152, 'B': 0.022, 'C': 0.0414, 'D': 0.0501, 'E': 0.1218, 'F': 0.0069, 'G': 0.0172,
               'H': 0.0079, 'I': 0.0569, 'J': 0.0046, 'K': 0.0004, 'L': 0.054, 'M': 0.0309, 'N': 0.0671,
               'Ñ': 0.0031, 'O': 0.0868, 'P': 0.0251, 'Q': 0.0088, 'R': 0.0687, 'S': 0.0798, 'T': 0.0463,
               'U': 0.0278, 'V': 0.0071, 'W': 0.0011, 'X': 0.001, 'Y': 0.0069, 'Z': 0.0049}
ENCODE = "PZEPHCIZYOYMBAPGIDLZMQEMAOCTRQOHGSDAXLYAIVUWKLCFHKZZDZCFZWYOAQOTTZZELWOWDTSMKWVZTFCMIWTLHGSMWWGKCCEETVVUDBQTBKVKDGSMWMEASSDBHOTSCHUWKLCFLVLBAMTWFIPAMACFSYPMIPKEWOAXRCPKJFAZBAKFVZJRHZFSCGNWETGSVIPAKMISGRSQFIUEPBTXNTCLXJPIGLRMHVJJNBVZTMOMVQFWICYWMZCAHSEPXQUKJSTVMPGZDDPBAIVBPBPIIXTWRWLBXAVZTWCIMBKLJRPIGLVZPHEPXQTSRVTMOMOWCHDAIMCCUCCBAMOKTZGMLACVAMEPXQTKIFLBXOAAHTLZEMUKTTQMVBKNTHSIGRQJSOYAPPKUWQLCLMUEDFPWYRCFTGCMIWTLHHZJNTNQWSCQGBQSEFZUHBKGC"

def _repeated_seq_pos(text, seq_len):
    seq_pos = {}  # entries of sequence : [positions]
    for i, char in enumerate(text):
        next_seq = text[i:i+seq_len]
        if next_seq in seq_pos.keys():
            seq_pos[next_seq].append(i)
        else:
            seq_pos[next_seq] = [i]
    repeated = list(filter(lambda x: len(seq_pos[x]) >= 2, seq_pos))
    rep_seq_pos = [(seq, seq_pos[seq]) for seq in repeated]
    return rep_seq_pos

def _get_spacings(positions):
    return [positions[i+1] - positions[i] for i in range(len(positions)-1)]

def _get_factors(number):
    factors = set()
    for i in range(1, int(sqrt(number))+1):
        if number % i == 0:
            factors.add(i)
            factors.add(number//i)
    return sorted(factors)

def _candidate_key_lengths(factor_lists, max_key_len):
    all_factors = [factor_lists[lst][fac] for lst in range(len(factor_lists)) for fac in range(len(factor_lists[lst]))]
    # exclude factors larger than suspected max key length
    candidate_lengths = list(filter(lambda x:  x <= max_key_len, all_factors))
    # sort by probability (descending)
    sorted_candidates = sorted(set(candidate_lengths), key=lambda x: all_factors.count(x), reverse=True)
    return sorted_candidates

def find_key_length(cyphertext, seq_len, max_key_len):
    # find repeated sequences and their positions
    rsp = _repeated_seq_pos(text=cyphertext, seq_len=seq_len)
    seq_spc = {}
    for seq, positions in rsp:
        seq_spc[seq] = _get_spacings(positions)
    # calculate spacings between positions of each repeated
    # sequence and factor out spacings
    factor_lists = []
    for spacings in seq_spc.values():
        for space in spacings:
            factor_lists.append(_get_factors(number=space))
    # get common factors by descending frequency,
    # which constitute candidate key lengths
    ckl = _candidate_key_lengths(factor_lists=factor_lists, max_key_len=max_key_len)
    key_len = ckl[0]
    return key_len

def _find_key_letter(text, lf):
    key_letter = ''
    max_corr = 0
    for count, letter in enumerate(string.ascii_uppercase):
        shifted = _shift(text=text, amount=count)
        corr = _corr(text=shifted, lf=lf)
        if corr > max_corr:
            max_corr = corr
            key_letter = letter
    return key_letter

def _shift(text, amount):
    shifted = ''
    letters = string.ascii_uppercase
    for letter in text:
        shifted += letters[(letters.index(letter)-amount) % len(letters)]
    return shifted

def get_letter_counts(text):
    text_upper = text.upper()
    letter_counts = {}
    for index, letter in enumerate(string.ascii_uppercase):
        letter_counts[letter] = text_upper.count(letter)
    return letter_counts

def _corr(text, lf):
    return sum([(lf[letter]*EN_REL_FREQ[letter]) for letter in text])

def get_blocks(text, size):
    blocks = [text[i:i+size] for i in range(0, len(text)-size, size)]
    return blocks

def _get_letter_frequencies(text):
    letter_counts = get_letter_counts(text)
    frequencies = {letter: count/len(text) for letter, count in letter_counts.items()}
    return frequencies


def get_columns(text_blocks):
    group_size = len(text_blocks[0])
    columns = []
    for letter_count in range(group_size):
        column = ''
        for group_count in range(len(text_blocks)):
            column += text_blocks[group_count][letter_count]
        columns.append(column)
    return columns


def to_blocks(cols):
    col_size = len(cols[0])
    blocks = []
    for letter in range(col_size):
        block = ''
        for col in range(len(cols)):
            block += cols[col][letter]
        blocks.append(block)
    return blocks

def restore_key(cyphertext, key_len):
    key = ''
    blocks = get_blocks(text=cyphertext, size=key_len)
    columns = get_columns(blocks)
    frequencies = _get_letter_frequencies(text=cyphertext)
    for column in columns:
        key += _find_key_letter(text=column, lf=frequencies)
    return key

def _decypher(cyphertext, key):
    letters = string.ascii_uppercase
    shifts = [letters.index(letter) for letter in key]
    blocks = get_blocks(text=cyphertext,size=len(key))
    cols = get_columns(blocks)
    decyphered_blocks = to_blocks([_shift(col, shift) for col, shift in zip(cols, shifts)])
    decyphered = ''.join(decyphered_blocks)
    return decyphered

def main():
    key_len = find_key_length(ENCODE, SEQ_LEN, MAX_KEY_LEN)
    key = restore_key(ENCODE, key_len)
    decyphered = _decypher(ENCODE, key)
    print('Chosen key length: '+str(key_len))
    print('Restored key: '+str(key))
    print('Plaintext: '+str(decyphered))

if __name__ == "__main__":
    main()