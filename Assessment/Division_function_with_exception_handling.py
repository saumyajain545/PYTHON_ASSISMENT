def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Invalid Input")

divide(10, 2)

#output
#5.0
