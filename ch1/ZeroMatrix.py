from array import array
import random

def generate_matrix(dim_0,dim_1):
    matrix = array('B')
    for _ in range(dim_0*dim_1):
        matrix.append(random.randrange(255))
    return matrix

def print_matrix(matrix,dim_0,dim_1):
    for i in range(dim_0):
        print(matrix[i*dim_0:i*dim_0+dim_1])

def zero_matrix(matrix,dim_0,dim_1):
    rows = set()
    cols = set()
    for i in range(dim_0):
        for j in range(dim_1):
            if matrix[i*dim_0 + j] == 0:
                rows.add(i)
                cols.add(j)
    for row in rows:
        for col in range(dim_1):
            matrix[row*dim_0+col] = 0
    for col in cols:
        for row in range(dim_0):
            matrix[row*dim_0 + col] = 0