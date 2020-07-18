import getpass as gp
import os

# clear = lambda: os.system('clear')
def main():
    # head = "    -     \n  /   \   \n |     |  \n  \   /   \n    -     "
    # upper_torso = "    |     \n    |     \n    |     "
    # right_arm = "----------"
    # print(head)
    # print(upper_torso)
    # print(right_arm)
    clear()
    word = gp.getpass("Please put in a word: ")
    blanks = _get_blanks(word)

    # There are 9 guesses available - one for each body part to be drawn (eventually)
    remaining_guesses = 9
    winner = False
    guessed_letters = []
    message = ""
    # We know the game is over when we run out of guesses or we win the game
    #  until the game is over we'll keep guessing
    while remaining_guesses > 0 and winner is False:
        print_scoreboard(remaining_guesses, guessed_letters, blanks, message)
        guess = input("Please enter a guess: ")
        # If a single letter guess is wrong:
        if guess not in word:
            #  subtract 1 from the guesses count
            remaining_guesses = remaining_guesses - 1
            # Add a letter to the "guessed letters"
            guessed_letters.append(guess)
            # print a "Wrong" message
            message = "\nWrong, baby rump kisser!\n"

            if remaining_guesses is 0:
                clear()
                print(f"You lost. The word was {word}.")
        # If a single letter guess is right:
        if guess in word:
            #  don't subtract from the guesses count
            #  receive "Correct" message
            message = "\nCorrect!\n"
            #  replace the blank(s) with the guessed letter
            blanks = _fill_blanks_with_correct_letters(guess, blanks, word)

            if "_" not in blanks:
                winner = True
                clear()
                print(str.join('', blanks))
                print("\n\nWinner Winner Chicken Dinner!!")

            
            
def clear():
     os.system('clear')
    
def _fill_blanks_with_correct_letters(guessed_letter, blanks, word):
    # Find the position(s) of the correct guessed letter in the word
    letter_positions = []
    for position in range(len(word)):
        if word[position] == guessed_letter:
            letter_positions.append(position)
    for position in letter_positions:
        blanks[position] = guessed_letter
    return blanks

    # Replace the blank(s) in the same position(s) as the letter in the word
def print_scoreboard(number_of_guesses_remaining, guessed_letters, blanks, message):
    clear()
    print(f"Number of guesses Remaining: {number_of_guesses_remaining}\n\nGuessed Letters:{guessed_letters}\n\n {str.join(' ',blanks)}\n\n {message}")

def _get_blanks(word):
    blanks = []
    for letter in word:
        blanks.append('_')
    return blanks

if __name__ == "__main__":
     main()


    
