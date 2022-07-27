print('Welcome to the rollercoster!')
height = int(input('what is your height in cm ? '))
if height >= 120:
    print('you can ride the rollercoster.')
    age = int(input('how old are you? '))
    photo = input(" Do you want a photo: ").lower()
    bill = 0

    if age >= 18:
        bill += 12

    if age >= 12 and age <18 :
        bill += 7
    if age < 12:
        bill += 5

    if photo == 'yes':
        bill += 3
        print(f' your total bill is $ {bill}')
    if photo == 'no':
        print(f' your total bill is $ {bill}')


else:
    print('Sorry you have to grow taller before you can ride.')
