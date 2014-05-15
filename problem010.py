def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(num**0.5) + 1, 6):
        if not num % i or not num % (i + 2):
            return False
    return True

tester = 1
result = 0
while tester<2*(10**6):
    tester+=1
    if is_prime(tester):
        result += tester
print result
