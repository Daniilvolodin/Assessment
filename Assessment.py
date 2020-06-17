# import random is a module that allows a variable to have different value
import random
# The function is responsible for checking if user's input isn't blank
# The function warns user if his response was blank
# The function checks and prints out output based on user input
def check_text(question):
    # loop within a function
    valid = False
    while not valid:
        response = input(question)
        if response == '':
            print('Cannot be blank')
        else:
            return response

# Number checking function.
# Checks if the user entered a valid number.
# Function will warn the user if: input is not a number, input is greater than 26 or if input is less than 1
def num_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response < 1:
                print('Cannot be lower than 1')
            elif response > 26:
                print('Cannot be higher than 26')
            else:
                return response
        except ValueError:
            print(error)

# String checking function.
# Checks if user input is in 'encrypted' or 'decrypted' list.
# sends user message that warns about the input being invalid.
def ask_user(question):
    valid = False
    while not valid:

        response = input(question)
        
        if response in encrypted:
            print('You chose: Encryption')
            return response
        if response in decrypted:
            print('You chose: Decryption')
            return response
        else:
            print(error)

# List that is going to store the ciphered letters of the user text.
cipher_text = []
# Variables that store arrays of possible user inputs
# Make shortcuts on words like:encryption,decryption and yes or no.
encrypted = ('en', 'encryption', 'encrypt')
decrypted = ('de', 'decryption', 'decrypt')
agree = ('y', 'n', 'yes', 'no')

# error message
error = 'Invalid input'

# variable that stores the key
keys = 1

# variable that indicates the key for the text.
time = 1
choice = ''
ask1=''
options = ''
ask1 = ''
instructions = ''
yes_no = ('n','no','yes','y')
alphabet1 = 'abcdefghijklmnopqrstuvwxyz'

# Section of code responsible for making sure the user knows what the 
# program is about and how it works.
while instructions not in yes_no:
  instructions = input('Do You Know Caesar Cipher Encryption? Yes/No: ')
  if instructions in ('y','yes'):
    pass
  # If user does not know what caesar cipher is, the program will 
  # print out the description of caesar cipher
  elif instructions in ('n','no'):
    print('\n** Caesar Cipher **\n')
    print('-- Caesar Cipher is used by replacing each plaintext letter \nwith a different one a fixed number of places down the alphabet. --\n')
  elif instructions not in yes_no:
    print('\nPlease type: Yes / No')
  

# Asks if user wants to encrypt or decrypt his message.
ask = ask_user('\nWould you like to: Encrypt or Decrypt your message? ')

# if user input is the same as one of the strings in 'encrypted' variable
# the program will display the encryption options that user can choose from 
if ask in encrypted:
    choice = 'encrypt'
    options = '\n1. Key of your choice\n2. Randomly generated key\n3. Ciphered Alphabet'

# if user input is the same as one of the strings in 'decrypted' variable
# the program will display the decryption options that user can choose from 
elif ask in decrypted:
    choice = 'decrypt'
    options = '\nDo you know the key? yes/no: '

# Options of encryption/decryption
print('\nHow would you like to {} your message?'.format(choice))

# If user picked 'Encrypting' and his input on encryption options is invalid then
# the program will warn the user with a message, telling him to pick an option.
if choice == 'encrypt':
    while ask1 not in ('1', '2','3'):
        ask1 = input(options)
        if ask1 not in ('1', '2','3'):
            print('Please pick one of the options above by typing 1, 2 or 3')

# If user picked 'Decrypting' and his input on decryption options is invalid then
# the program will warn the user with a message, telling him to choose from list of options.
elif choice == 'decrypt':
    while ask1 not in agree:
        ask1 = input(options)

        if ask1 not in agree:
            print('Please specify: Yes/No')

# Options of Encryption option 1 and Decryption option 'yes' have the same coding
# style, that is why they have the same key input.
# keys input asks for the key that the user has to enter.
if ask1 in (str('1'),str('3')) or ask1 in ('y','yes'):
    keys = num_check('\nWhat is the key? ')

# If the user picked Encryption option 2, the key will be randomly generated by the
# program. The program will choose random integer from an alpabetical range (Limit of keys in cesar cipher)
if ask1 == str('2'):
    keys = random.randint(1, 26)

# Program asks for input (Text) that user wants to encrypt or decrypt .
# The input variable uses blank checking function which means that
# the program will send user a message, saying that the input cannot be blank
if ask1 in (str('1'),str('2')) or ask1 in yes_no:
  ask_text = check_text('\nEnter your Text: ')

# if the option input for encryption is 3, the program will print the cesar cipher alphabet
# based on user's key.
if ask1 == str('3'):
  for i in range(1):
    print('\nYour Ciphered Alphabet Is:',alphabet1[keys:]+alphabet1[:keys])

# If the option input of decryption is not 'n' or 'no' then the program will
# go over the code that is meant to work for encryption option 1 and 2 or decryption answer 'yes'
elif ask1 == 'y' or ask1 == 'yes' :
    # The program will shift every letter in user text by using for i in v loop.
    for i in range(len(ask_text)):
            # Variables that work within a function
            
            # coded is a variable that will be used to find the
            # character that has been shifted xKey times. 
            coded = 0
            # Code is a variable that turns each character in user input
            # into ASCII number, this allows me to add numbers to ASCII to make 
            # new characters
            code = ord(ask_text[i])
            
            # short_sum is a variable that shows the overall number (ASCII + KEYS)
            short_sum = code + keys

            # If the ASCII user text character is not a letter, the program will leave
            # the character as it is.
            if code <123:
              coded=code
            if code in range(1, ord('A')):
                coded = code
            
            # if the ASCII user text character is a capital letter, the program will
            # use the formula below to calculate the shift (x) letter, key times.
            elif code in range(ord('A'), ord('Z')+1):
                
                # If ASCII letter + key is less than ASCII 'Z'
                # the program will add ASCII letter with key number
                if short_sum <= ord('Z'):
                    coded = short_sum
                
                # If ASCII letter + key is greater than ASCII 'Z',
                # The program will take away 26 (letters) from short_sum
                # to make the final ord(letter)
                if short_sum > ord('Z'):
                    coded = code - 26 + keys
            # If ASCII letter + keys is greater than lower case ord('z')
            # the program will add ord(letter) with key number
            elif short_sum <= ord('z'):
                coded = short_sum

            
            # If ASCII letter + keys is lower than lower case ord('z')
            # the program will add ord(letter) with key number and subtract it by 26 (letters
            # in the alphabet)
            elif short_sum > ord('z'):
                coded = short_sum - 26

            # The final ASCII letter will then be added to a list
            # where it will turn ASCII letter into its average state.   
            cipher_text.append(chr(coded))
    
    # When the program is done looping through the text, it will print the 
    # final result.
    print('Your {}ed text is: '.format(choice)+''.join(cipher_text))
    
# If the option for decryption was - 'n' or 'no', the program 
# will try and find the key that decrypts your message.
elif ask1 == 'n' or ask1 == 'no':
    print('\nPossible texts with different keys:\n')
    
    # While the program haven't yet tested every text outcome 
    # for every key, the program will use the following code:
    while keys < 27:
        
        # same code from lines:  139-177
        for i in range(len(ask_text)):
            coded = 0
            code = ord(ask_text[i])
            short_sum = code + keys
            if code <123:
              coded=code
            if code in range(1, ord('A')):
                coded = code
            elif code in range(ord('A'), ord('Z')+1):
                if short_sum <= ord('Z'):
                    coded = short_sum
                if short_sum > ord('Z'):
                    coded = code - 26 + keys
            elif short_sum <= ord('z'):
                coded = short_sum
            elif short_sum > ord('z'):
                coded = short_sum - 26
            cipher_text.append(chr(coded))
            
            # If the amount of characters in the list is equal to 
            # amount of characters in the text, the list will join 
            # the characters to make the ciphered message 
            if len(cipher_text) == len(ask_text):
                code_text = ''.join(cipher_text)
                
                # After the program is done ciphering text for a key, it will
                # clear itself to make the room for the next key
                cipher_text.clear()
                
                # prints out different variations of ciphered text that uses the
                # range of 1 to 26  keys
                print('key-'+str(time)+' '+code_text)
                keys += 1
        time += 1
