# Import Pandas library
import pandas as pd

# Dictionary to store student records
students = {}

try:
    # Input student details
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    # Store data in dictionary
    students[roll] = [name, marks]

    # Convert dictionary data into DataFrame
    df = pd.DataFrame(
        students.values(),
        columns=['Name', 'Marks']
    )

    # Assign grades using apply function
    df['Grade'] = df['Marks'].apply(
        lambda x: 'A' if x >= 75 else 'B'
    )

    # Display report
    print("\nStudent Report:")
    print(df)

    # Save report into CSV file
    df.to_csv("student_report.csv", index=False)

    print("\nReport Saved Successfully")

# Handle invalid input
except ValueError:
    print("Invalid Input")

'''
output
Enter Roll Number: 101
Enter Student Name: Aman
Enter Marks: 82

Student Report:
   Name  Marks Grade
0  Aman     82     A

Report Saved Successfully
''' 
