import string
#Substitution cipher program that maps a phrase 1 to 1 to a key


#Setting variables for loop and alphabet/key
loop='yes'
alphabet='abcdefghijklmnopqrstuvwxyz'
key='qwertyuiopasdfghjklzxcvbnm'

#Introducing user to program
print("""Welcome to a substitution cipher program. The program may be used to either
encrypt or decrypt a phrase in the English alphabet.\n
You may either use the built-in alphabet and key, or provide an alphabet, a key, or both.\n""")
print("*letters will stay capitals, and punctuation will remain\n")

#Asking if the user wants to use their own alphabet
alphabet_choice=input("Type 'yes' to provide an alphabet: ")
print("")
if alphabet_choice.lower()=='yes':
    print("Do not include punctuation, and enter as lowercase\n")
    alphabet=input("Input: ")
    print("")

#Asking if user wants to use their own key
key_choice=input("Type 'yes' to provide a key: ")
print("")
if key_choice.lower()=='yes':
    print("Do not include punctuation, and enter as lowercase. \nAlso, do not use any characters not inside the alphabet.\n")
    key=input("Input: ")
    print("")

#Turning the alphabet and key into lists
alphabet=list(alphabet)
key=list(key)

#Temporarily making the lists a dictionary to remove duplicates, then reverting to list
key=list(dict.fromkeys(key))
alphabet=list(dict.fromkeys(alphabet))

#Removing spaces from lists
if ' ' in key:
    key.remove(' ')
if ' ' in alphabet:
    alphabet.remove(' ')
#key[:]=[x for x in key if x!=' ']     alternate way to remove all spaces

#Ensuring all letters in the alphabet and key are lowercase
alphabet[:]=[x.lower() if x.isupper() else x for x in alphabet]
key[:]=[x.lower() if x.isupper() else x for x in key]

#Removes punctuation from alphabet
alphabet[:]=[x for x in alphabet if ((x not in string.punctuation) and (not (x.isnumeric())))]

#removing characters not in the alphabet (capitals, punctuation, and numbers) from key
key[:]=[x for x in key if (x in alphabet)]

#Ensuring the key has all the letters of the alphabet
if len(alphabet)>len(key):
    start_point=alphabet.index(key[-1])     #ensuring that the program starts adding letters from the last letter of the key
    for letter in alphabet[start_point:]:
        if letter not in key:
            key.append(letter)
    for letter in alphabet[:start_point]:
        if letter not in key:
            key.append(letter)

#Creating uppercase copies of the key and alphabet
upper_alphabet=[]
upper_key=[]
for letter in alphabet:
    upper_alphabet.append(letter.upper())
for letter in key:
    upper_key.append(letter.upper())

#While loop to allow user to easily run the program multiple times
while loop.lower()=='yes':
    
    choice=input('Choose either "Encryption" or "Decryption": ')    #Allows user to decide function of program
    print("")


    #Main codeblock for encrypting statements
    if choice.lower()=="encryption":
        phrase=input("Enter the sentence to be encrypted: ")    #Takes the phrase to be encrypted
        encryption=''
        for letter in phrase:
            if letter in alphabet:                              #If statements determine if letter is lower, upper, or punctuation
                given_position=alphabet.index(letter)           #Finds the location of the given letter in the alphabet
                encryption+=key[given_position]                 #Uses determined location to lookup position in key and save to an output
            elif letter in upper_alphabet:
                given_position=upper_alphabet.index(letter)
                encryption+=upper_key[given_position]
            else:
                encryption+=letter
        print(encryption)
        loop=input("Type 'yes' to try again: ")                 #gives user option to re-run program



    #Main codeblock for decrypting statements    
    elif choice.lower()=="decryption":
        phrase=input("Enter the sentence to be decrypted: ")
        decryption=''
        for letter in phrase:
            if letter in key:
                given_position=key.index(letter)                #Finds the location of the given letter in the key
                decryption+=alphabet[given_position]            #Uses determined location to lookup position in alphabet and save to an output
            elif letter in upper_key:
                given_position=upper_key.index(letter)
                decryption+=upper_alphabet[given_position]
            else:
                decryption+=letter
        print(decryption)
        loop=input("Type 'yes' to try again: ")



        
    else:
        print('Neither "Encryption" nor "Decryption" was typed.')
        loop=input("Type 'yes' to try again: ")

