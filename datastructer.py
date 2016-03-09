# coding=utf-8
#
# datastructer.py
# Create by hexapetalous on Mar 8, 2016.
#
# Copyright
#
from seat import Seat


class DataStructer(object):
    CLASSROOM_HEIGHT = 9
    CLASSROOM_WIDTH = 19
    singleton = None

    def __init__(self):
        super(DataStructer, self).__init__()
        self.seat_map = DataStructer.init_seat_map(
            DataStructer.CLASSROOM_HEIGHT, DataStructer.CLASSROOM_WIDTH)
        DataStructer.singleton = self

    def formatted_seat_map(self):
        my_map = []
        for y in range(DataStructer.CLASSROOM_HEIGHT):
            row = []
            for x in range(DataStructer.CLASSROOM_WIDTH):
                seat1 = {}
                seat2 = self.seat_map[y][x]
                if seat2.is_shadowed():
                    seat1['shadowed'] = 1
                else:
                    seat1['shadowed'] = 0
                    seat1['x'] = x
                    seat1['y'] = y

                    def list2str(l):
                        if l:
                            return u'%3s 等%2d人' % (l[0], len(l))
                        else:
                            return u'..........'
                    seat1['best'] = list2str(seat2.get_best_choice_list())
                    seat1['soso'] = list2str(seat2.get_soso_choice_list())
                row.append(seat1)
            my_map.append(row)
        return my_map

    def add_best_choice(self, x, y, name):
        self.seat_map[y][x].add_best_choice(name)
        return True

    def add_soso_choice(self, x, y, name):
        self.seat_map[y][x].add_soso_choice(name)
        return True

    @staticmethod
    def get_data_structer():
        if DataStructer.singleton:
            return DataStructer.singleton
        else:
            return DataStructer()

    @staticmethod
    def init_seat_map(height, width):
        my_map = []
        for y in range(height):
            row = []
            for x in range(width):
                seat = Seat(x, y)
                row.append(seat)
            my_map.append(row)
        return my_map
