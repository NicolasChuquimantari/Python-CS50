import sys


if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as file:
        for line in file:
            



