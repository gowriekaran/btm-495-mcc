from student import Student

class Candidate(Student):
    """
    Private class for representing student information.

    Attributes:
        __submissionID (int): The unique identifier for the student's submission.
        __offerID (str): The unique identifier of the offer given to the president, if exists.
    """
    
    """ class-level attributes with double underscores to enforce encapsulation and make attributes private """

    __submissionID = None
    __offerID = None