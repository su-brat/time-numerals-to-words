"""
Given the time in numerals we may convert it into words, as shown below:
    5.00 -> five o'clock
    5.01 -> one minute past five
    5.10 -> ten minutes past five
    5.15 -> quarter past five
    5.30 -> half past five
    5.40 -> twenty minutes to six
    5.45 -> quarter to six
    5.47 -> thirteen minutes to six
    5.28 -> twenty eight minutes past five
    
"""

from helpers.time_integrator import to_time, past_time


def get_in_words(h: int, m: int) -> str:
    """converts hours and minutes in numbers to words

    Args:
        h (int): hrs in number
        m (int): minutes in number

    Returns:
        str: word representation of h hours and m minutes
    """
    if m > 30:
        worded_time = to_time(h, m)
    else:
        worded_time = past_time(h, m)
    return worded_time
