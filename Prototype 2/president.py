from mccTeamMember import MccTeamMember

class President(MccTeamMember):
    """
    Private class for representing President information.

    Attributes:
        __ID (int): The unique identifier of the object; autoincremented.
    """

    id_count = 0

    def __init__(self, student):
        President.id_count += 1
        self.__ID = President.id_count

        super().__init__(student.get_student_id(), student.get_first_name(), student.get_last_name(), student.get_email(), student.get_phone_number())
        
    def get_id(self):
        return self.__ID