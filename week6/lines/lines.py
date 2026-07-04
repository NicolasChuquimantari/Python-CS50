import sys


if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as file:
        count_line = 0
        for line in file:
            if line.strip() and not line.lstrip().startswith("#"):
                 count_line +=1

    print(count_line)

except FileNotFoundError:
        sys.exit("File does not exist")






