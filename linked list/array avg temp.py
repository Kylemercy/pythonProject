#calculate average temperature of given days using list
numdays = int(input('how many days temperature? '))
total = 0
temp = [ ]
for i in range(numdays):
    nextday = int(input('Day'+str(i + 1) +' high temperature ?'))
    temp.append(nextday)
    total += nextday
average = round(total/numdays,2)
print('Average = ',average)
above = 0
for i in temp:
    if i > average:
        above += 1
print(str(above) + " day(s) are above average")