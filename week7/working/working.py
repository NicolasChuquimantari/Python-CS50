import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hour := re.search(r"([0-9]{1,2})((:[0-9]{2})?) AM to ([0-9]{1,2})((:[0-9]{2})?) PM"):
        




if __name__ == "__main__":
    main()
