from helpers import numeral_to_word


def get_minutes_in_word(m: int) -> str:
    if m == 0:
        return "o' clock"
    if m == 1:
        return 'one minute'
    if m == 15:
        return 'quarter'
    if m == 30:
        return 'half'
    if m in range(1, 60, 1):
        numeral_in_word = numeral_to_word.get(m)
        if numeral_in_word:
            return '{} minutes'.format(numeral_in_word)
    return ''


def get_minutes_to_pass(m: int) -> int | None:
    if m in range(0, 60, 1):
        return 60 - m
    return None
