import calculator

def calculator_program():
    def operation(selection, num1, num2):
        if selection == 1:
            return calculator.add(num1, num2)
        elif selection == 2:
            return calculator.subtract(num1, num2)
        elif selection == 3:
            return calculator.multiply(num1, num2)
        elif selection == 4:
            return calculator.divide(num1, num2)

    while True:
        try:
            selection = int(input("Select your calculator operation: \
                                \n1. Addition\
                                \n2. Subtraction\
                                \n3. Multiplication\
                                \n4. Division\n\n"))

            if selection not in [1, 2, 3, 4]:
                print("--------------------------------------\n")
                print("Invalid selection. Please try again.\n\n")
                continue

            num1 = int(input("\nEnter the first number: "))
            num2 = int(input("\nEnter the second number: "))

            result = operation(selection, num1, num2)
            print("The result is:", result)
            break

        except ValueError:
            print("--------------------------------------\n")
            print("Invalid input. Please enter a valid integer.\n")

# Call the calculator_program() function to run the calculator
calculator_program()


#Test cases:
    # Verify that only 2 numbers can be entered
    # Verify that the outcome of the result is displayed in the console
    # Verify that under selection, a number other than 1~4 will throw an error and ask user to choose again
    # Verify that you can select addition and the result is correct
    # Verify that you can select subtraction and the result is correct
    # Verify that you can...
