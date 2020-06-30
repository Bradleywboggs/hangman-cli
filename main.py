import getpass as gp

def main():
    # head = "    -     \n  /   \   \n |     |  \n  \   /   \n    -     "
    # upper_torso = "    |     \n    |     \n    |     "
    # right_arm = "----------"
    # print(head)
    # print(upper_torso)
    # print(right_arm)

    word = gp.getpass("Please put in a word: ")
    blanks = _get_blanks(word)

    # There are 9 guesses available - one for each body part to be drawn (eventually)
    guesses = 9
    winner = False
    guessed_letters = []
    # We know the game is over when we run out of guesses or we win the game
    #  until the game is over we'll keep guessing
    while guesses > 0 and winner is False:
        print_scoreboard(guesses, guessed_letters, blanks)
        guess = input("Please enter a guess: ")
        # If a single letter guess is wrong:
        if guess not in word:
            #  subtract 1 from the guesses count
            guesses = guesses - 1
            # Add a letter to the "guessed letters"
            guessed_letters.append(guess)
            # print a "Wrong" message
            print("\nWrong, baby rump kisser.!\n")
        # If a single letter guess is right:
        if guess in word:
            #  don't subtract from the guesses count
            #  receive "Correct" message
            print("\nCorrect!\n")
            #  replace the blank(s) with the guessed letter
            blanks = _fill_blanks_with_correct_letters(guess, blanks, word)

            if "_" not in blanks:
                winner = True
                print(str.join('', blanks))
                print("\n\nWinner Winner Chicken Dinner!!")

            
            


    
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
def print_scoreboard(number_of_guesses_remaining, guessed_letters, blanks):
    print(f"Number of guesses Remaining: {number_of_guesses_remaining}\n\nGuessed Letters:{guessed_letters}\n\n {str.join(' ',blanks)}")

def _get_blanks(word):
    blanks = []
    for letter in word:
        blanks.append('_')
    return blanks

if __name__ == "__main__":
     main()


    
