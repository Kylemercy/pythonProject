#calculate average temperature of given days
numdays = int(input('how many days temperature? '))
total = 0
for i in range(1,numdays + 1):
    nextday = int(input('Day'+str(i) +' high temperature ?'))
    total += nextday
average = round(total/numdays,2)
print('Average = ',average)