from helpers import numeral_to_word


def get_hours_in_word(h: int) -> str:
    if h in range(1, 13, 1):
        return numeral_to_word.get(h)
    return ''


def get_12h_hour(h: int) -> int | None:
    if h in range(0, 24, 1):
        # converts all 12h or 24h format to 12h format
        return ((h - 1) % 12) + 1


def get_next_hour(h: int) -> int | None:
    """returns next hour in 12h format

    Args:
        h (int): hour in 12h or 24h format

    Returns:
        int: next hour in 12h format
    """
    if h in range(0, 24, 1):
        next_hour = (h % 12) + 1  # 12.31 -> twenty nine minutes to one, \
        # also converts all 24h format to 12h format
        return next_hour
