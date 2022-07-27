print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
#note count function counts only alphabet in lowercase
names = name1 + name2
t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')
true = t + r + u + e
l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')

love = l + o + v + e
love_score = int (str(true) + str(love))
if (love_score < 10) or  (love_score > 90):
    print(f'you love score is {love_score} you go together like coke and mentos')
elif love_score >= 40 and love_score <= 50:
    print(f' your love score is {love_score} you are alright together.')
else:
    print(f' your love score is {love_score}')
