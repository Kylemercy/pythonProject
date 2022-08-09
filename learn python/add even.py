# adding evens
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
    else:
        continue
print(total)
# another way
sum = 0
for number in range(2, 101, 2):
    sum += number
print(sum)
