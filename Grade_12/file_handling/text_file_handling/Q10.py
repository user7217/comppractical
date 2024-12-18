#read last n lines of a text file 
with open("poem.txt") as f:
    data = f.readlines()
    n = 3
    for i in range(n):
        print(data[len(data)-n+i])
    