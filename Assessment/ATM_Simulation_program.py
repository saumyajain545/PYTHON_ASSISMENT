# ATM Simulation Program with PIN Validation

# Correct ATM PIN
correct_pin = "1234"

# Counter for invalid attempts
attempts = 0

# Loop until maximum 3 attempts
while attempts < 3:

    # Taking PIN input from user
    pin = input("Enter ATM PIN: ")

    # Check if entered PIN is correct
    if pin == correct_pin:
        print("Access Granted")
        break

    else:
        # Increase invalid attempt counter
        attempts += 1
        print("Incorrect PIN")

# Lock account after 3 wrong attempts
if attempts == 3:
    print("Account Locked")

'''
output
Enter ATM PIN: 1234
Access Granted
'''
