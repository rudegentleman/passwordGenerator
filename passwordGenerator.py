import random
# Sample space for letters, numbers, words and special characters
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sampleWords = ['Kenya', 'Nigeria', 'Rwanda', 'Uganda', 'Manchester', 'Burundi', 'South Sudan', 'England',
'Arsenal', 'London', 'Chelsea', 'Tanzania', 'Ethiopia', 'Sudan', 'Egypt', 'Democratic Republic of Congo', 'Malawi', 
'South Africa', 'United States of America']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(',')', ',', '{', '}', '-', '+', '_',
 ':', '?', '/', '>', '<', '~', '[', ']', '|']

# Get user input from user
numLetters = int(input('How many letters should be in your password?: '))
wordInput = int(input('How many words should be in your password?: '))
charInput = int(input('How many special characters should be in your password?: '))
numInput = int(input('How many numbers should be in your password?: '))

# Based on user input, generate password from available sample dictionaries
def passwordGen(num_Letters, word_Input, char_Input, num_Input):
    password = ''
    if(num_Letters > 0):
        for let in range(0, num_Letters):
            password = password + random.choice(letters)

    if(word_Input > 0):
        for i in range(0, word_Input):
            password = password + str(random.choice(sampleWords))

    if(char_Input > 0):
        for i in range(0, char_Input):
            password = password + str(random.choice(specialCharacters))

    if(num_Input > 0):
        for i in range(0, num_Input):
            password = password + str(random.choice(numbers))
        print('This is the password generated from your entries: ' + password)
    # To generate a 16 byte password, check if user didn't enter all zero values
    if(len(password) <= 0):
        print('Password should contain at least one word, a special character, a letters and/or a number.')
    else:
        # Generate 16byte password from the password generated based on user input
        pazz = ''
        while(len(pazz) <16):
            pazz = pazz + random.choice(password)
        # Print final password
        print('This is your final password: '+ pazz)

# Run the program
passwordGen(numLetters, wordInput, charInput, numInput)
