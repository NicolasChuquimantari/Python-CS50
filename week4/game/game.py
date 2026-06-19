import random

while True:
    try:
        level_n = int(input("Level: "))
        if level_n > 0:
            break
    except ValueError:
        continue

number = random.randint(1, level_n)

while True:
     try:
         guess = int(input("Guess: "))
         if guess > 0:
             if guess > number:
                 print("Too large!")
             elif guess < number:
                 print("Too small!")
             else:
                 print("Just right!")
                 break
     except ValueError:
         continue















