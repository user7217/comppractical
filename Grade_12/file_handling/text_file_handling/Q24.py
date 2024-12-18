with open('word_old.txt', 'r') as old_file, open('word_new.txt', 'w') as new_file:
    for line in old_file:
        words = line.split()
        five_char_words = [word for word in words if len(word) == 5]
        new_file.write(' '.join(five_char_words) + '\n')
