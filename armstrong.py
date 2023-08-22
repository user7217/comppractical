n = int(input("enter a number: "))
temp = n
sum = 0

while n > 0:
    rem = n%10
    sum += rem**3
    n //= 10
if temp == sum:
    print(temp, "is an armstrong number")
else:
    print(temp, "is not an armstrong number")  