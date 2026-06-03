def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not numbers(s):
        return False
    return True


def numbers(s):
    number = False

    for char in s:
        if char.isdigit():
            number = True
        if char.isalpha():
            if number:
                return False


main()
