def palindrome(s): #function to check string is palindrome or not
    rev = ''.join(reversed(s))   #reversed() function returns the reversed iterator of the given string
    if (s == rev): #checking if the string is equal to its reverse
        return True #return true if it is palindrome
    return False #return false if it is not palindrome
 
s = str(input("Enter a string: ")) #input string
ans = palindrome(s) #calling the function
 
if (ans): #if ans is true
    print("Yes") #print yes
else: #else
    print("No") #print no