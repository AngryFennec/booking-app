class BookingItem:
    """Class for single booking item"""
    def __init__(self, name, phone, visit_date, start_time, period, table):
        self.__name = name
        self.__phone = phone
        self.__visit_date = visit_date
        self.__start_time = start_time
        self.__period = period
        self.__table = table

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone

    @property
    def visit_date(self):
        return self.__visit_date

    @visit_date.setter
    def visit_date(self, new_visit_date):
        self.__visit_date = new_visit_date

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, new_start_time):
        self.__start_time = new_start_time

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, new_period):
        self.__period = new_period

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, new_table):
        self.__table = new_table

