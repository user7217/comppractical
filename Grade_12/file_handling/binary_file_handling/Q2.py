import random, pickle  # Importing modules for random number generation and file handling

# Take input for the number of random numbers to generate
n = int(input("How many 4-digit numbers? "))

# Generate a list of n random 4-digit numbers
pwdlist = [random.randint(1000, 9999) for _ in range(n)]

# Write the list to a binary file
with open('pwdlist.dat', 'wb') as f: 
    pickle.dump(pwdlist, f)

# Read and display the contents of the binary file
with open('pwdlist.dat', 'rb') as f: 
    print("File contents:", pickle.load(f))
