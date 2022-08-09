student_heights = input("Input a list of student heights ").split()
n = len(student_heights)
print(student_heights)
sum = 0
for i in student_heights:
    sum += int(i)
print(round(sum / n, 2))
number_of_student = 0
for student in student_heights:
    number_of_student += 1
print('number of sudent:', number_of_student)
