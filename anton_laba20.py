from random import randrange
i = int(input(" "))
matrix=[[randrange(-10, 10)for k in (i)]for k in (i)]

def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print("{:4d}".format(j), end = " ")
        print()
printMatrix(matrix)

def randomize(i):
    for i in range(-10, 10)
        print(i, i+1)

randomize(i)
