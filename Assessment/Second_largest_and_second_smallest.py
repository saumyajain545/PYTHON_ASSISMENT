# Function to find second largest and second smallest

def second_values(lst):
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    for num in lst:
        # Second largest
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

        # Second smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_largest, second_smallest

numbers = [12, 45, 7, 89, 23, 5]

result = second_values(numbers)

print("Second Largest:", result[0])
print("Second Smallest:", result[1])

#output
#Second Largest: 45
#Second Smallest: 7
