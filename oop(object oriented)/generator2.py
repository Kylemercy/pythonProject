# creating a generator
def square(my_nums):
    for i in my_nums:
        yield i * i


nums = square([3, 4, 6, 7, 8, 11.12])
print(nums)
# another way to print out the generated values is
for j in nums:
    print(j)

# this yields an object
# print(next(nums))

'''the next allows the number  to be printed
print(next (nums))
print(next (nums))
print(next (nums))
print(next (nums))
print(next (nums))
print(next (nums))'''
# when the whole list has been iterated a
# stop-iteration exception is raised
# list comprehension
my_num = [x * x for x in [2, 3, 4, 5, 6]]
print(my_num)
# a generator can be created from this
my_num = (x * x for x in [2, 3, 4, 5, 6])
print(my_num)
# this print a generator object
for j in my_num:
    print(j)

    # to  compare between generator and list
import random
import time

names = ['john', 'mike', 'faith', 'hannah', 'jay', 'caleb']
major = ['CRK', 'sociology', 'physics', 'chemistry', 'engineering', 'agriculture']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {'id': i,
                  'name': random.choice(names),
                  'major': random.choice(major)}
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {'id': i,
                  'name': random.choice(names),
                  'major': random.choice(major)}

        yield person


t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()
print(f"Took {t1-t2} seconds")
