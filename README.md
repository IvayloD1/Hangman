The game starts with a menu where a player can choose to either play or exit.

Print "Type "play" to play the game, "exit" to quit:" and show this message again if the player inputs something else. If the user chooses to play, the game begins.
The word should be selected from the list: 'python', 'java', 'kotlin', 'javascript'. 

The player starts the game with 8 "lives", which is to say, our player can input a wrong letter 8 times.

Print "That letter does not appear in the word" and reduce the number of remaining attempts if the word selected by the program doesn't contain this letter. If the user enters the same letter twice, then the program should output "You've already guessed this letter". This message should also be printed if the user inputs a letter that doesn't appear in the word. The number of attempts shouldn't be decreased in this case. Also, you should check to make sure the player entered an English lowercase letter. If not, the program should print "Please enter a lowercase English letter". You should also check if the player entered exactly one letter. If not, the program should print "You should input a single letter". Remember that zero is also not one!Note that none of these three errors should reduce the number of remaining attempts.



Test:
H A N G M A N

Type "play" to play the game, "exit" to quit: > play

    ----------

Input a letter: > a

-a-a------

Input a letter: > i

-a-a---i--

Input a letter: > o

That letter doesn't appear in the word

-a-a---i--

Input a letter: > o

You've already guessed this letter

-a-a---i--

Input a letter: > p

-a-a---ip-

Input a letter: > p

You've already guessed this letter

-a-a---ip-

Input a letter: > h

That letter doesn't appear in the word

-a-a---ip-

Input a letter: > k

That letter doesn't appear in the word

-a-a---ip-

Input a letter: > a

You've already guessed this letter

-a-a---ip-

Input a letter: > z

That letter doesn't appear in the word

-a-a---ipt

Input a letter: > t

-a-a---ipt

Input a letter: > x

That letter doesn't appear in the word

-a-a---ipt

Input a letter: > b

That letter doesn't appear in the word

-a-a---ipt

Input a letter: > d

That letter doesn't appear in the word

-a-a---ipt

Input a letter: > w

That letter doesn't appear in the word

You lost!

Type "play" to play the game, "exit" to quit: > exit 
