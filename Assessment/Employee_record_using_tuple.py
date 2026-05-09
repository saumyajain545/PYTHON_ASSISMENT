# Employee records

employees = [
    (101, "Amit", 50000),
    (102, "Riya", 60000),
    (103, "Karan", 45000)
]

# Calculate average salary
avg_salary = sum(emp[2] for emp in employees) / len(employees)

print("Average Salary:", avg_salary)
print("Employees Above Average Salary:")

for emp in employees:
    if emp[2] > avg_salary:
        print(emp)


#output
#Average Salary: 51666.67
#Employees Above Average Salary:
#(102, 'Riya', 60000)
