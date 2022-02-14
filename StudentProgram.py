import Student as s


def main():

    student1 = ("111222333", "Jane Doe", 11 / 5 / 2000, "Jr")

    print("Student ID: ", student1.get_ID())
    print("Student Name: ", student1.get_Name())
    print("Student Age: ")
    print("Student Registration Date: ", student1.register_date())
