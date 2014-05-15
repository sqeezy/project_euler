def sum_of_squares(n):
    result = 0
    for i in range(0,n+1):
        result+=i*i
    return result

def square_of_sum(n):
    return sum(range(1,n+1))**2

print square_of_sum(100)-sum_of_squares(100)