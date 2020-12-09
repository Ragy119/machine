
from random import randint
Actual = randint(0,100) 
#print(Actual)

print('Range here from 0 to 100')
print('Try to guess the right number')


guesses = []
old_diff = 0
old_Guess = 0
while(1):
    # Take the input
    Guess= int(input('Enter your guess: '))
    guesses.append(Guess)
    
    # checking the boundries
    if (Guess > 100 or Guess < 0):
        print("Wrong boundry")
        continue
    
    # check right or wrong (close or far)
    if  Actual == Guess :
        # if right then print something
        print('Right Number')
        print("you took {} times to get the right answer".format(len(guesses)))
        break
    else:
        new_diff = abs(Guess - Actual)
        if  new_diff<old_diff :
            print(' you are closer to target ')
        else:
            print(' you are far from the target ')
        old_diff = new_diff
        old_Guess = Guess

