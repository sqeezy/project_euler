f = open("problem018-data.txt",'r')

levels = []
for rawLine in f:
    numbers = rawLine.split(' ')
    level = []
    for number in numbers:
        level.append(int(number))
    levels.append(level)

def bestWayValue(x,y):
    if(y==len(levels)-1):
        return levels[y][x]
    leftValue = bestWayValue(x,y+1)
    rightValue = bestWayValue(x+1,y+1)
    return max(leftValue,rightValue)+levels[y][x]

print bestWayValue(0,0)