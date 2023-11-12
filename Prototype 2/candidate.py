from student import Student

class Candidate(Student):
    """
    Private class for representing Candidate information.

    Attributes:
        __ID (int): The unique identifier of the object; autoincremented.
        __submissionID (int): The unique identifier for the student's submission.
        __status (string): The candidate's status
    """

    id_count = 0
    
    def __init__(self, student, submission_id, status="Interview"):
        Candidate.id_count += 1
        self.__ID = Candidate.id_count

        super().__init__(student.get_student_id(), student.get_first_name(), student.get_last_name(), student.get_email(), student.get_phone_number())
        self.__submissionID = submission_id
        self.__status = status

    def get_id(self):
        return self.__ID

    def get_submission_id(self):
        return self.__submissionID

    def set_submission_id(self, submission_id):
        self.__submissionID = submission_id

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status
