
# A decorator is a function that wraps another function.
# Admin credentials
#Admin_username = "admin" # This creates a variable containing the administrator’s username.
#Admin_password = "admin123" # This creates a variable containing the administrator’s password.

# Logged in status
#logged_in = False

from functools import wraps

# Login status

logged_in = False

# This is the decorator.
def login_required(func):

    # Keeps the original function information.
    @wraps(func)

    def wrapper(*args, **kwargs):

        global logged_in

        if logged_in:

            return func(*args, **kwargs)

        else:

            print("Access denied. Please log in first.")

    return wrapper

