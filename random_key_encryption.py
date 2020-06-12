# import random module allows variable to pick a random integer
# with .random.randint(range)
import random


# Function that checks if the input isn't blank. If the response is blank, it will
# warn the user to enter something
def check_text(question):
    valid = False
    while not valid:
        response = input(question)
        if response == '':
            print('Cannot be blank')
        else:
            return response


# Num_list turns user string into ASCII number which can be added/subtracted
# to make a new number
num_list = []
# Cipher text is a list that takes in Ascii number and turns it into a new character
cipher_text = []
# error message
error = 'Invalid Input'
# The key being chosen will be in the alphabetical range (1,26), which is the
# alphabetical range
keys = random.randint(1, 26)
# ask user for a text he wants to encrypt
ask = check_text('question: ')
# for every letter in the text, the program will use the formula below
# to encrpyt user message
# alphabet range normal
for i in range(len(ask)):
    coded = 0
    # cipher represents the letters in the text
    cipher = ask[i]
    # code represents the ASCII numbers of letters in the text
    code = ord(ask[i])
    # short sum adds the key to the code (ASCII), which results in the shift of characters
    short_sum = code + keys
    # If code is not in alphabet range, then the program will use
    # formula below:
    # code Responsible for keeping all the symbols the same.

    if code in range(0, ord('A')) or code in range(ord('{'), 128):
        coded = code
    # If code is in alphabet range but is using capital letters, then the program will use:
    elif code in range(65, 91):
        if short_sum <= ord('Z'):
            coded = short_sum
        if short_sum > ord('Z'):
            coded = code - 26 + keys
    # If code is
    elif code in range(ord('a'), ord('{')):
        if short_sum <= ord('z'):
            coded = short_sum
        if short_sum > ord('z'):
            coded = short_sum - 26

    cipher_text.append(chr(coded))

# Code that adds the ASCII and cesar ciphered text to the list
# Prints out the cesar ciphered user text.
print('Ciphered Text: ', ''.join(cipher_text))
# Random Key
print('Key: ', keys)




