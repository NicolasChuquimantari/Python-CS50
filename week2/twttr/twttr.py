def main():
    text = input("Please enter your text: ")
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

    for c in text:
        if c in vowels:
            continue
        else:
            print(c, end = "")

main()

