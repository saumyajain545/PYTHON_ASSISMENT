# Program to generate first N prime numbers

n = int(input("Enter value of N: "))

primes = []
num = 2

while len(primes) < n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

    num += 1

# Calculate sum and average
prime_sum = sum(primes)
average = prime_sum / n

print("Prime Numbers:", primes)
print("Sum:", prime_sum)
print("Average:", average)

#output
#Enter value of N: 5
#Prime Numbers: [2, 3, 5, 7, 11]
#Sum: 28
#Average: 5.6
