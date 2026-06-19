import inflect
p = inflect.engine()

names = []

while True:
    try:
        text = input("Name: ")
        names.append(text)
    except EOFError:
        print()
        break

names_list = p.join(names)
print (f"Adieu, adieu, to {names_list}")

