import math

x = int(input("enter  number x: ")) #x is the number
n = int(input("enter  number n: ")) #n is the number of terms
def exp(x,n): #function to calculate the exponential series
    series = 1 #first term of the series is 1
    for i in range(1,n+1): #loop from 1 to n+1 (n+1 because range is exclusive)
        series += x**i/math.factorial(i) #series is the sum of the previous term and the next term
    return series #return the series
print(exp(x,n)) #print the series
