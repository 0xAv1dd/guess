import random 

times = input("How many games would you like to play ?: ")
print("You would like " + times + " games.") 

game = 0 
guesses = 0 
x =random.randint(0,25)

try:
    times = int(times)
    while times > game:
        guess = input("Guess a number between 0 and 25: ")
        guess_y = int(guess) 
        print("You guessed " + str(guess_y))
        if guess_y == x :
            print (str(x) + " You guessed it ! ")
            game += 1 
            print("You guessed it in " + str(guesses + 1 ) + " guesses")
            guesses = 0 
            x = random.randint(0,25)
        elif guess_y > x:
            print("incorrect, the number is lower")
            guesses += 1 
        elif guess_y < x:
            print("incorrect, the number is higher")
            guesses += 1 
            
            
finally:
    print("Thank you for playing")
 

