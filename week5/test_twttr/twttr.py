def main():
    text = input("Enter text: ")
    output = shorten(word)
    print(output)



def shorten(word):
    vowels = ("a","e","i","o","u")
    for char in word:
        if char not in vowels:
            return 



if __name__ == "__main__":
    main()
