import math

x = int(input("enter  number x: "))
n = int(input("enter  number n: "))
def exp(x,n):
    series = 1
    for i in range(1,n+1):
        series += x**i/math.factorial(i)
    return series
print(exp(x,n))
