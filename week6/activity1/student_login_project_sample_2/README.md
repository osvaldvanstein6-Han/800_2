Project Objective

This project demonstrates the use of a Python decorator to automatically log user activities without modifying the original functions.

⸻

How the Decorator Works

The log_activity decorator wraps each function with a wrapper function. Before the original function executes, it prints:

* Function name
* Current date and time
* Activity started message

After the original function finishes, it prints:

* Activity completed message

Finally, it returns the original function’s result.

⸻

Benefits of Using Decorators

* Reduces duplicated logging code.
* Improves code readability.
* Separates logging from business logic.
* Makes debugging easier.
* Follows the DRY (Don’t Repeat Yourself) principle.
* Makes the program easier to maintain and extend.

⸻

Debugging Process

During debugging, comments were added to each function to explain:

* The purpose of each function.
* How the decorator intercepts function calls.
* The role of wrapper(*args, **kwargs).
* The execution order before and after the original function.
* Why return result is necessary to preserve the original function’s behavior.

⸻

Findings

The project successfully demonstrates how Python decorators can transparently add logging functionality to multiple functions. The @log_activity decorator automatically records execution details without requiring changes to the business logic in users.py, making the code more modular, reusable, and maintainable.