class Table:
    """Class for table"""
    def __init__(self, name, seats, free_seats, checked=False):
        self.__name = name
        self.__seats = seats
        self.__free_seats = free_seats
        self.__checked = checked

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, new_seats):
        self.__seats = new_seats

    @property
    def free_seats(self):
        return self.__free_seats

    @free_seats.setter
    def free_seats(self, new_free_seats):
        self.__free_seats = new_free_seats

    @property
    def checked(self):
        return self.__checked

    @checked.setter
    def checked(self, new_checked):
        self.__checked = new_checked