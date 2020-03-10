# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "Introduction/Week3/Hangman/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = 0
    for let in secretWord:
        if let in lettersGuessed:
            guessed += 1
    if guessed == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    outstring = ''
    for let in secretWord:
        if let in lettersGuessed:
            outstring += str(let)
        else:
            outstring += '_ '
    return outstring


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    outstring = string.ascii_lowercase
    for let in string.ascii_lowercase:
        if let in lettersGuessed:
            outstring = outstring.replace(let, '')
    return outstring


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesMade = 0
    lettersGuessed = []
    guesses = 8
    print("Welcome to the game, Hangman!")
    wordlen = len(secretWord)
    print('I am thinking of a word that is '+str(wordlen)+' letters long.')
    print("-------------")
    while True:
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was " +
                  str(secretWord)+".")
            break
        print('You have '+str(guesses)+' guesses left.')
        print('Available letters: '+getAvailableLetters(lettersGuessed))
        userlet = input('Please guess a letter: ')
        if userlet in lettersGuessed:
            print("Oops! You've already guessed that letter: " +
                  str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")

        elif userlet in secretWord:
            lettersGuessed.append(userlet)
            word = getGuessedWord(secretWord, lettersGuessed)
            print('Good guess: '+str(word))
            print("------------")
        else:
            lettersGuessed.append(userlet)
            print("Oops! That letter is not in my word: " +
                  str(getGuessedWord(secretWord, lettersGuessed)))
            guesses -= 1
            print("------------")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
