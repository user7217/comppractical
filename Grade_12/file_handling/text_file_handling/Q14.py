#find and print longest word in file
with open("poem.txt") as f:
    data = f.read()
    words = data.split()
    print(max(words, key=len))
    