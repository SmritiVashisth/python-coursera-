# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
secret_number = 0
guessed_num = 0
number_of_guesses = 0

# helper function to start and restart the game
def new_game():
    print "new game begins"
    global secret_number, count
    global number_of_guesses
    global total_number
    number_of_guesses = 7
    secret_number = random.randrange(0,100)

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    global number_of_guesses
    number_of_guesses = 7
    secret_number = random.randrange(0,100)
    print "Game restarted with range 100"

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number
    global number_of_guesses
    number_of_guesses = 10
    secret_number = random.randrange(0,1000)
    print "Game restarted with range 1000"
    
def input_guess(guess):
    global secret_number
    global guessed_num
    global number_of_guesses
    guessed_num = int(guess)
    number_of_guesses = number_of_guesses - 1
    if(number_of_guesses > 0):
        if(guessed_num == secret_number):
            print "the number guessed is", guessed_num
            print "The number guessed is correct!"
            new_game()
        elif(guessed_num > secret_number):
            print "the number guessed is", guessed_num
            print "lower!"
        else:
            print "the number guessed is", guessed_num
            print "higher!"
        print "number of guesses remaining is", number_of_guesses
        print
    else:
        if(guessed_num == secret_number):
            print "the number guessed is", guessed_num
            print "The number guessed is correct!"
        else:
            print "you are out of guesses! you lose!!"
            print "The number was ", secret_number
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_input("Enter number", input_guess, 100)
frame.add_button("Range100", range100, 100)
frame.add_button("Range1000", range1000, 100)


# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
