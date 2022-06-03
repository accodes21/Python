import random
import string

print("WELCOME TO PASSWORD GENERATOR")

len = int(input("Enter the length of password:"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbol = string.punctuation

all = lower + upper + num + symbol

x = random.sample(all, len)

password = "".join(x)

print("Password:",password)

