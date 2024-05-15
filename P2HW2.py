#Keoni Decipulo
#4/14/2024
#P2HW2
#Enter in your grades throughout each module to see your lowest and highest grade,
#sum of your grades and your grade average
#using some index brackets from learning how to make lists in code ninjas
grades = []
#using append to add one item at a time to grades list
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))
#
print('-----------------Results-----------------')
# Display the lowest grade
print(f"Lowest grade: {min(grades)}")

# Display the highest grade
print(f"Highest grade: {max(grades)}")

# Calculate the sum of grades
sum_of_grades = sum(grades)
print(f"Sum of grades: {sum_of_grades}")

# Calculate the average grade
average_grade = sum_of_grades / len(grades)
print(f"Average grade: {average_grade:.2f}")
print('---------------------------------------------')
