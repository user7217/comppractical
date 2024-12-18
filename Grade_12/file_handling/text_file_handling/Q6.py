#read first n lines of poem.txt
with open("poem.txt") as f:
    data = f.readlines()
    n = int(input("Enter number of lines to read: "))
    for i in range(n):
        print(data[i])

