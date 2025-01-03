class BookStack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, book):
        if len(self.stack) >= self.size:
            print("STACK OVERFLOW! Cannot add more books.")
        else:
            self.stack.append(book)
            print(f"Book '{book[1]}' added to the stack.")

    def pop(self):
        if self.is_empty():
            print("STACK UNDERFLOW! No books to remove.")
        else:
            book = self.stack.pop()
            print(f"Removed book: {book}")

    def display(self):
        if self.is_empty():
            print("STACK UNDERFLOW! No books to display.")
        else:
            print("Books in the stack:")
            for book in reversed(self.stack):
                print(f"[ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: {book[3]}]")

    def top(self):
        if self.is_empty():
            print("STACK UNDERFLOW! No top book.")
        else:
            book = self.stack[-1]
            print(f"Top book: [ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: {book[3]}]")

    def is_empty(self):
        return len(self.stack) == 0


def menu():
    size = int(input("Enter the maximum size of the stack: "))
    book_stack = BookStack(size)

    while True:
        print("\nMENU:")
        print("1. Push")
        print("2. Pop")
        print("3. Display entire stack content")
        print("4. Display Top Node")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            price = float(input("Enter Price: "))
            book_stack.push([book_id, title, author, price])
        elif choice == "2":
            book_stack.pop()
        elif choice == "3":
            book_stack.display()
        elif choice == "4":
            book_stack.top()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
