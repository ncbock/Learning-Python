# we will use the hashlib to encrypt a message that is imported as a file.
# the recipient of the message will be able to decrypt it using a key that only the message
# writter and the recipient know. 
#
# We will also import os to see if the file exist and decide whether the messahe should be 
# encrptyed and saved or decrypted and read.
#
# This is a shift cypher, but it is harder to decode because the shift of each character
# is based on the hash function created using the hashlib

import hashlib, os

# create a hash that we will use to encrypt/decrypt our message, input string is the key.
def createHash(s):
    myHash = hashlib.sha256(s.encode('utf-8')).hexdigest() 
    return myHash


# User to input the key that will be used to encrypt/decrypt our message
def getKey():   
    key = input("What is the key?\n\n")
    values = []
    for i in createHash(key):
        values.append(ord(i))
    return values

def encryptMessage(s):
    # Create the message file
    createFile = open(s,"w")
    values = getKey()
    lenHash = len(values)
    print("\nType your message\n")
    #Create the message
    while True:
        # Create a list of each character in the message
        userTypes = list(input())
        # Stop message taking
        if userTypes == list("I am done"):
            break
        # for each character in the message
        for i in range(len(userTypes)):
            # Change the character to its ASCII value
            userTypes[i] = ord(userTypes[i])
            # Change the ASCII value of each character to encrypt it. Values between 32 and 126
            # are easily displayed without encoding. i%lenHash is used to deal with message lines
            # which contain more characters than the length of the hash function.
            for j in range(values[i%lenHash]):
                if userTypes[i] == 126:
                    userTypes[i] = 32
                else:
                    userTypes[i] += 1
            # Change the encrypted ASCII value back to a character
            userTypes[i] = chr(userTypes[i])
        userTypes = "".join(userTypes)
        createFile.write(userTypes)
        createFile.write("\n")
        print("")
    createFile.close()

def readMessage(s):
    # Open the message file
    readFile = open(s,"r")
    values = getKey()
    lenHash = len(values)
    lines = readFile.readlines()
    for i in range(len(lines)):
        line = list(lines[i])
        # .pop() is used to eliminate the new line character created in the message function
        line.pop()
        for j in range(len(line)):
            line[j] = ord(line[j])
            for k in range(values[j%lenHash]):
                if line[j] == 32:
                    line[j] = 126
                else:
                    line[j] -= 1
            line[j] = chr(line[j])
        lines[i] = "".join(line)                     
        print(lines[i])


messageFile = input("Name the file of the message.\n\n")
fileExist = os.path.isfile(messageFile)

if fileExist == False:
    encryptMessage(messageFile)
else:
    readMessage(messageFile)   


