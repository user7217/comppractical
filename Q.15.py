#count the number of negative positive and zero numbers from an input list and terminate when zero and odd and even numbers from an input list and terminate when zero is entered
pos = 0
neg = 0
odd = 0
even = 0
while True:
    num = int(input("enter a number: "))
    if num == 0:
        break
    if num > 0:
        pos += 1
    else:
        neg += 1
    if num%2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)
print("Number of positive numbers: ",pos)
print("Number of negative numbers: ",neg)
