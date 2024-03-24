# Function to calculate maximum, minimum, sum, and average marks
def analyze_marks(student_marks):
    max_marks = max(student_marks)
    min_marks = min(student_marks)
    total_marks = sum(student_marks)
    average_marks = total_marks / len(student_marks)

    return max_marks, min_marks, total_marks, average_marks

# Accepting marks for five students into a list of tuples
student_marks_list = []

for i in range(5):
    student_marks = tuple(map(int, input(f"Enter marks for student {i + 1} in three subjects separated by space: ").split()))
    student_marks_list.append(student_marks)

# Analyzing and displaying results for each student
for i, student_marks in enumerate(student_marks_list, 1):
    max_marks, min_marks, total_marks, average_marks = analyze_marks(student_marks)

    print(f"\nStudent {i} - Marks Analysis:")
    print("Maximum Marks:", max_marks)
    print("Minimum Marks:", min_marks)
    print("Total Marks:", total_marks)
    print("Average Marks:", average_marks)
