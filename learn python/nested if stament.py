print('Welcome to the rollercoster!')
height = int(input('what is your height in cm ? '))
if height >= 120:
    print('you can ride the rollercoster.')
    age = int(input('how old are you? '))
    if age > 18:
        print('Adult ticket is  $12.')
    elif age >= 12 and age <= 18 :
        print('Youth ticket is  $7.')
    elif age < 12:
        print('Child ticket is  $5.')
else:
    print('Sorry you have to grow taller before you can ride.')