summands = []

for num in range(0,1000):
    if num%3==0 or num%5==0:
        summands.append(num)
print sum(summands)