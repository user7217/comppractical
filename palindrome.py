n = int(input("enter a number: "))
num = n
palindrome = 0 

while num > 0:
    rem = num%10
    palindrome = palindrome*10 + rem
    num //= 10
if n == palindrome:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")