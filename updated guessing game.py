import random

winning_game = random.randint(1,100)
guess = 1
n = int(input("enter a number between 1 to 100 : "))
game_over = False
while not game_over:
    if n == winning_game:
        print(f"YOU WIN !!! , you tried {guess} times")
        game_over = True
    else:
        if n < winning_game:
            print("too low")
            guess += 1
            n = int(input("guess again : "))
        else:
            print("too high")
            guess += 1
            n = int(input("guess again : "))