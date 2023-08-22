def fibonacci(n):
    f = [0, 1] #list of first two fibonacci numbers
    for i in range(2, n+1): #for loop to iterate through the list from 2 to n+1 (n+1 because range is exclusive) 
        f.append(f[i-1] + f[i-2]) #new val of the list is the sum of the previous two values in the list before f[i]
    return f[n] #return the nth value of the list
print(fibonacci(9))