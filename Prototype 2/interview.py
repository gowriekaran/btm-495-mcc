class Interview:
    """
    Private class for representing Interview information.

    Attributes:
        __date (date): The interview date.
        __time (time): The interview time.
        __location (str): The interview location.
        __feedback (str): The optional feedback a president can add to the interview record.
        __status (str): The status of the interview.
    """
    
    def __init__(self, date, time, location):
        self.__date = date
        self.__time = time
        self.__location = location
        self.__status = "Not Started"
        self.__feedback = ""

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_feedback(self):
        return self.__feedback

    def set_feedback(self, feedback):
        self.__feedback = feedback
