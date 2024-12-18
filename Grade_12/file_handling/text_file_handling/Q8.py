#print alternate lines of a text file 
with open("poem.txt") as f:
    data = f.readlines()
    print(i for i in data if data.index(i)%2==0)