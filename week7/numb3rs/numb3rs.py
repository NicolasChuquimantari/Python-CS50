import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipv4 = ip.split(".")
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        for number in ipv4:
            if int(number)<0 or int(number)>255:
                return False

        return True

    return False


if __name__ == "__main__":
    main()
