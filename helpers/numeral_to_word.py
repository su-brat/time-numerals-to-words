def get(number: int) -> str:
    number_map = ["zero", "one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine",
                  "ten", "eleven", "twelve", "thirteen",
                  "fourteen", "fifteen", "sixteen",
                  "seventeen", "eighteen", "nineteen",
                  "twenty", "twenty one", "twenty two",
                  "twenty three", "twenty four",
                  "twenty five", "twenty six", "twenty seven",
                  "twenty eight", "twenty nine"]
    if number in range(0, 30, 1):
        return number_map[number]
    return ''
