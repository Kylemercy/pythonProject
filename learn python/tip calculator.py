print('WELCOME TO TIP CALCULATOR')
bill = float(input('how much is your total bill?\n'))
tip = float(input('what percentage tip do you want to give,10,12,15,20?\n '))
num = float(input('how many people to split the bill?\n'))
total = bill + tip/100*bill
amount = total / num
split = "{:.2f}".format(amount)
#another way of formatting
print(f'Each of you will pay a bill of ${split}.')
