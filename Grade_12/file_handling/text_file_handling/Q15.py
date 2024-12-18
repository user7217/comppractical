#count and print number of times "and" and "is" appear in the file
with open("poem.txt") as f:
    data = f.read()
    words = data.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    print(word_freq["and"], word_freq["is"])
