Winning_game = 8
guess = int(input("guess any number between 1 to 100 : "))
print(f"you guess number is {guess}")
if Winning_game > guess:
    print("too low")
if Winning_game < guess:
    print("too high")
if Winning_game == guess:
    print("YOU WIN!!!")
