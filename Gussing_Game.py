import random
secret_number = random.randint(1,100)
print(" Welcome to Guessing Game!!!\n",
      "Guess a number between 1 to 100\n","You only have 5 chances")
for Guess_number in range(5):
    Guess_number = int(input(" Guess a number = "))
    if secret_number > Guess_number:
        print("You are too low!! Try again")
    elif secret_number < Guess_number:
        print("You are too high!! Try again")
    else:
        break
    
if Guess_number == secret_number:
                   print(" Congratulations!! You guessed right!!")
else:
    print(" Failed to guess...\n","Correct number is =",secret_number)
