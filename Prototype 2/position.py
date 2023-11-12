class Position:
    """
    Private class for representing Position information.

    Attributes:
        __ID (int): The unique identifier of the object; autoincremented.
        __Name (str): The name of the position.
        __Description (str): The description of the position.
        __Status (str): The status of the position.
    """

    id_count = 0
    
    def __init__(self, name, description, status="Vacant"):
        Position.id_count += 1
        self.__ID = Position.id_count
        self.__Name = name
        self.__Description = description
        self.__Status = status

    def get_id(self):
        return self.__ID

    def get_name(self):
        return self.__Name

    def set_name(self, name):
        self.__Name = name

    def get_description(self):
        return self.__Description

    def set_description(self, description):
        self.__Description = description

    def get_status(self):
        return self.__Status

    def set_status(self, status):
        self.__Status = status
