class Position:
    """
    Private class for representing Position information.

    Attributes:
        __Name (str): The name of the position.
        __Description (str): The description of the position.
        __Status (str): The status of the position.
    """
    
    def __init__(self, name, description, status):
        self.__Name = name
        self.__Description = description
        self.__Status = status

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
