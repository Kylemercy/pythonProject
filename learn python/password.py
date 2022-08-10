import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the P4"
      "5"
      "4"
      "yPassword Generator!")
print('Your password has 10 characters')

length = 10
password_list = []
all_char = numbers + letters + symbols
for i in range(1, length + 1):
    password_list.append(random.choice(all_char))
print(password_list)
random.shuffle(password_list)
password = ' '
for char in password_list:
    password += char

print('Your password is : ', password)
