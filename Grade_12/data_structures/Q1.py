class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, item):
        if len(self.stack) >= self.size:
            print("Stack Overflow! Cannot add more items.")
        else:
            self.stack.append(item)
            print(f"{item} pushed to stack.")

    def pop(self):
        if not self.stack:
            print("Stack Underflow! No items to pop.")
        else:
            print(f"Popped item: {self.stack.pop()}")

    def display(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print("Stack contents:", self.stack)

    def top(self):
        if not self.stack:
            print("Stack is empty. No top element.")
        else:
            print(f"Top element: {self.stack[-1]}")

def menu():
    size = int(input("Enter the size of the stack: "))
    stack = Stack(size)

    while True:
        print("\nMENU:")
        print("1. Push")
        print("2. Pop")
        print("3. Display entire stack content")
        print("4. Display Top Node")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter a number to push: "))
            stack.push(num)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            stack.display()
        elif choice == "4":
            stack.top()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
