import string
from random import choice, sample

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)


numberofletters = int(input("How many letters would you like your password to be? "))
numberofsymbols = int(input("How many symbols would you like your password to be? "))
numberofnumbers = int(input("How many numbers would you like your password to be? "))


password = ""

for _ in range(numberofletters):
    password += choice(letters)

for _ in range(numberofsymbols):
    password += choice(symbols)

for _ in range(numberofnumbers):
    password += choice(numbers)

password = ''.join(sample(password, len(password)))

print("Generated Password:", password)

