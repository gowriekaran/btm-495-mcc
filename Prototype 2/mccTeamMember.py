from student import Student

class MccTeamMember(Student):
    """
    Private class for representing MCC Team Member information.

    Attributes:
        __positionID (int): The unique identifier for the MCC Team Member's position.
    """
    
    def __init__(self, position_id):
        # To resolve
        super().__init__(submission_id)
        self.__positionID = position_id

    def get_position_id(self):
        return self.__positionID

    def set_position_id(self, position_id):
        self.__positionID = position_id
