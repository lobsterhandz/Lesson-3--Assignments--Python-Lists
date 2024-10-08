# Task 1 Sort the grades in descending order and print the sorted list.
# code for sorted and reversed lists. 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse =True)
print("your grades sorted and reversed are ", grades)
# code for list reversal without sort
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
for grade in grades[::-1]:
    print(grade) 
#Task 2 Task 2: Calculate the average grade and print it.
average_grade = sum(grades) / len(grades)
print("your average grade is:", average_grade)

