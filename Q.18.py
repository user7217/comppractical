# #finding prime numbers
# num = int(input("enter a number: "))

# if num ==0 or num==1:
#     print(num," is neither prime nor composite")
# else:
#     for i in range(2,int(num/2)):
#         if num%i ==0:
#             print("the number isnt prime")
#             break
#         else:
#             print("the number is prime")
#             break
# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)