#factors of a number 
num = int(input("Enter a number: ")) #input number
print("Factors of",num,"are: ") #print factors of the number
for i in range(1,int((num+1)/2)): #loop from 1 to num
    if num%i==0: #if i is a factor of num
        print(i) #print i
