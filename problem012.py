def number_of_divisors(number):
    nod = 0
    sqrt = int(number**0.5)

    for i in range(1,sqrt+1):
        if number%i==0:
            nod += 2
    if sqrt * sqrt == number:
        nod-=1

    return nod

number = 0
i = 1

while number_of_divisors(number)<500:
    number+=i
    i+=1

print number