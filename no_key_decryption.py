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


# Cipher text is a list that takes in Ascii number and turns it into a new character
cipher_text = []
# error message
error = 'Invalid Input'

# Variables
coded = 0
# Keys
keys = 1
# Times
times = 1
# ask user for a text he wants to decrypt
ask = check_text('question: ')
# While 26 is higher or equal to keys, the program will continue to loop
while keys <= 26:
    # for every letter in the text, the program will use the formula below
    # to try and decrypt user message

    for x in range(len(ask)):
        # code represents ASCII characters in text
        code = ord(ask[x])
        if code in range(ord('a'), ord('z')):
            if keys + code <= ord('z'):
                coded = code + keys
            elif keys + code > ord('z'):
                coded = code - 26 + keys
        if code in range(ord('A'), ord('Z')):
            if keys + code <= ord('Z'):
                coded = code + keys
            elif keys + code > ord('Z'):
                coded = code - 26 + keys

        # If code is not in alphabet range, then the program will
        # ignore the formula and use average ASCII character instead.

        if code in range(0, ord('A')) or code in range(ord('{'), 128):
            coded = code
        cipher_text.append(chr(coded))

        # If the number of characters in the list is equal to the number of characters in
        # user text, the program will join the characters in the list to make a new string
        # the program will then clear the list to make space for a new set of characters.
        if len(cipher_text) == len(ask):
            print('Key- {}: '.format(times) + ''.join(cipher_text))
            cipher_text.clear()
    # Adds 1 to keys to make a new key
    keys += 1
    # adds 1 to number of times the program will print different ciphers of text.
    times += 1