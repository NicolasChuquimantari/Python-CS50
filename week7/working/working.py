import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hour := re.search(r"([0-9]{1,2})(:[0-9]{2})? (AM|PM)? to ([0-9]{1,2})(:[0-9]{2})? (AM|PM)", s):

#split into groups
        hour1 = hour.group(1)
        min1 = hour.group(2)
        timeday1 = hour.group(3)

        hour2 = hour.group(4)
        min2 = hour.group(5)
        timeday2 = hour.group(6)

#validate time
    if hour1 < 0 or hour1 > 12:
        raise ValueError
    if hour2 < 0 or hour2 > 12:
        raise ValueError

    if min1 < 0 or min1 > 59:
        raise ValueError
    if min2 < 0 or min2 > 59:
        raise ValueError






if __name__ == "__main__":
    main()
