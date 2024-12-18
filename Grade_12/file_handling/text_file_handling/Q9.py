#read random line from file
with open("poem.txt") as f:
    data = f.readlines()
    import random
    print(random.randint(0, len(data)-1), data[random.randint(0, len(data)-1)])