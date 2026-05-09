# Import Pandas library
import pandas as pd

# Read attendance CSV file
attendance = pd.read_csv("attendance.csv")

# Display complete data
print("Attendance Record:")
print(attendance)

# Filter students with attendance below 75%
low_attendance = attendance[attendance['Attendance'] < 75]

# Display students below 75%
print("\nStudents Below 75% Attendance:")
print(low_attendance)

'''
output
Attendance Record:
    Name  Attendance
0   Aman          80
1   Riya          70
2  Karan          65

Students Below 75% Attendance:
    Name  Attendance
1   Riya          70
2  Karan          65
'''
