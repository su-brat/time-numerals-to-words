from helpers.minutes_handler import get_minutes_in_word, get_minutes_to_pass
from helpers.hours_handler import get_hours_in_word, get_next_hour, get_12h_hour


def to_time(h: int, m: int) -> str:
    """returns time in words in the format 'twenty minutes to 6' for 5.40

    Args:
        h (int): hours in number
        m (int): minutes in number

    Returns:
        str: time in words
    """
    next_hour = get_next_hour(h)
    minutes_to_pass = get_minutes_to_pass(m)
    if next_hour and minutes_to_pass:
        minutes_in_word = get_minutes_in_word(minutes_to_pass)
        hours_in_word = get_hours_in_word(next_hour)
        if minutes_in_word and hours_in_word:
            return '{minutes} to {hours}'.format(minutes=minutes_in_word, hours=hours_in_word)
    return ''


def past_time(h: int, m: int) -> str:
    """returns time in words in the format 'forty minutes past 5' for 5.40

    Args:
        h (int): hours in number
        m (int): minutes in number

    Returns:
        str: time in words
    """
    hours = get_12h_hour(h)
    if hours:
        minutes_in_word = get_minutes_in_word(m)
        hours_in_word = get_hours_in_word(hours)
        if minutes_in_word and hours_in_word:
            if m == 0:  # Ex: For 5.00 -> five o' clock -> {hours} {minutes}
                return '{hours} {minutes}'.format(minutes=minutes_in_word, hours=hours_in_word)
            return '{minutes} past {hours}'.format(minutes=minutes_in_word, hours=hours_in_word)
    return ''
