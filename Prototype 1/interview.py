class Interview:
    """
    Private class for representing Interview information.

    Attributes:
        __date (date): The interview date.
        __time (time): The interview time.
        __location (str): The interview location.
        __feedback (str): The optional feedback a president can add to the interview record.
        __status (str): The status of the interview..
    """
    
    """ class-level attributes with double underscores to enforce encapsulation and make attributes private """

    __date = None
    __time = None
    __location = None
    __feedback = None
    __status = None