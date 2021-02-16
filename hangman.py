import random


def run():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    hidden_word = ["-" for _ in range(len(word))]  # replacing all unsolved letters with "-"
    used_letters = []
    lives = 8

    while True:
        print(''.join(hidden_word))
        letter = input("Input a letter:")
        if len(letter) == 1:  # check if input is single letter
            if letter.islower():  # check if letter is lowercase
                if letter not in word and letter not in used_letters:  # if selected letter is incorrect and was not selected yet
                    lives -= 1
                    if lives == 0:
                        print("That letter doesn't appear in the word\nYou lost!")
                        break
                    else:
                        print("That letter doesn't appear in the word\n")
                elif letter in used_letters:
                    print("You've already guessed this letter\n")
                else:  # if selected letter is correct
                    count = 0  # counter to get letter index in the word
                    for i in word:  # iterate through word to get letter index and replace "-" in hidden_word by the  guessed letter
                        if i == letter:
                            hidden_word[count] = letter
                        count += 1
                    print()
                used_letters.append(letter)  # add letter to used letters list
            else:
                print("Please enter a lowercase English letter\n")
        else:
            print("You should input a single letter\n")
        if "-" not in hidden_word:  # break loop if there are no more letters to guess, print win message
            print(f'{word}\nYou guessed the word!\nYou survived!\n')
            select()
            break


def select():
    return input('Type "play" to play the game, "exit" to quit:\n')


print("H A N G M A N\n")

# loop until "play" is not selected or "exit" - to quit is chosen
while True:
    if select() == "play":
        run()
    elif select() == "exit":
        quit()
    else:
        continue
