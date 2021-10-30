class Table:
    def __init__(self, name, seats, free_seats, checked=False, free=True):
        self.name = name
        self.seats = seats
        self.free_seats = free_seats
        self.checked = checked
        self.free = free
