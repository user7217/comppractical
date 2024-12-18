with open ("sample1.txt") as f: 
    data = f.read()
    for i in range(0,len(data), 2):
        print(data[i], end = "")
    f.close()