import random
user_input = input("Enter a string: ")
word_list = user_input.split()
print(f"You entered: {user_input}")
print(f"Random word from the list: {random.choice(word_list)}")


