from student import Student

class MccTeamMember(Student):
    """
    Private class for representing MCC Team Member information.

    Attributes:
        __ID (int): The unique identifier of the object; autoincremented.
        __positionID (int): The unique identifier for the MCC Team Member's position.
    """

    id_count = 0
    
    def __init__(self, student, position_id):
        MccTeamMember.id_count += 1
        self.__ID = MccTeamMember.id_count

        super().__init__(student.get_student_id(), student.get_first_name(), student.get_last_name(), student.get_email(), student.get_phone_number())
        self.__positionID = position_id

    def get_id(self):
        return self.__ID

    def get_position_id(self):
        return self.__positionID

    def set_position_id(self, position_id):
        self.__positionID = position_id
