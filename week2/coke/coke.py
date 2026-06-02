coke_price = 50
due = coke_price

while due > 0:
    print(f"Amount Due: {due}")
    insert_coin = int(input("Insert Coin: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        due -= insert_coin
if due == 0:
    print("Change Owed: 0")
elif due < 0:
    due = -due

print(f"Change Owed: {due}")

