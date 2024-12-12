with open ("sample1.txt") as f: 
    data = f.read()
    for i in data:
        if i.isnumeric():
            print(i, end = "")