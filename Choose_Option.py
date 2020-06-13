# The function is responsible for checking if user's input isn't blank

# The function checks and prints out output based on user input
def ask_user(question):
  
  
  
  valid = False
  while not valid:
    
    response = input(question)
  
    # Checks if the user's response is in the list 
    if response in encrypting :
      print('\nYou chose: Encryption')
      
      
      return response
    if response in decrypting:
      
      print('\nYou chose: Decryption')
      
      return response
    else:
      print('Invalid Input')

# List of possible user inputs
encrypting = ('en','encryption','encrypt')
decrypting = ('de','decryption','decrypt')


# Input that has a built in function from above
state = ''
question = ask_user('Do you want to: Encrypt or Decrypt your message?')
# If the 
while True: 
  # If user chose decrypting his message, then the program will
  # enquire about the key.
  if question in decrypting:
    question1 = input('Do you know they key? y/n')
    if question1 in ('yes','y','n','no'):
      if question1 in ('yes','y'):
        print('-- You chose decryption with a key --')
        break
      elif question1 in ('n','no'):
        print('** You chose decryption without a key **')
        break
    else:
      print('Try again, type yes or no')
  
  # If user chose encrypting his messahe, then the program wiil list 
  # 3 different options on how he can cipher his message.
  elif question in encrypting:
    question1 = input('\nHow would you like to encrypt your message?\n\n1. Using key of preference\n2. Randomly Generated Key\n3. Using Ciphered alphabet')
    if question1 in (str('1'),str('2'),str('3')):
      if question1 == str('3'):
        print('You chose to Encrypted alpahbet')
        break
      elif question1 == str('2'):
        print('You chose to use random key')
        break
      elif  question1 == str('1'):
        print('You chose to use your personal key')
        break
    else:
      print('\nInvalid Input, please pick the option from the list above')
