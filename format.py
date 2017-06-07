'''
    example to demostrate pylint formatting and example with py3
    https://pylint.readthedocs.io/en/pylint-1.5/run.html
    .pylintrc file here was generated using the followin command line
    https://stackoverflow.com/questions/22448731/how-do-i-create-a-pylintrc-file
    pylint --generate-rcfile > .pylintrc

    Using Enum
    https://docs.python.org/3/library/enum.html
'''

import string
from enum import Enum


CHOICEMSG = "would you like to encode or decode?"
WORDMSG = "Please enter text"

class EncodeChoice(Enum):
    '''enum'''
    ENCODE = 1
    DECODE = 2

def parse_example():
    '''
    pylint example with 100 score after moving the script to a method.
    '''
    shift = 3
    choice = input(CHOICEMSG)
    word = (input(WORDMSG))
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ''
    if choice == EncodeChoice.ENCODE.name:
        for letter in word:
            if letter == ' ':
                encoded = encoded + ' '
            else:
                x = letters.index(letter) + shift
                encoded = encoded + letters[x]
    if choice == EncodeChoice.DECODE.name:
        for letter in word:
            if letter == ' ':
                encoded = encoded + ' '
            else:
                x = letters.index(letter) - shift
                encoded = encoded + letters[x]
    print(encoded)

parse_example()
