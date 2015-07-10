__author__ = 'silverbaq'

from random import randint

class SocketGames:
    gamelist = ["Guess a number"]

    def getGameMenu(self):
        return "Select a game:\r\n" \
               "1: %s\r\n" \
               "2: --Comming--\r\n" % self.gamelist[0]

    def choiceGame(self, gamenumber):
        if gamenumber == 1:
            return GuessNumber()
        elif gamenumber == 2:
            return "Not implementet yet\r\n"
        else:
            return "try agian\r\n"



class GuessNumber:
    guesses = 0

    def __init__(self):
        self.number = randint(0,100)
        print "Guess a number game has started"

    def guess(self, myGuess):
        if myGuess == self.number:
            self.guesses = self.guesses + 1
            return "You are correct! You have used %d tryes.\nTo try agian, type 'Restart'\n" % self.guesses
        elif myGuess < self.number:
            self.guesses = self.guesses + 1
            return "%d is too low - you have used %d guesses.\n" % (myGuess, self.guesses)
        elif myGuess > self.number:
            self.guesses = self.guesses + 1
            return "%d is too high - you have used %d guesses.\n" % (myGuess, self.guesses)

    def newGame(self):
        self.guesses = 0
        self.number = randint(0,100)
        return "Guess a number between 0 - 100\n"