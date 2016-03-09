#
# seat.py
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
