#create calculator using if else
n1, n2 = input("Enter two numbers: ").split()
n1, n2 = int(n1), int(n2)
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation\n7. Floor division") #menu
choice = int(input("Enter your choice: ")) #input choice
if choice==1: #if choice is 1 then add
    print("Addition is: ",n1+n2)
elif choice==2: #if choice is 2 then subtract
    print("Subtraction is: ",n1-n2)
elif choice==3: #if choice is 3 then multiply
    print("Multiplication is: ",n1*n2)
elif choice==4: #if choice is 4 then divide
    print("Division is: ",n1/n2)
elif choice==5: #if choice is 5 then modulus
    print("Modulus is: ",n1%n2)
elif choice==6: #if choice is 6 then exponentiation
    print("Exponentiation is: ",n1**n2)
elif choice==7: #if choice is 7 then floor division
    print("Floor division is: ",n1//n2)
else: #if choice is not in the range of 1 to 7 then invalid choice
    print("Invalid choice")