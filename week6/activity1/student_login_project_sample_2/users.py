from decorators import log_activity
# importing the log_activity decorator from the decorators module

#  Logs student login activity.
@log_activity
def student_login(username):
    print(f"{username} logged into the system.")


#  Logs assignment submission activity.
@log_activity
def submit_assignment(username, assignment):
    print(f"{username} submitted {assignment}.")


# Logs grade viewing activity.
@log_activity
def view_grades(username):
    print(f"{username} is viewing grades.")

