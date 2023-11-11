class Submission:
    """
    Private class for representing Submission information.

    Attributes:
        __studentID (int): The unique identifier for the student.
        __selectedPositionID (int): The unique identifier for the selected position.
        __experience (str): The experience of the student relative to the position.
        __dateSubmitted (date): The date of when the submission was submitted by the student.
    """
    
    def __init__(self, student_id, selected_position_id, experience, date_submitted):
        self.__studentID = student_id
        self.__selectedPositionID = selected_position_id
        self.__experience = experience
        self.__dateSubmitted = date_submitted

    def get_student_id(self):
        return self.__studentID

    def set_student_id(self, student_id):
        self.__studentID = student_id

    def get_selected_position_id(self):
        return self.__selectedPositionID

    def set_selected_position_id(self, selected_position_id):
        self.__selectedPositionID = selected_position_id

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def get_date_submitted(self):
        return self.__dateSubmitted

    def set_date_submitted(self, date_submitted):
        self.__dateSubmitted = date_submitted
