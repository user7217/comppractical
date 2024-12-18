with open('poem.txt', 'r') as poem, open('file2.txt', 'w') as file2:
    vowels = 'AEIOU'
    for line in poem:
        words = line.split()
        filtered_words = [word for word in words if word[0].isupper() and word[0] not in vowels]
        file2.write(' '.join(filtered_words) + '\n')
