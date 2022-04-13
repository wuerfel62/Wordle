import random
from termcolor.termcolor import colored
import os

class wordle:
    def __init__(self) -> None:
        self.wordList = open('wordListDE copy.txt', 'r').read().split()

        self.errMsg = ""

        self.guessedWords = []
        self.guessCount = 0
        self.wordToGuess = self.wordList[random.randint(0, len(self.wordList))]
        self.wordToGuessList = [char for char in self.wordToGuess]

    def main(self):
        while not self.has_lost():
            self.check_word(self.get_user_input())
        if self.has_lost():
            print(self.wordToGuess)

    def get_user_input(self):
        userInput = ""
        while(len(userInput) != 5):
            self.print_guessed_words()
            self.errMsg="word hat keine 5 buchstaben"
            userInput = input()
            
        return userInput

    def check_word(self, word):
        if(word == self.wordToGuess):
            self.print_guessed_words()
            print(colored(word, 'green'))
            exit()
        elif word not in self.wordList:
            self.errMsg = word + " is not in the Wordlist"
        else:
            self.guessedWords.append(word)
            self.guessCount += 1
            self.print_guessed_words()

    def has_lost(self):
        if self.guessCount == 6:
            return True
        else:
            return False

    def print_guessed_words(self):
        os.system('cls')
        if not self.errMsg == "":
            print(colored(self.errMsg, 'red'), sep=" ")
        for gw in self.guessedWords:
            tempStrList = [char for char in gw]
            for i in range (0,5):
                if(tempStrList[i] == self.wordToGuessList[i]):
                    print(colored(tempStrList[i], 'green'), end="")
                elif(tempStrList[i] in self.wordToGuessList):
                    print(colored(tempStrList[i], 'yellow'), end="")
                else:
                    print(tempStrList[i], end="")
            print("")
        self.errMsg = ""


if __name__ == "__main__":
    game = wordle()
    game.main()