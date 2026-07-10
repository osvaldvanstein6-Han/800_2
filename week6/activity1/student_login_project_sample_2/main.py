from users import (
    student_login,
    submit_assignment,
    view_grades
)
# Main function to run the student management system
# Calls several functions from the users module to demonstrate functionality
def main():

    # Simulate a student logging into the system.
    student_login("Mohammad")

    # Simulate submitting an assignment.
    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    # Simulate viewing grades for a student.
    view_grades("Alex")


# Entry point of the program
if __name__ == "__main__":
    main()
