# generates a random password
# 2 uppercase letters
# 2 lowercase letters
# 2 digits
# 2 symbols


import random

def randUppercase() :
    return chr(random.randint(65, 90))

def randLowercase() :
    return chr(random.randint(97, 122))

def randDigit() :
    return chr(random.randint(48, 57))

def randSymbol() :
    return chr(random.randint(33, 47))

def shuffle(input) :
    tempList = list(input)
    random.shuffle(tempList)
    return ''.join(tempList)

password = randUppercase() + randUppercase() + randLowercase() + randLowercase() + randDigit() + randDigit() + randSymbol() + randSymbol()
password = shuffle(password)

print(password)