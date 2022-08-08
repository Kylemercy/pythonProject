import random
names_string = input("Give me everybody's names,separated by a comma.\n")
names = names_string.split(",")
n = len(names)
txt = random.randint(0,n-1
                     )
#print(txt)
person_to_pay = names[txt]
print(person_to_pay)
print(person_to_pay + ' is going to buy the meal today!')
