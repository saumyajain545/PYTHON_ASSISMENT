n = int(input("Enter rows: "))
sum_val = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
        sum_val += j
    print()

print("Sum:", sum_val)

'''
output
Enter rows: 4
1
1 2
1 2 3
1 2 3 4

Sum: 20
'''
