from configparser import RawConfigParser
import string
import random

passwordChars = []
randomLetter = random.choice(string.ascii_letters)
specialChars = ["@", "#", "$", "!", "£", "?", "%", "&", "-", "_"]

#this function generates 5 random letters 3 random numbers and 2 special characters
def getPasswordChars():
    for i in range(5):
        passwordChars.append(random.choice(string.ascii_letters))
    
    for i in range(3):
        passwordChars.append(random.randint(0, 9))
    
    for i in range(2):
        passwordChars.append(specialChars[random.randint(0, len(specialChars) - 1)])

#this function takes all the random characters from getPasswordChars() and mixes the order and returns the final password
def makePassword():
    password = ""
    random.shuffle(passwordChars)
    for i in passwordChars:
        password = password + str(i)

    return password