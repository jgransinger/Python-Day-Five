import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#-----  easy version
password = ""
for x in range(0,nr_letters):
    password += (random.choice(letters)) # i chose the below method for doing this, but this is simplified and correct

for x in range(0,nr_numbers):
    current = (random.choice(numbers))
    password += current

for x in range(0,nr_symbols):
    current = (random.choice(symbols))
    password += current

print(password)

#----------------------------------------------------

#hard version
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for x in range(0,nr_letters):
    current = (random.choice(letters))
    password += current

for x in range(0,nr_numbers):
    current = (random.choice(numbers))
    password += current

for x in range(0,nr_symbols):
    current = (random.choice(symbols))
    password += current

pw_to_list = [letters for letters in password] #convert string to list, don't fully understand this line, but works
random.shuffle(pw_to_list)
password = ''.join(pw_to_list)  #converts list back to string, i have no idea how it works, but it does

print(password)