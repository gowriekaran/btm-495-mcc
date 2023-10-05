class Submission:
    """
    Private class for representing submission information.

    Attributes:
        __studentID (int): The unique identifier for the student.
        __selectedPositionID (int): The unique identifier for the selected position.
        __experience (str): The experience of the student relative to the position.
        __dateSubmitted (date): The date of when the submission was submitted by the student.
    """
    
    """ class-level attributes with double underscores to enforce encapsulation and make attributes private """

    __studentID = None
    __selectedPositionID = None
    __experience = None
    __dateSubmitted = None