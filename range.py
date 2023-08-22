#o print all the numbers in the given range divisible by a given number 
num = int(input("enter a number: "))
div = int(input("enter a number to divide by: "))
for i in range(0, num):
    if i%div ==0:
        print(i)
        