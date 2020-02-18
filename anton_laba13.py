from random import randrange
A = 6
matrix = [[randrange(-10, 10) for i in range(A)]for i in range(A)]

def printMartix(matrix):
    for i in matrix:
        for j in i:
            print("{:4d}".format(j), end = ' ')
        print()

printMartix(matrix)

def silence(A):
    while A!=5:
        print(A**2)

silence(A)

git weraafsf
