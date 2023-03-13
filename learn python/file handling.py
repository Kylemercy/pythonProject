# file object
# open a file
# method 1
f = open('test.txt')
# we open a file to reader write,append,read and write
f = open('test.txt', 'r')
# to open a file for reading we use lower case r for writing w,for appending a,to read and write we use r+
# to print the name of the file we opened
print(f.name)
# make sure to close the file after printing
print(f.mode)
# prints the mode in which the file is open as
f.close()
#another method of opening a file
with open('test.txt') as f:
    # we dont need to lose the file while using this method
    print(f.name)
with open('test.txt') as t:
    t_contents = t.read()
    print(t_contents)
    #how read file with large data method one using for loop
with open('test.txt') as t:
    for line in t:
        print(line,end='')
print('\n')
#another method
with open('test.txt') as t:
    t_contents = t.read(50)
    #this prints 50 characters from our file
    print(t_contents,end='')
#writing to a file
with open('text2.txt','w') as c:
    c.write('maths')

    c.write('crk')
#opening and writing in a file
with open('test.txt','r') as rf:
    with open('test.copy', 'w') as wf:
        for line in rf:
            wf.write(line)
            #this means for eaach line in the rf write it to another text file named test.copy

#working with images
#we add b to r and w cause we are working with imag which is in binary format
with open('pic.jpg','rb') as rf:
    with open('pic_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)