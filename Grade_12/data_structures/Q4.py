def POP_PUSH(LPop, LPush, N):
    # Check if N is greater than the length of LPop
    if N > len(LPop):
        print("Pop not possible")
    else:
        # Pop the last N elements from LPop and append them to LPush
        for _ in range(N):
            LPush.append(LPop.pop())
        print(f"Updated LPush: {LPush}")
        print(f"Updated LPop: {LPop}")

# Example execution
LPop = [10, 15, 20, 30]
LPush = []

# Define the number of elements to pop
N = 2

# Call the POP_PUSH function
POP_PUSH(LPop, LPush, N)
