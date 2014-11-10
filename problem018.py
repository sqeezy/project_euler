f = open("problem018-data.txt",'r')

levels = []
for rawLine in f:
    numbers = rawLine.split(' ')
    level = []
    for number in numbers:
        level.append(int(number))
    levels.append(level)

bestPathTillDepth = []
way = []
for i in range(0,len(levels)):
    bestPathTillDepth.append(0)



for level in range(0,len(levels)):
    for number in range(0,len(levels[level])):
        tryForBest = bestPathTillDepth[level-1]+levels[level][number]
        if(tryForBest>bestPathTillDepth[level]):
            bestPathTillDepth[level] = tryForBest
#Way has to be saved

print bestPathTillDepth
print len(bestPathTillDepth)
