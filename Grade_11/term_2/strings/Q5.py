Lines = """This is a multi-line string.
It spans across several lines.
Each line contains different words."""

# Split the lines into a list of words and count the number of words in each line
for i, line in enumerate(Lines.split('\n'), 1):
    word_count = len(line.split())
    print(f"Line {i}: {word_count} words")
