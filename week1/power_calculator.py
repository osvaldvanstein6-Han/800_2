def calculate_power(x, y):

    return x ** y

def main():

    print("Power Calculator")

    print("----------------")

    x = float(input("Enter the base number x: "))

    y = float(input("Enter the exponent number y: "))

    result = calculate_power(x, y)

    print(f"{x} raised to the power of {y} is: {result}")

if __name__ == "__main__":

    main()