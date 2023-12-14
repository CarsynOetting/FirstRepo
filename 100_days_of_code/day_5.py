import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

tot_letter = ''
tot_symbol = ''
tot_number = ''
password = []
finalpw = ''

for letter in letters:
    if len(tot_letter) < nr_letters:
        tot_letter = tot_letter + (letters[random.randint(0,(len(letters) - 1))])
password += tot_letter

for symbol in symbols:
    if len(tot_symbol) < nr_symbols:
        tot_symbol = tot_symbol + (symbols[random.randint(0,(len(symbols) - 1))])
password += tot_symbol

for number in numbers:
    if len(tot_number) < nr_numbers:
        tot_number = tot_number + (numbers[random.randint(0,(len(numbers) - 1))])
password += tot_number

print(password)
random.shuffle(password)

for char in password:
    finalpw += char

print(finalpw)
