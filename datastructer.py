#
# datastructer.py
# Create by hexapetalous on Mar 8, 2016.
#
# Copyright
#
from seatmap import SeatMap


class DataStructer(object):
    CLASSROOM_HEIGHT = 9
    CLASSROOM_WIDTH = 19
    singleton = None

    def __init__(self):
        super(DataStructer, self).__init__()
        self.seat_map = SeatMap(DataStructer.CLASSROOM_WIDTH,
                                DataStructer.CLASSROOM_HEIGHT)
        DataStructer.singleton = self

    def formatted_seat_map(self):
        my_map = []
        for y in range(DataStructer.CLASSROOM_HEIGHT):
            row = []
            for x in range(DataStructer.CLASSROOM_WIDTH):
                seat1 = {}
                seat2 = self.seat_map.get_seat(x, y)
                if seat2.is_shadowed():
                    seat1['shadowed'] = 1
                else:
                    seat1['shadowed'] = 0
                    seat1['x'] = x
                    seat1['y'] = y
                    seat1['best'] = seat2.get_best_choice_list()
                    seat1['soso'] = seat2.get_soso_choice_list()
                row.append(seat1)
            my_map.append(row)
        return my_map

    def get_seat_map(self):
        return self.seat_map

    @staticmethod
    def get_data_structer():
        if DataStructer.singleton:
            return DataStructer.singleton
        else:
            return DataStructer()
