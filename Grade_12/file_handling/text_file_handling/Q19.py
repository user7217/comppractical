#program to copy contents of text1.txt into text2.txt
with open("text1.txt") as f:
    data = f.read()
    with open("text2.txt", "w") as f2:
        f2.write(data)
    print("File copied successfully")