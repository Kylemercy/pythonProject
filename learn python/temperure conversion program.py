print('TEMPERATURE CONVERSION PROGRAM')
print('SELECTION:\n ENTER 1 for celsius \n ENTER 2 for fahrenheit \n ENTER 3 for kelvin')
choice = int(input('Enter your selection: '))
if choice > 3:
    print('Invalid input')
if choice == 1:
    temp = float(input('Enter your temperature in celsius: '))
    fahrenheit = round((((9 / 5) * temp) + 32), 2)
    kelvin = round((temp + 273.15), 2)
    print('Temperature in fahrenheit: ', fahrenheit, 'deg f')
    print('Temperature in kelvin: ', kelvin, 'deg k')
elif choice == 2:
    temp = float(input('Enter your temperature in fahrenheit: '))
    celsius = round(((5 / 9) * (temp - 32)), 2)
    kelvin = round(((temp + 459.67) * (5 / 9)), 2)
    print('Temperature in celsius: ', celsius, 'deg c')
    print('Temperature in kelvin: ', kelvin, 'deg k')
elif choice == 3:
    temp = float(input('Enter your temperature in kelvin: '))
    celsius = round((temp - 273.15),2)
    fahrenheit = round(((temp * (9/5) - 459.67)),2)
    print('Temperature in celsius: ', celsius, 'deg c')
    print('Temperature in fahrenheit: ', fahrenheit, 'deg f')



