def calculator():
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))
    
    # Display the operation choices
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Prompt the user to input the operation choice
    choice = input("Enter choice (1/2/3/4): ")
    
    # Perform the calculation based on the operation choice
    if choice == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif choice == '4':
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input. Please enter a valid choice.")

# Run the calculator function
calculator()
