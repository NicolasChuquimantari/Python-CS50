while True:
    try:
        fraction = input("Enter fraction: ").split("/")
        x,y = fraction
        x = int(x)
        y = int(y)
        if x > y or y == 0 or x < 0:
            continue
        percentage = round((x / y) * 100)
        if percentage <= 1:
            print("E")
            break
        elif percentage >=99:
            print("F")
            break
        else:
            print(f"{percentage}%")
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break





