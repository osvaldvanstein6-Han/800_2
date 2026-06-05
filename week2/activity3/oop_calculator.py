# Week 2 - Activity 3
# Object-Oriented Programming Project - Basic Mathematical Operations


class Calculator:
    def __init__(self, number1, number2):
        # Store the two numbers as object attributes
        self.number1 = number1
        self.number2 = number2

    # Method 1: addition
    def add(self):
        return self.number1 + self.number2

    # Method 2: subtraction
    def subtract(self):
        return self.number1 - self.number2

    # Method 3: multiplication
    def multiply(self):
        return self.number1 * self.number2

    # Method 4: division
    def divide(self):
        if self.number2 != 0:
            return self.number1 / self.number2
        else:
            return "Cannot divide by zero"


# Function 1: get user input
def get_numbers():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    return number1, number2


# Function 2: display results
def display_results(calculator):
    print("\nBasic Mathematical Operations")
    print("-----------------------------")
    print(f"Addition: {calculator.add()}")
    print(f"Subtraction: {calculator.subtract()}")
    print(f"Multiplication: {calculator.multiply()}")
    print(f"Division: {calculator.divide()}")


# Main program
if __name__ == "__main__":
    num1, num2 = get_numbers()

    calculator = Calculator(num1, num2)

    display_results(calculator)