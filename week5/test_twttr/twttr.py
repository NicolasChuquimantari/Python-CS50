def main():
    text = input("Enter text: ")
    output = shorten(word)
    print(output)



def shorten(word):
    vowels = ("a","e","i","o","u")
    n_word = []
    for char in word:
        if char not in vowels:
            n_word += char

    return n_word



if __name__ == "__main__":
    main()
