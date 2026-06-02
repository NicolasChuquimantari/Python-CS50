def main():
    camel_text= input("Enter text: ")
    snake_text= ""

    for c in camel_text:
        if c.isupper():
            snake_text = snake_text + "_" + c.lower()
        else:
            snake_text = snake_text + c

    print(snake_text)


main()
