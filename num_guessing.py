import random
randNumber=random.randint(1,150)    # Generate a random number between 1 and 150
userGuess=None
guesses=0
uName=input("Enter your name:")

while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess:"))    # Get user's guess
    guesses+=1
    # Check if the guess is correct
    if(userGuess==randNumber):
        print("You Guessed it right!!")
    else:
        # Provide feedback based on the user's guess
        if(userGuess>randNumber):
            print("You Guessed it wrong ! Enter a smaller Number")
        else:
            print("You Guessed it wrong ! Enter a larger Number")

# Print the user's name and number of guesses
print(f"{uName} guessed a number in {guesses} guesses")

# Read the previous high score from the file
with open("highscore.txt","r") as f:
    highscore=int(f.read())

# Check if the current guess count is lower than the previous high score
if(guesses<highscore):
    print(uName,"have just broken this highscore!")

    # Update the high score in the file
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))
