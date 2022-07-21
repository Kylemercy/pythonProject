#lists and strings
#coverting strings to list using split method
a = 'spam spam bread egg'
b = list(a)
c = a.split()
print(b)
print(c)
d = 'dog-cat-fish-cow'
item = '-'
txt = 'o'
e = d.split("-")
e = d.split(txt)
print(e)
#using join
#coverts a list back to a string
print(txt.join(e))
#pitfalls in lists to avoid
