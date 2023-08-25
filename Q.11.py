#sum and product of first n odd and even numbers
n = int(input("Enter a number: ")) #input number
sum_even = 0 #sum of even numbers
sum_odd = 0 #sum of odd numbers
product_even = 1 #product of even numbers
product_odd = 1 #product of odd numbers
for i in range(1,n+1): #loop from 1 to n
    if i%2==0: #if i is even
        sum_even+=i #add i to sum_even
        product_even*=i #multiply i to product_even
    else: #if i is odd
        sum_odd+=i #add i to sum_odd
        product_odd*=i #multiply i to product_odd
print("Sum of first",n,"even numbers is: ",sum_even)
print("Sum of first",n,"odd numbers is: ",sum_odd)
print("Product of first",n,"even numbers is: ",product_even)
print("Product of first",n,"odd numbers is: ",product_odd)
