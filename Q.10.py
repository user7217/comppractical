num = int(input("enter a number: "))
sum = 0
product = 1
for i in range(1, num+1):
    sum += i
    product = product*i
print(sum, product)
