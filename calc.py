# simple_calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Division (/)")
    
    while True:
        choice = input("Enter your choice (1/2/3/4) or 'q' to quit: ")
        if choice.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please select a valid operation.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else :
            print( "Invalid Operation. Choice should be between 1 to 4" )
        
        print()  # Print a blank line for better readability

if __name__ == "__main__":
    main()
