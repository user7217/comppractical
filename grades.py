#quetion 9: program to accpet percentage from user and print grade accordingly
perc = int(input("enter percentage: "))

if perc >= 90:
    print("Grade: A")
     
elif perc >= 80:
    print("Grade: B")
elif perc >= 70:
    print("Grade: C")
elif perc >= 60:
    print("Grade: D")
elif perc >= 40:
    print("Grade: E")
else:
    print("Grade: F")


