# Open "new.txt" in append mode to retain its content
with open('new.txt', 'a') as new_file:
    # Open "sample.txt" in read mode
    with open('sample.txt', 'r') as sample_file:
        # Iterate through each line in sample.txt
        for line in sample_file:
            words = line.split()
            # Filter words starting with 't' or 'T'
            filtered_words = [word for word in words if word.lower().startswith('t')]
            # Write the filtered words to "new.txt"
            new_file.write(' '.join(filtered_words) + '\n')
