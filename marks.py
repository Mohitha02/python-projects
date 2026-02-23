import numpy as np

# Marks of 3 students in 3 subjects
# Rows = Students
# Columns = Subjects
marks = np.array([
    [85, 90, 88],   # Student 1
    [78, 82, 80],   # Student 2
    [92, 88, 95]    # Student 3
])

print("Marks of Students:\n", marks)

# Total marks of each student (row-wise sum)
total_marks = np.sum(marks, axis=1)
print("\nTotal Marks of Each Student:", total_marks)

# Average marks of each student
average_marks = np.mean(marks, axis=1)
print("Average Marks of Each Student:", average_marks)

# Highest total marks
print("Highest Total Marks:", np.max(total_marks))

# Lowest total marks
print("Lowest Total Marks:", np.min(total_marks))
