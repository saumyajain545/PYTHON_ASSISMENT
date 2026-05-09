# Merge lists and filter numbers divisible by 3 and 5

list1 = [10, 15, 20, 30]
list2 = [15, 45, 60, 10]

# Merge lists
merged = list1 + list2

# Remove duplicates
unique = list(set(merged))

# Sort in descending order
unique.sort(reverse=True)

# Filter numbers divisible by 3 and 5
result = []

for num in unique:
    if num % 3 == 0 and num % 5 == 0:
        result.append(num)

print("Final List:", result)

#output
#Final List: [60, 45, 30, 15]
