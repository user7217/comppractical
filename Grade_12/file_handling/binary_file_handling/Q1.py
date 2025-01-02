#WAP to write a tuple of 5 elements into a binary file named tupbin.dat. Also read and display the contents of tupbin.dat 
import pickle

# Tuple with 5 elements
my_tuple = (1, 'Hello', 3.14, True, [1, 2, 3])

# Write the tuple to a binary file using pickle
with open('tupbin.dat', 'wb') as file:
    pickle.dump(my_tuple, file)

# Read and display the contents of the binary file
with open('tupbin.dat', 'rb') as file:
    loaded_tuple = pickle.load(file)

print("Contents of tupbin.dat:", loaded_tuple)
