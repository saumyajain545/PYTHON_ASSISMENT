# Program for grading system

marks = []

# Input marks for 5 subjects
for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Calculate percentage
percentage = sum(marks) / 5

# Assign grade using nested if-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Scholarship eligibility
if percentage >= 85:
    scholarship = "Eligible"
else:
    scholarship = "Not Eligible"

print("Percentage:", percentage)
print("Grade:", grade)
print("Scholarship:", scholarship)

#output
#Percentage: 86.4
#Grade: A
#Scholarship: Eligible
