import json
import os
import random
import re
import sys
from datetime import datetime

DATA_FILE = "users.json"


class UserManager:
    def __init__(self, storage_path=DATA_FILE):
        self.storage_path = storage_path
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.storage_path):
            return []
        with open(self.storage_path, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def save_users(self):
        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump(self.users, file, indent=2)

    def find_user(self, email):
        normalized = email.strip().lower()
        return next((user for user in self.users if user["email"] == normalized), None)

    def add_user(self, full_name, dob, email, password):
        self.users.append({
            "full_name": full_name.strip(),
            "dob": dob,
            "email": email.strip().lower(),
            "password": password,
            "reset_code": None,
        })
        self.save_users()

    def update_user(self, user):
        self.save_users()

    def authenticate(self, email, password):
        user = self.find_user(email)
        if not user or user["password"] != password:
            return None
        return user

    def create_recovery_code(self, email):
        user = self.find_user(email)
        if not user:
            return None
        code = f"{random.randint(100000, 999999)}"
        user["reset_code"] = code
        self.save_users()
        return code

    def reset_password(self, email, code, new_password):
        user = self.find_user(email)
        if not user or user.get("reset_code") != code:
            return False
        user["password"] = new_password
        user["reset_code"] = None
        self.save_users()
        return True


def print_header():
    print("\n=== Week 10 Activity 1 Python Login & Signup System ===\n")


def validate_email(email):
    if not email or "@" not in email:
        return False
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))


def validate_password(password):
    return len(password) >= 6


def validate_dob(dob_text):
    try:
        datetime.strptime(dob_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def prompt_input(prompt_text):
    return input(prompt_text).strip()


def prompt_signup(manager):
    print("\n--- Signup ---")
    full_name = prompt_input("Full Name: ")
    dob = prompt_input("Date of Birth (YYYY-MM-DD): ")
    email = prompt_input("Email: ")
    password = prompt_input("Password: ")
    confirm_password = prompt_input("Confirm Password: ")

    if not full_name:
        print("Full Name is required.")
        return
    if not validate_dob(dob):
        print("Date of Birth must be in YYYY-MM-DD format.")
        return
    if not validate_email(email):
        print("Email is invalid.")
        return
    if manager.find_user(email):
        print("An account with this email already exists.")
        return
    if not validate_password(password):
        print("Password must be at least 6 characters.")
        return
    if password != confirm_password:
        print("Passwords do not match.")
        return

    manager.add_user(full_name, dob, email, password)
    print("Account created successfully. You can now log in.")


def prompt_login(manager):
    print("\n--- Login ---")
    email = prompt_input("Email: ")
    password = prompt_input("Password: ")

    user = manager.authenticate(email, password)
    if not user:
        print("Email or password is incorrect.")
        return None

    print(f"\nWelcome back, {user['full_name']}!")
    return user


def prompt_forgot_password(manager):
    print("\n--- Forgot Password ---")
    email = prompt_input("Email: ")
    if not validate_email(email):
        print("Email is invalid.")
        return
    code = manager.create_recovery_code(email)
    if not code:
        print("No account matches this email.")
        return
    print("Recovery code generated.")
    print(f"Recovery Code: {code}")
    print("Use this code in the Reset Password option.")


def prompt_reset_password(manager):
    print("\n--- Reset Password ---")
    email = prompt_input("Email: ")
    code = prompt_input("Recovery Code: ")
    new_password = prompt_input("New Password: ")
    confirm_password = prompt_input("Confirm Password: ")

    if not validate_password(new_password):
        print("Password must be at least 6 characters.")
        return
    if new_password != confirm_password:
        print("Passwords do not match.")
        return
    if manager.reset_password(email, code, new_password):
        print("Password has been reset. You can now log in.")
    else:
        print("Invalid recovery code or email.")


def show_profile(user):
    print("\n--- Account Details ---")
    print(f"Full Name: {user['full_name']}")
    print(f"Date of Birth: {user['dob']}")
    print(f"Email: {user['email']}")


def prompt_update_profile(manager, user):
    print("\n--- Edit Profile ---")
    full_name = prompt_input(f"Full Name ({user['full_name']}): ") or user["full_name"]
    dob = prompt_input(f"Date of Birth ({user['dob']}): ") or user["dob"]

    if not full_name.strip():
        print("Full Name cannot be empty.")
        return
    if not validate_dob(dob):
        print("Date of Birth must be in YYYY-MM-DD format.")
        return

    user["full_name"] = full_name.strip()
    user["dob"] = dob
    manager.update_user(user)
    print("Profile updated successfully.")


def account_menu(manager, user):
    while True:
        print("\n--- Account Menu ---")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Logout")
        choice = prompt_input("Select an option: ")
        if choice == "1":
            show_profile(user)
        elif choice == "2":
            prompt_update_profile(manager, user)
        elif choice == "3":
            print("Logged out.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


def main():
    manager = UserManager()
    print_header()
    while True:
        print("1. Signup")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Reset Password")
        print("5. Exit")
        choice = prompt_input("Select an option: ")

        if choice == "1":
            prompt_signup(manager)
        elif choice == "2":
            user = prompt_login(manager)
            if user:
                account_menu(manager, user)
        elif choice == "3":
            prompt_forgot_password(manager)
        elif choice == "4":
            prompt_reset_password(manager)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication interrupted.")
        sys.exit(0)
