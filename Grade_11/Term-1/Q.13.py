#o print all the numbers in the given range divisible by a given number 
num = int(input("enter the range : ")) #range of numbers
div = int(input("enter a number to divide by: ")) #number to divide by
for i in range(0, num): #loop from 0 to num
    if i%div ==0: #if i is divisible by div
        print(i) #print i
        