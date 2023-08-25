#check if leap year or not
year = int(input("Enter a year: "))
if year%4==0:#if the year is divisible by 4 then it is a leap year
    if year%100==0: #if the year is divisible by 100 then it is not a leap year
        if year%400==0: #if the year is divisible by 400 then it is a leap year
            print("Leap year")
        else:
            print("Not a leap year") 
    else:
        print("Leap year")
