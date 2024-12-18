#print n lines of a text file and line number along with it 
with open("poem.txt") as f:
    data = f.readlines()
    n = int(input("Enter number of lines to read: "))
    for i in range(n):
        print(i+1, data[i])