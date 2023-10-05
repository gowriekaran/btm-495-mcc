from candidate import Candidate

class MccTeamMember(Candidate):
    """
    Private class for representing MCC Team Member information.

    Attributes:
        __positionID (int): The unique identifier for the MCC Team Member's position.
    """
    
    """ class-level attributes with double underscores to enforce encapsulation and make attributes private """

    __positionID = None