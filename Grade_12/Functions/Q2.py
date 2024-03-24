#generate random number between input range
import random
def random_number(a,b):
    return random.randint(a,b)
a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
print(random_number(a,b))