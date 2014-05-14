summands = [2]
a = 1
b = 2
barrier = 4*10**6

while(True):
    c = a+b
    if c>barrier:
        break
    if c%2==0:
        summands.append(c)
    a=b
    b=c

print sum(summands)
