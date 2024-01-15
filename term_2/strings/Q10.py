import random

word_list = ["apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "strawberry"]

user_input = input("Enter a string: ")
print(f"You entered: {user_input}")
print(f"Random word from the list: {random.choice(word_list)}")
