from math import factorial

def nCr(n,k):
   	return factorial(n)/(factorial(k)*factorial(n-k))

print nCr(40,20)