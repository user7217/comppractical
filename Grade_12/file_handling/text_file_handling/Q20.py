#Write a program to copy the contents of “try.txt” into “final.txt”. While copying the content from the text file “try.txt” into “final.txt” append “#” after each and every character. 
with open("try.txt", "r") as infile, open("final.txt", "w") as outfile:
    outfile.write(''.join(c + '#' for c in infile.read()))
