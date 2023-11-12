class Offer:
    """
    Private class for representing Offer information.

    Attributes:
        __ID (int): The unique identifier of the object; autoincremented.
        __details (str): The details of the offer.
        __candidateID (int): The unique identifier of the candidate receiving the offer.
        __positionID (int): The unique identifier of the position being offered.
    """

    id_count = 0
    
    def __init__(self, details, candidate_id, position_id):
        Offer.id_count += 1
        self.__ID = Offer.id_count
        self.__details = details
        self.__candidateID = candidate_id
        self.__positionID = position_id

    def get_id(self):
        return self.__ID

    def get_details(self):
        return self.__details

    def set_details(self, details):
        self.__details = details

    def get_candidate_id(self):
        return self.__candidateID

    def set_candidate_id(self, candidate_id):
        self.__candidateID = candidate_id

    def get_position_id(self):
        return self.__positionID

    def set_position_id(self, position_id):
        self.__positionID = position_id
