# Banking application

balance = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")


#output
#1. Deposit
#2. Withdraw
#3. Check Balance
#4. Exit
#Enter your choice: 1
#Enter deposit amount: 5000
#Amount Deposited
