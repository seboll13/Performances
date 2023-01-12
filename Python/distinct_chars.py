from time import time
from string import ascii_lowercase
from random import randint

WINDOW_SIZE = 14
MAX_ITERATIONS = 10_000
DEFAULT_STRG_LENGTH = 1000

chars = ascii_lowercase
fpath = 'test_string.txt'


def avgtime(func):
    def wrapper(*args, **kwargs):
        start = time()
        for _ in range(MAX_ITERATIONS):
            func(*args, **kwargs)
        end = time()
        print(f"Average time elapsed: {1000*(end - start)/MAX_ITERATIONS:.3f} [ms]")
    return wrapper


def create_string(length):
    return ''.join([chars[randint(0, len(chars) - 1)] for _ in range(length)])


@avgtime
def find_lastpos_of_14_first_distinct_chars_take1(string) -> int:
    for _ in range(len(string)-WINDOW_SIZE):
        if len(set(string[_:_+WINDOW_SIZE])) == WINDOW_SIZE:
            return _+WINDOW_SIZE
    return -1


@avgtime
def find_lastpos_of_14_first_distinct_chars_take2(string) -> int:
    for _ in range(len(string)-WINDOW_SIZE):
        curr = string[_:_+WINDOW_SIZE]
        for char in curr:
            if curr.count(char) > 1:
                break
        else:
            return _+WINDOW_SIZE
    return -1


@avgtime
def find_lastpos_of_14_first_distinct_chars_take3(string) -> int:
    _dict = {}
    lower_bound, upper_bound = 0, WINDOW_SIZE-1
    _ = lower_bound
    while _ < upper_bound:
        curr_char = string[_]
        if curr_char in _dict:
            lower_bound = _dict[curr_char]+1
            upper_bound = WINDOW_SIZE+_dict[curr_char]+1
            _dict = {k:v for k,v in _dict.items() if v >= lower_bound}
        _dict[curr_char] = _
        _ += 1
        if len(_dict) == WINDOW_SIZE:
            return upper_bound
    return -1


@avgtime
def find_lastpos_of_14_first_distinct_chars_take4(string) -> int:
    _dict = {}
    lower_bound = 0
    for _ in range(len(string)):
        curr_char = string[_]
        if curr_char in _dict and _dict[curr_char] >= lower_bound:
            lower_bound = _dict[curr_char]+1
        _dict[curr_char] = _
        _+=1
        if _-lower_bound== WINDOW_SIZE:
            return _
    return -1


if __name__ == '__main__':
    _str = create_string(DEFAULT_STRG_LENGTH)
    find_lastpos_of_14_first_distinct_chars_take1(_str)
    find_lastpos_of_14_first_distinct_chars_take2(_str)
    find_lastpos_of_14_first_distinct_chars_take3(_str)
    find_lastpos_of_14_first_distinct_chars_take4(_str)
    print('Done.')
    