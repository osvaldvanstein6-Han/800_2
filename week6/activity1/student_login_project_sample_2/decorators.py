from datetime import datetime


# Decorator function.
# Adds logging information before and after
# executing another function.
def log_activity(func):
    

    
    # Wrapper function that adds logging information.
    # accepts any number of positional and keyword arguments.
    def wrapper(*args, **kwargs):
        # displays the name of the function being called, the current date and time, and a message indicating that the activity has started.
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        # Calls the original function with the provided arguments and stores the result.
        result = func(*args, **kwargs)

        # displays a message indicating that the activity has completed, along with a separator line.
        print("Activity completed.")
        print("===================================\n")

        # return original function's result to maintain its behavior.
        return result

    # returns the wrapper function, effectively replacing the original function with the decorated version that includes logging functionality.
    return wrapper
