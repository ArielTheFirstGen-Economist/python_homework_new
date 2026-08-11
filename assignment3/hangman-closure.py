############### Task 4 ###############

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display_word = ""
        for char in secret_word:
            if char in guesses:
                display_word += char
            else:
                display_word += "_"
        print("\ntask 4")
        print(display_word)

        if "_" in display_word:
            return False            
        else:
            return True
    return hangman_closure

guess_word = input("Enter your guess:")
play_hangman = make_hangman(guess_word)

loss = False

while loss == False:

    guess = input("Input a letter:")

    loss = play_hangman(guess)

print("You win")
        
