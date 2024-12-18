#program to write n lines into a text file called lines.txt
with open("lines.txt", "w") as f:
    n = 5
    for i in range(n):
        f.write("This is line number %d\n" % (i+1))
    print("File created successfully")