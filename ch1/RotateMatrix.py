from array import array
import random
import math


def generate_matrix(dim):
    matrix = array('B')
    for i in range(dim*dim):
        matrix.append(random.randrange(255))
    return matrix

def print_matrix(matrix,dim):
    for i in range(dim):
        print(matrix[i*dim:i*dim+dim])

def swap(matrix, a, b,c,d):
    matrix[a],matrix[b],matrix[c],matrix[d] = matrix[d],matrix[a],matrix[b],matrix[c]

def rotate_matrix(matrix,dim):
    quad = math.ceil(dim/2)
    for i in range(quad):
        for j in range(quad):
            swap(matrix,i*dim + j,j*dim+dim-1-i,dim*(dim-i-1)+dim-j-1,dim*(dim-j-1)+ i)