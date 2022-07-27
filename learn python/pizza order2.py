print('WELCOME TO PIZZA DELIVERIES')
size = input('what size of pizza do you want? S,M,L \n ').upper()
add_pepperoni = input('Do you want pepperoni ? y or n ').upper()
extra_cheese = input('Do you want extra cheese? y or n').upper()

bill = 0
if size == 'S':
    bill += 15
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        bill += 2
        bill += 1
        print(f'your total bill of small pizza with pepperoni and extra cheese is ${bill}')
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        bill += 2
        print(f'your total bill of small pizza with pepperoni but without extra cheese is ${bill}')
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        bill += 1
        print(f'your total bill of small pizza without pepperoni but with extra cheese is ${bill}')
    elif add_pepperoni == 'N' and extra_cheese == 'N':
        print(f'your total bill of small pizza without pepperoni and extra cheese is ${bill}')
if size == 'M':
    bill += 20
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        bill += 3
        bill += 1
        print(f'your total bill of medium pizza with pepperoni and extra cheese is ${bill}')
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        bill += 3
        print(f'your total bill of medium   pizza with pepperoni but without extra cheese is ${bill}')
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        bill += 1
        print(f'your total bill of medium  pizza without pepperoni but with extra cheese is ${bill}')
    elif add_pepperoni == 'N' and extra_cheese == 'N':
        print(f'your total bill of medium  pizza without pepperoni and extra cheese is ${bill}')
if size == 'L':
    bill += 25
    if add_pepperoni == 'Y' and extra_cheese == 'Y':
        bill += 3
        bill += 1
        print(f'your total bill of large pizza with pepperoni and extra cheese is ${bill}')
    elif add_pepperoni == 'Y' and extra_cheese == 'N':
        bill += 3
        print(f'your total bill of large   pizza with pepperoni but without extra cheese is ${bill}')
    elif add_pepperoni == 'N' and extra_cheese == 'Y':
        bill += 1
        print(f'your total bill of large  pizza without pepperoni but with extra cheese is ${bill}')
    elif add_pepperoni == 'N' and extra_cheese == 'N':
        print(f'your total bill of large  pizza without pepperoni and extra cheese is ${bill}')
