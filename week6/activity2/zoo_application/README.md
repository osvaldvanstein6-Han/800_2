# Zoo Application - Admin Login System

## Project Description

This project is a simple Zoo Application developed in Python. It demonstrates how to use a **decorator** to protect functions so that only a logged-in administrator can access the zoo information.

---

## Project Structure

```
zoo_application/
│
├── decorators.py   # Contains the login_required decorator
├── users.py        # Defines the User class and login function
├── zoo.py          # Defines the Zoo class and zoo functions
├── main.py         # Runs the application
└── README.md       # Project documentation
```

---

## Features

- Admin login system
- Username and password verification
- Display zoo animals after successful login
- Function protection using a Python decorator

---

## How to Run

1. Open the project folder in VS Code.
2. Activate the virtual environment.

### macOS

```bash
source .venv/bin/activate
```

3. Run the program.

```bash
python main.py
```

4. Enter the login details.

Example:

```
Username: admin
Password: 1234
```

---

## Example Output

```
Enter username: admin
Enter password: 1234
Login successful!

Animals in the zoo:
- Lion
- Tiger
- Elephant
```

---

## How the Decorator Works

The project uses a decorator called `login_required`.

- The decorator checks whether the administrator is logged in.
- If the user has logged in successfully, the protected function is executed.
- Otherwise, access is denied and a message is displayed.

Example:

```python
@login_required
def display_animals(self):
    ...
```

This separates the login check from the main zoo functions and makes the code cleaner and easier to maintain.

---

## Conclusion

This project demonstrates:

- Python classes
- Object-Oriented Programming (OOP)
- User authentication
- Python decorators
- Function protection using decorators

The decorator improves code readability by separating authentication logic from the main application logic.