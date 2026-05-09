# Recursive function to calculate sum of digits

def recursive_sum(n):

    # Base condition
    if n == 0:
        return 0

    # Recursive call
    return n % 10 + recursive_sum(n // 10)


# Iterative function to calculate sum of digits
def iterative_sum(n):

    total = 0

    # Loop until number becomes 0
    while n > 0:
        total += n % 10
        n //= 10

    return total


# Input from user
number = int(input("Enter a number: "))

# Display results
print("Recursive Sum:", recursive_sum(number))
print("Iterative Sum:", iterative_sum(number))

'''
output
Enter a number: 1234

Recursive Sum: 10
Iterative Sum: 10
'''
