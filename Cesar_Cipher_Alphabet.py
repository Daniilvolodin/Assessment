# Function that will check if the user entered a valid input and that it is no greater than 26

def num_check(question):
    valid = False
    while not valid:
        try:

            response = int(input(question))
            if response > 26:
                print('You can only shift 26 times')
            else:
                return response

        except ValueError:
            print('Invalid Input')


# 26 letter Alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

# Input asking the user to enter a key with a built-in num_check function
cesar_alphabet = num_check('Key - ')

# start variable splits the alphabet list and shows the letter that has been
# shifted .. times
# finish completes the alphabet by filling in the missing letters in order
start = alphabet[cesar_alphabet:]
finish = alphabet[0:cesar_alphabet]
# Is the final product of start and finish
alphabet1 = start + finish

print('Ciphered Alphabet: ', *alphabet1)