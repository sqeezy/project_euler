def isPalindrom(n):#recursive solution possible
    strN = str(n)
    result = True
    for i in range(0,len(strN)/2):
        if strN[i]!=strN[-(i+1)]:
            result=False
            break
    return result

biggestPalindrom = 0

for a in range(100,1000):
    for b in range(100,1000):
        test = a*b
        if isPalindrom(test):
            if test > biggestPalindrom:
                biggestPalindrom = test
print biggestPalindrom