


def calculator():
    print("                        CALCULATOR                   ")
    print("                         TASK - 2                    ")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if operation == '1':
            result = num1 + num2
            operation_symbol = '+'
    elif operation == '2':
            result = num1 - num2
            operation_symbol = '-'
    elif operation == '3':
            result = num1 * num2
            operation_symbol = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation_symbol = '/'
    print(f"{num1} {operation_symbol} {num2} = {result}")
    

calculator()#run
