from student import Student

class Candidate(Student):
    """
    Private class for representing Candidate information.

    Attributes:
        __submissionID (int): The unique identifier for the student's submission.
        __status (string): The candidate's status
    """
    
    def __init__(self, submission_id):
        # To resolve
        super().__init__()
        self.__submissionID = submission_id
        self.__status = "Interview"

    def get_submission_id(self):
        return self.__submissionID

    def set_submission_id(self, submission_id):
        self.__submissionID = submission_id

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
