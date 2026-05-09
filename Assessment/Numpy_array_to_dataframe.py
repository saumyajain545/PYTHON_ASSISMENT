import numpy as np
import pandas as pd

marks = np.array([[80,90,85],[75,88,92]])

df = pd.DataFrame(marks, columns=["Math", "Science", "English"])

print(df)
print("Highest Marks:\n", df.max())
print("Average Marks:\n", df.mean())

#output
'''Math  Science  English
0    80       90       85
1    75       88       92

Highest Marks:
Math       80
Science    90
English    92
dtype: int64

Average Marks:
Math       77.5
Science    89.0
English    88.5
dtype: float64 '''
