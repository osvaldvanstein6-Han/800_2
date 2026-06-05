from rectangle import Rectangle


def get_dimensions():
    length = float(input("Enter the length of the land: "))
    width = float(input("Enter the width of the land: "))
    return length, width


def display_results(rectangle):
    print("\nRectangle Information")
    print("----------------------")
    print(f"Length: {rectangle.length}")
    print(f"Width: {rectangle.width}")
    print(f"Area: {rectangle.calculate_area()}")
    print(f"Perimeter: {rectangle.calculate_perimeter()}")


if __name__ == "__main__":
    length, width = get_dimensions()

    land = Rectangle(length, width)

    display_results(land)