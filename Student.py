class Student:
    """
    Represents a student with attributes such as student ID, first name, last name, email, and phone number.
    """

    def __init__(self, student_id, first_name, last_name, email, phone_number):
        """
        Initializes a new Student object with the provided information.

        Args:
            student_id (int): The student's unique identifier.
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            email (str): The email address of the student.
            phone_number (str): The phone number of the student.
        """
        self._student_id = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number

    # Getter methods
    def get_student_id(self):
        """
        Get the student's unique identifier.

        Returns:
            int: The student's ID.
        """
        return self._student_id

    def get_first_name(self):
        """
        Get the first name of the student.

        Returns:
            str: The first name of the student.
        """
        return self._first_name

    def get_last_name(self):
        """
        Get the last name of the student.

        Returns:
            str: The last name of the student.
        """
        return self._last_name

    def get_email(self):
        """
        Get the email address of the student.

        Returns:
            str: The email address of the student.
        """
        return self._email

    def get_phone_number(self):
        """
        Get the phone number of the student.

        Returns:
            str: The phone number of the student.
        """
        return self._phone_number

    # Setter methods
    def set_student_id(self, student_id):
        """
        Set the student's unique identifier.

        Args:
            student_id (int): The new student ID.
        """
        self._student_id = student_id

    def set_first_name(self, first_name):
        """
        Set the first name of the student.

        Args:
            first_name (str): The new first name.
        """
        self._first_name = first_name

    def set_last_name(self, last_name):
        """
        Set the last name of the student.

        Args:
            last_name (str): The new last name.
        """
        self._last_name = last_name

    def set_email(self, email):
        """
        Set the email address of the student.

        Args:
            email (str): The new email address.
        """
        self._email = email

    def set_phone_number(self, phone_number):
        """
        Set the phone number of the student.

        Args:
            phone_number (str): The new phone number.
        """
        self._phone_number = phone_number

    def __str__(self):
        """
        Get a string representation of the student object.

        Returns:
            str: A string containing student information.
        """
        return f"Student ID: {self._student_id}\nName: {self._first_name} {self._last_name}\nEmail: {self._email}\nPhone Number: {self._phone_number}"

if __name__ == "__main__":
    # Code for testing the Student class
    student1 = Student(1, "John", "Doe", "john.doe@example.com", "123-456-7890")
    print(student1)
