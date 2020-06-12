# Number checking function.
# Checks if the user entered a valid number.
# Function will warn the user if: input is not a number, input is greater than 26 or if input is less than 1
def check_num(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response > 26:
                print('Cannot be more than 26')
            elif response < 1:
                print('Cannot be less than 1')
            else:
                return response
        except ValueError:
            print('The key has to be an integer')

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


coded = 0
alphabet_num = 26
cipher_text = []
# keys is an input that asks user for the key in the range 1-26
# if the key equals to zero or a number above 26, the input will print a message
# telling that the input is invalid.
keys = check_num('Key: ')
ask= check_text('Encrypted text: ')

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
print('Message: '+''.join(cipher_text))



