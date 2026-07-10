import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hour := re.search(r"([0-9]{1,2})((:[0-9]{2})?) AM to ([0-9]{1,2})((:[0-9]{2})?) PM"):

#split into groups
        hour1 = hour.group(1)
        min1 = hour.group(2)

        hour2 = hour.group(3)
        min2 = hour.group(4)





if __name__ == "__main__":
    main()
