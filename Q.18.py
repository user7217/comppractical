#finding prime numbers
num = int(input("enter a number: "))

if num ==0 or num==1:
    print(num," is neither prime nor composite")
else:
    for i in range(2,int(num/2)):
        if num%i ==0:
            print("the number isnt prime")
            break
        else:
            print("the number is prime")
            break
