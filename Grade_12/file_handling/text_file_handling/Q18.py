#program to write a list containing strings into text file write_lines.txt
with open("write_lines.txt", "w") as f:
    lines = ["This is line number %d\n" % (i+1) for i in range(5)]
    f.writelines(lines)
    print("File created successfully")
    