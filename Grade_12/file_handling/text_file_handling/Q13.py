#count frequency of each word in a file
with open("poem.txt") as f:
    data = f.read()
    words = data.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    print(word_freq)
