import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if web_link := re.search(r'<iframe.+?src="https?://(www\.)?youtube\.com/embed/(\w+)"', s):
        return f"https://youtu.be/{web_link.group(2)}"

if __name__ == "__main__":
    main()
