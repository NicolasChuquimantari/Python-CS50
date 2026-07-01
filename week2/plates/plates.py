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

        if not char.isalpha() and not char.isdigit():
            return False

        if char.isdigit():
            if char == "0" and not number:
                return False
            number = True

        if char.isalpha():
            if number:
                return False

    return True


if __name__ == "__main__":
    main()
