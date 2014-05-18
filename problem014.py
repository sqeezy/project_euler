def next(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def sequence(n):
    seq = [n]
    while n!=1:
        n = next(n)
        seq.append(n)
    return seq

maxLen = 0
maxNum = 0
for i in range(1,10**6):
    curLen = len(sequence(i))
    if curLen>maxLen:
        maxLen=curLen
        maxNum = i
        print maxLen
print maxLen
print maxNum