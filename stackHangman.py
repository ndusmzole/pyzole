
def get_secret_word():
    while True:
        secret_word = input('Please enter a word to be guessed\nthat does not contain ? or whitespace:')
    if not ('?' in secret_word or ' ' in secret_word or secret_word == ''):
        return secret_word


def is_game_over(wrong_guess, secret_word, output, chars_guessed):
    if wrong_guess == 7:
        print('You failed to guess the secret word:', secret_word)
        return True
    for guess in secret_word:
        if guess in chars_guessed:
            output += guess
        else:
            output += '?'
    if not ('?' in output):
        print('You correctly guessed the secret word:', secret_word)
        return True
    else:
        return False


def display_hangman(wrong_guess):
    if wrong_guess == 1:
        print('\n |')
    elif wrong_guess == 2:
        print('\n |', '\n O')
    elif wrong_guess == 3:
        print('\n |', '\n O', '\n |')
    elif wrong_guess == 4:
        print('\n |', '\n O', '\n/|')
    elif wrong_guess == 5:
        print('\n |', '\n O', '\n/|\\')
    elif wrong_guess == 6:
        print('\n |', '\n O', '\n/|\\', '\n/')
    elif wrong_guess == 7:
        print('\n |', '\n O', '\n/|\\', '\n/', '\\')

def display_guess(secret_word, chars_guessed):
    output = ''

    for guess in secret_word:
        if guess in chars_guessed:
            output += guess
        else:
            output += '\nSo far you have guessed: '
            for guess in chars_guessed:
                output += guess + ","
                print(output.strip(","))

def get_guess(secret_word, chars_guessed):
    while True:

        guess_character = input('Please enter your next guess: ')
        if guess_character == '':
            print('You must enter a guess.')
            continue
        elif len(guess_character) > 1:
            print('You can only guess a single character.')
        elif guess_character in chars_guessed:
            print('You already guessed the character:', guess_character)
        else:
            return guess_character

def main():
    wrong_guess = 0
    chars_guessed = []
    secret_word = get_secret_word()
    output = ''

    while not is_game_over(wrong_guess, secret_word, output, chars_guessed):
        display_hangman(wrong_guess)
        display_guess(secret_word, chars_guessed)
        guess_character = get_guess(secret_word, chars_guessed)
        chars_guessed.append(guess_character)
        chars_guessed.sort()
        if not guess_character in secret_word:
            wrong_guess += 1
            return wrong_guess
            pass


if __name__ == '__main__':
    main()