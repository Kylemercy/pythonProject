#rotating a matrix in 90 degree
import numpy as np
array = np.array([[2,3,4],[4,5,6],[7,9,5]])
print(array)
def matrix_rotation(matrix):
    n = len(array)
    # this gives the number row of the 2d array
    for layer in range(n//2):
        first = layer
        last = n -layer-1
        for i in range(first,last):
     #swapping of position of elements in matrix
            top = matrix[layer][i]
     #move last left element to top
            matrix[layer][i] = matrix[-i -1][layer]
     #move bottom element to left
            matrix[-i - 1][layer] = matrix[-layer-1][-i-1]
     #move right element to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer-1]
     # move right to top
            matrix[i][-layer - 1] = top
    return matrix
print(matrix_rotation(array))