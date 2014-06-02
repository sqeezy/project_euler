def sum_of_digits(x):
    result = 0
    sx = str(x)
    for i in range(0,len(sx)):
        result+=int(sx[i])
    return result

print sum_of_digits(2**1000)