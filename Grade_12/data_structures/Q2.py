def PUSHSTACK(STK, N):
    if len(STK) >= 10:
        print("STACK OVERFLOW! Cannot add more items.")
    else:
        STK.append(N)
        print(f"{N} pushed into the stack.")

def IS_EMPTY(STK):
    return len(STK) == 0

def POPSTACK(STK):
    if IS_EMPTY(STK):
        print("STACK UNDERFLOW! No items to pop.")
        return None
    else:
        return STK.pop()

def SHOWSTACK(STK):
    if IS_EMPTY(STK):
        print("STACK UNDERFLOW! Stack is empty.")
    else:
        print("Stack contents:", STK)

def PEEK(STK):
    if IS_EMPTY(STK):
        print("STACK UNDERFLOW! Stack is empty.")
    else:
        print(f"Topmost element: {STK[-1]}")

def menu():
    L = []
    while True:
        print("\nStack Menu:")
        print("===========")
        print("1. Push into Stack")
        print("2. Pop from Stack")
        print("3. Show Stack")
        print("4. Peek Top Element")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter a number to push: "))
            PUSHSTACK(L, num)
        elif choice == "2":
            item = POPSTACK(L)
            if item is not None:
                print(f"Popped item: {item}")
        elif choice == "3":
            SHOWSTACK(L)
        elif choice == "4":
            PEEK(L)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
