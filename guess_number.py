i = 1
while i <= 3 :
    guess = int(input("Guess a number: "))
    i += 1
    if guess == 9:
        print("You win")
        break
else:
    print("you lose")
