import sys

directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[-1,1],[-1,-1]]
matrix = []
try:
    file = open("problem011-data.txt",'r')
    for line in file:
        row = []
        splits = line.split(' ')
        for numCandidate in splits:
            row.append(int(numCandidate))
        matrix.append(row)
except ValueError:
    exit("The data in this file is not valid.")

greatestProduct = 0
xMax = len(matrix)-1
yMax = len(matrix[0])-1

for x in range(0,len(matrix)):
    for y in range(0,len(matrix[0])):
        for direction in directions:
            xtest = x+3*direction[0]
            ytest = y+3*direction[1]
            if xtest <= xMax and ytest <= yMax:
                testProduct = matrix[x][y]
                for i in range(1,4):
                    xfac = x+i*direction[0]
                    yfac = y+i*direction[1]
                    testProduct *= matrix[xfac][yfac]
                if testProduct > greatestProduct:
                    greatestProduct = testProduct

print greatestProduct