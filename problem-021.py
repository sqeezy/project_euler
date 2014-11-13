def get_proper_devisors(x):
    result = []
    for i in range(1, x / 2 + 1):
        if x % i == 0:
            result.append(i)
    return result


divisorsSum = dict()
for i in range(1, 10000):
    divisorsSum[i] = sum(get_proper_devisors(i))

amicableNums = set()
for keyOne in divisorsSum.keys():
    for keyTwo in divisorsSum.keys():
        if keyOne == keyTwo:
            continue
        if divisorsSum[keyOne] == keyTwo and divisorsSum[keyTwo] == keyOne:
            amicableNums.add(keyOne)
            amicableNums.add(keyTwo)

print divisorsSum
print(amicableNums)
print sum(amicableNums)