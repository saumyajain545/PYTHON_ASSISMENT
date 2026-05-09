import pandas as pd

students = {
    'Name': ['A', 'B'],
    'Math': [80, 90],
    'Science': [85, 95]
}

df = pd.DataFrame(students)

df['Total'] = df['Math'] + df['Science']
df['Percentage'] = df['Total'] / 2

df['Grade'] = df['Percentage'].apply(lambda x: 'A' if x >= 90 else 'B')

print(df)

'''
output
Name  Math  Science  Total  Percentage Grade
0    A    80       85    165        82.5     B
1    B    90       95    185        92.5     A
'''
