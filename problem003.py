import sys

def prim_factors(n):
    result = []

    if n<0:
        n = -n
    if n<2:
        return [n]
    while n%2 == 0:
        result.append(2)
        n/=2

    for candidate in range(3,int(n**0.5+1),2):
        while(n%candidate==0):
            result.append(candidate)
            n/=candidate

    if n>2:
        result.append(n)
    return result

if __name__ == '__main__':
    try:
        number = int(raw_input("Enter a number to evaluate prime factors from...\n"))#600851475143
    except ValueError:
        exit("Not a integer!")
    factors = prim_factors(number)
    print "The prime factors are {}.".format(factors)
