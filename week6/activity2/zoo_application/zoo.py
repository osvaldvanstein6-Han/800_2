# zoo.py should contain the functions of the zoo system that the admin can use.

from decorators import login_required

class Zoo:

    # Create a Zoo class
    def __init__(self):

        self.animals = ["Lion", "Tiger", "Elephant"]

    # this function displays the animals in the zoo

    @login_required
    def display_animals(self):

        print("Animals in the zoo:")

        for animal in self.animals:

            print("-", animal)

