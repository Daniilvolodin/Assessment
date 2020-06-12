# The function is responsible for checking if user's input isn't blank
# The function warns user if his response was blank
# The function checks and prints out output based on user input
def ask_user(question):
    valid = False
    while not valid:

        response = input(question)
        if response == '':
            print('Input cannot be blank')
        # Checks if the user's response is in the list
        if response in encrypting:
            print('You chose: Encryption')

            return response
        if response in decrypting:

            print('You chose: Decryption')

            return response
        else:
            print('Invalid Input')


encrypting = ('en', 'encryption', 'encrypt')
decrypting = ('de', 'decryption', 'decrypt')

# Input that has a built in function from above
state = ''
question = ask_user('Encrypt or Decrypt?')
if question in decrypting:
    state = 'decrypted'
elif question in encrypting:
    state = 'encrypted'

ask = input('Enter your {} text: '.format(state))