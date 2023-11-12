class Student:
    """
    Private class for representing Student information.

    Attributes:
        __ID (int): The unique identifier of the object; autoincremented.
        __studentID (int): The unique identifier for the student.
        __firstName (str): The first name of the student.
        __lastName (str): The last name of the student.
        __email (str): The email address of the student.
        __phoneNumber (int): The phone number of the student.
    """

    id_count = 0
    
    def __init__(self, student_id, first_name, last_name, email, phone_number):
        Student.id_count += 1
        self.__ID = Student.id_count
        self.__studentID = student_id
        self.__firstName = first_name
        self.__lastName = last_name
        self.__email = email
        self.__phoneNumber = phone_number

    def get_id(self):
        return self.__ID

    def get_student_id(self):
        return self.__studentID

    def set_student_id(self, student_id):
        self.__studentID = student_id

    def get_first_name(self):
        return self.__firstName

    def set_first_name(self, first_name):
        self.__firstName = first_name

    def get_last_name(self):
        return self.__lastName

    def set_last_name(self, last_name):
        self.__lastName = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phoneNumber

    def set_phone_number(self, phone_number):
        self.__phoneNumber = phone_number
