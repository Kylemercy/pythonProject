import numpy as np
#two dimensional array
my_array = np.array([[12,23,22,44],[23,45,46,77],[18,45,88,90],[43,53,63,73]])
print(my_array)
new_array = np.insert(my_array,3,[[19,59,37,40]],axis=1)
#inserting an element in a two dimensional array
#note axis =1 adds new column to the 2dimension array and axis = 0 adds new row
print(new_array)
#another way to insert in a 2d array is using append this adds row or column at end at the array
new_array1 = np.append(my_array,[[1, 9, 87, 40]], axis=0)
print(new_array1)
#acessing elements in 2d array using index notec first number is row index and second is column index
def acessarray(array,rowindex,columnindex):
    if rowindex >= len(array) and columnindex >= len(array[0]):
        print('incorrect index')
    else:
        print(array[rowindex][columnindex])
acessarray(my_array,2,2)
#travasal of 2d array
def travasal(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
#travasal(my_array)
#searching for element in 2d array
def searching(array,element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == element:
                return 'element found at index '+ str(i) +' ' + str(j)

    return 'element not found'
print(searching(my_array,77))
#deletion of row column in a 2d array
new_array = np.delete(my_array,0,axis = 1)
print(new_array)
