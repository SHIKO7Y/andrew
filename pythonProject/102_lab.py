from turtledemo.chaos import jumpto

print("-_-__CSCI102_LAB__-_-")

student_no = int(input("Enter your number: "))
grades = []
for i in range(student_no):
    grade = int(input("Enter your grade: "))  # Convert grade to integer
    grades.append(grade)

print("Maximum grade :", max(grades))
print("Minimum grade:", min(grades))

grades = 