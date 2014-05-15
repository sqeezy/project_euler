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

def lcm(numbers):
    if type(numbers)!=list:
        raise ValueError("numbers is not of type 'list'")
    for num in numbers:
        try:
            int(num)
        except ValueError:
            raise ValueError("Not all members of numbers are of type 'int'.")

    resultFactorExponents = dict()

    for number in numbers:
        factors = prim_factors(number)
        for fac in factors:
            if fac not in resultFactorExponents:
                resultFactorExponents[fac] = factors.count(fac)
            else:
                if factors.count(fac)>resultFactorExponents[fac]:
                    resultFactorExponents[fac] = factors.count(fac)

    result = 1
    for key in resultFactorExponents.keys():
        result *= key**resultFactorExponents[key]
    return result

divs = range(1,21)
print lcm(divs)
