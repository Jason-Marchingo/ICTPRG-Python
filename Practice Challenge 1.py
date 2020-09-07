# Number Guessing Game // Practice Challenge #1
# Written and Coded By: Jason Marchingo
# Date: 31.08.20

# Create a number guessing game that
# asks the user for a number between 1 and 25
# tells the user if their guess is too high, or too low
# tells the user if their guess is right or if they failed with too many guesses
# and lists the users number of attempts and numbers guessed

# The user enters their guess
numberGuess = -1
# This is how many guesses the user has taken
guessCount = 0
# User maximum attempts
attempts = 7
# This is the hardcoded correct guess. This number can be changed to anything
# between 1 and 25 and the program will run
correctNumber = 23
# Lists all numbers entered / guessed by the user
guessedNumbers = []

# If the user answers their guess and it is not correct or equal to the correct number and is less than 
# their maximum guess count of 7 it will continue to ask the user to submit a guess.
while numberGuess != correctNumber and guessCount < 7:
        numberGuess = int(input("Guess a number between 1 and 25: "))
        # adds user guess to the list
        guessedNumbers.append(numberGuess)
        # tallies user guesses (+1)
        guessCount += 1
        # if the number is less than the correct number, ask the user to resubmit guess
        if numberGuess < correctNumber:
            print("Try again! Guess a number higher than", numberGuess)
            print("You have " + (str(attempts - guessCount)) + " attempts left")
        # if the number is greater than the correct number, ask the user to resubmit guess
        elif numberGuess > correctNumber:
            print("Try again! Guess a number lower than", numberGuess)
            print("You have " + (str(attempts - guessCount)) + " attempts left")
        # if the user guesses the correct number, congratulate them, tell them how many guesses it took
        # as well as what numbers they guessed
        elif numberGuess == correctNumber:
            print("You guessed the right number", numberGuess) 
            print("It took you", guessCount,"guesses!")
            print("Your guesses were", guessedNumbers)

# If the user fails the game / takes too many guesses, fail them and tell them what the correct number is, and list their guesses
if guessCount >= 7 and numberGuess != correctNumber:
    print("You failed! You took too many guesses! The correct number is", correctNumber)
    print("Your guesses were", guessedNumbers)

     #elif numberGuess > correctNumber or numberGuess == 0: 
             #print("This is outside the range! Pay attention!")
             #print("You have " + (str(attempts - guessCount)) + " attempts left")