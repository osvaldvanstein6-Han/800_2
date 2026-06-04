student_list = []


class Student:

    def set_data(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


def collect_students():

    print("Enter details for at least 3 students:\n")

    for i in range(3):

        print(f"Student {i + 1}")

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        student_id = input("Enter student ID: ")

        student = Student()

        student.set_data(
            name,
            age,
            student_id
        )

        student_list.append(student)

        print()


def display_students():

    print("\nList of Students:")

    sorted_students = sorted(
        student_list,
        key=lambda s: s.name.lower()
    )

    for student in sorted_students:
        print(student.display_info())


if __name__ == "__main__":
    collect_students()
    display_students()