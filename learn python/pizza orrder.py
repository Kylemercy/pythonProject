print('WELCOME TO PIZZA DELIVERIES')
size = input('what size of pizza do you want? S,M,L \n ').upper()
add_pepperoni = input('Do you want pepperoni ? y or n ').upper()
extra_cheese = input('Do you want extra chesse? y or n').upper()
bill = 0
if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
        print(f'your total bill for small pizza with pepperoni is ${bill}')
    else:
        print(f'your total bill for small pizza without pepperoni is ${bill}')
    if extra_cheese