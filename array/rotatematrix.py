# rotating an N*N matrix in a clockwise direction
import numpy as np
class solution:
    def rotate_matrix(self, matrix):
        # setting our pointers note number of columns and rows are thesame
        l, r = 0, len(matrix) - 1
        while l < r:
            # to determine the number of rotations to be done
            for i in range(r - l):
                top, bottom = l, r
                # save our topleft value
                topleft = matrix[top][l + i]
                # move the bottom left to the top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move the bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move the top right to the
                matrix[bottom][r - i] = matrix[top + i][r]
                # move topleft to the top right
                matrix[top + i][r] = topleft

            r -= 1
            l += 1
        return matrix

ll = solution()
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ll.rotate_matrix(matrix))
