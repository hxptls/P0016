#
# seatmap.py
# Created by hexapetalous on Mar 7, 2016.
#
# Copyright
#

# SOMETHING IMPORTANT
#  <-----x/w----->
#  ^     0 1 2 3 4
#  |   0
# y/h  1
#  |   2
#  |   3
#  v   4


class Seat(object):
    """

    """

    def __init__(self, x, y):
        super(Seat, self).__init__()
        self.x = x
        self.y = y
        self.bestChoice = []
        self.sosoChoice = []
        self.shadowed = False

    def add_best_choice(self, name):
        self.bestChoice.append(name)

    def get_best_choice_list(self):
        return self.bestChoice

    def add_soso_choice(self, name):
        self.sosoChoice.append(name)

    def get_soso_choice_list(self):
        return self.sosoChoice

    def set_shadowed(self):
        self.shadowed = True

    def is_shadowed(self):
        return self.shadowed

    def clean(self):
        self.bestChoice = []
        self.sosoChoice = []


class SeatMap(object):
    """

    """

    def __init__(self, width, height):
        super(SeatMap, self).__init__()
        self.width = width
        self.height = height
        self.map = []
        # (y, x) is for easy display on web.
        for y in range(height):
            row = []
            for x in range(width):
                seat = Seat(x, y)
                row.append(seat)
            self.map.append(row)

    '''
    def add_shadowed_seat(self, x, y):
        seat = self.map[y][x]
        seat.set_shadowed()

    def add_best_choice(self, x, y, name):
        seat = self.map[y][x]
        seat.add_best_choice(name)

    def add_soso_choice(self, x, y, name):
        seat = self.map[y][x]
        seat.add_soso_choice(name)

    def get_best_choice(self, x, y):
        seat = self.map[y][x]
        return seat.get_best_choice_list()

    def get_soso_choice(self, x, y):
        seat = self.map[y][x]
        return seat.get_soso_choice_list()
    '''

    def get_seat(self, x, y):
        return self.map[y][x]

    def clean(self):
        for y in range(self.height):
            for x in range(self.width):
                seat = self.map[y][x]
                seat.clean()
