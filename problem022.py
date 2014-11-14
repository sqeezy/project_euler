import string
f = open("names.txt")

names = f.readline().split(',')

for i in range(0,len(names)):
    new = names[i][1:-1]
    names[i] = new

names.sort()

def getValueForWord(x):
    summands = []
    for c in x:
        summands.append(string.uppercase.index(c)+1)
    return sum(summands)

values = []
for i in range(0,len(names)):
    name = names[i]
    values.append(getValueForWord(name)*(i+1))

print sum(values)
