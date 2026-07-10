# The purpose of main.py is to connect everything together

import decorators
from users import User
from zoo import Zoo

admin = User("admin", "1234")
zoo = Zoo()

username = input("Enter username: ")
password = input("Enter password: ")

if admin.login(username, password):
    decorators.logged_in = True
    print("Login successful!")
    zoo.display_animals()

else:
    print("Login failed!")

