student_scores = input("Input a list of student scores ").split()
print(student_scores)
max_score = 0
for scores in student_scores:
    if int(scores) > max_score:
        max_score = int(scores)
print('Highest score is :', max_score)
