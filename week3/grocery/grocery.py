grocery_dict = {}

while True:
    try:
        item = input().upper()
        if item in grocery_dict:
            grocery_dict[item] += 1
        else:
            grocery_dict[item] = 1
    except EOFError:
        break

sorted_dict = sorted(grocery_dict)
for item in sorted(grocery_dict):
    print(grocery_dict[item],item)

