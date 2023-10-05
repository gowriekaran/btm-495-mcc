class Student:
    """
    Private class for representing Student information.

    Attributes:
        __studentID (int): The unique identifier for the student.
        __firstName (str): The first name of the student.
        __lastName (str): The last name of the student.
        __email (str): The email address of the student.
        __phoneNumber (int): The phone number of the student.
    """
    
    """ class-level attributes with double underscores to enforce encapsulation and make attributes private """

    __studentID = None
    __firstName = None
    __lastName = None
    __email = None
    __phoneNumber = None