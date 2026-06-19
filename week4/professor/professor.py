import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for i in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                if answer != x + y:
                    print("EEE")
                else:
                    print("EEE")
            except ValueError:
                continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                continue
            return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
