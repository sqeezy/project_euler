def factorial(x):
    if(x==1):
        return 1
    return x*factorial(x-1)

num = str(factorial(100))

numAsString = str(num)

sum = 0
for c in numAsString:
    sum += int(c)

print sum