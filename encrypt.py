import random

num = random.random()

def encrypt(sttr, enkey=str(num)):
    return enkey.join(sttr)

text = input("Enter any text: ")
print(encrypt(text))
