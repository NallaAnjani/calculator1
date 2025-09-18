from calc import add, sub, mul, div

print("------------------- Command-line Calculator ----------------")

while True:  
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for Exit")

    option = input("Enter your choice: ")
    
    if not option.isdigit(): 
        print("Please enter a valid number for choice!")
        continue
    option = int(option)

    if option == 5:
        print("Thank you for using calculator")
        break

    if option not in [1, 2, 3, 4]:
        print(" Invalid choice! Please select 1–5.")
        continue

    num1 = input("Enter the first number: ")
    if not num1.isdigit():  
        print(" Please enter an integer for first number!")
        continue
    num1 = int(num1)

    num2 = input("Enter the second number: ")
    if not num2.isdigit():   
        print(" Please enter an integer for second number!")
        continue
    num2 = int(num2)

    if option == 1:
        print("The Addition of two numbers:", add(num1, num2))
    elif option == 2:
        print(" The Subtraction of two numbers:", sub(num1, num2))
    elif option == 3:
        print(" The Multiplication of two numbers:", mul(num1, num2))
    elif option == 4:
        if num2 == 0:
            print(" Division by zero is not allowed!")
        else:
            print(" The Division of two numbers:", div(num1, num2))
