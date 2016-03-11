# coding=utf-8
#
# datastructer.py
# Create by hexapetalous on Mar 8, 2016.
#
# Copyright
#
from seat import Seat
import json


class DataStructer(object):
    CLASSROOM_HEIGHT = 9
    CLASSROOM_WIDTH = 19
    singleton = None

    def __init__(self):
        super(DataStructer, self).__init__()
        self.system_status = None
        self.lesson_info = {}
        self.system_info = {}
        self.final_result = None
        self.seat_map = DataStructer.init_seat_map(
            DataStructer.CLASSROOM_HEIGHT, DataStructer.CLASSROOM_WIDTH)
        self.init_shadowed_seats()
        self.init_prepare_data()
        self.user_table = {}
        DataStructer.singleton = self

    def formatted_seat_map(self):
        my_map = []
        for y in range(DataStructer.CLASSROOM_HEIGHT):
            row = []
            for x in range(DataStructer.CLASSROOM_WIDTH):
                seat1 = {}
                seat2 = self.seat_map[y][x]
                if seat2.is_shadowed():
                    seat1['shadowed'] = True
                else:
                    seat1['shadowed'] = False
                    seat1['x'] = x
                    seat1['y'] = y

                    def list2str(l):
                        if l:
                            return u'%3s 等%2d人' % (l[0], len(l))
                        else:
                            return u' '
                    seat1['best'] = list2str(seat2.get_best_choice_list())
                    seat1['soso'] = list2str(seat2.get_soso_choice_list())
                row.append(seat1)
            my_map.append(row)
        return my_map

    def add_choice(self, x, y, name):
        if name in self.user_table:
            if self.user_table[name] == 4:
                return False
            self.user_table[name] += 1
            if self.add_soso_choice(x, y, name):
                return 'soso'
            else:
                return False
        self.user_table[name] = 1
        if self.add_best_choice(x, y, name):
            return 'best'
        else:
            return False

    def update_choice(self, x, y, name):
        seat = self.seat_map[y][x]
        if name in seat.get_best_choice_list():
            seat.delete_best_choice(name)
            self.user_table[name]['best'] = 0
            return True, 'delete', 'best'
        elif name in seat.get_soso_choice_list():
            seat.delete_soso_choice(name)
            self.user_table[name]['soso'] -= 1
            return True, 'delete', 'soso'

        if name not in self.user_table:
            seat.add_best_choice(name)
            self.user_table[name] = {'best': 0, 'soso': 0}
            self.user_table[name]['best'] = 1
            return True, 'add', 'best'

        if self.user_table[name]['best'] == 0:
            seat.add_best_choice(name)
            self.user_table[name]['best'] = 1
            return True, 'add', 'best'
        if self.user_table[name]['soso'] < 3:
            seat.add_soso_choice(name)
            self.user_table[name]['soso'] += 1
            return True, 'add', 'soso'
        return False, '', ''

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

    def init_shadowed_seats(self):
        for y in range(DataStructer.CLASSROOM_HEIGHT):
            self.seat_map[y][4].set_shadowed()
            self.seat_map[y][-5].set_shadowed()
        self.seat_map[0][0].set_shadowed()
        self.seat_map[0][1].set_shadowed()
        self.seat_map[0][2].set_shadowed()
        self.seat_map[0][3].set_shadowed()
        self.seat_map[0][-1].set_shadowed()
        self.seat_map[0][-2].set_shadowed()
        self.seat_map[0][-3].set_shadowed()
        self.seat_map[0][-4].set_shadowed()
        self.seat_map[1][0].set_shadowed()
        self.seat_map[1][1].set_shadowed()
        # self.seat_map[1][2].set_shadowed()
        self.seat_map[1][-1].set_shadowed()

    def init_prepare_data(self):
        from prepare.lesson_info import lesson_info
        self.lesson_info = lesson_info
        from prepare.system_info import system_info
        self.system_info = system_info
        from prepare.result import result
        self.final_result = result
        self.system_status = lesson_info['status']

    def get_system_status(self):
        return self.system_status

    def get_lesson_info(self):
        return self.lesson_info

    def get_system_info(self):
        return self.system_info

    def get_data_map(self):
        data_map = []
        for x in range(DataStructer.CLASSROOM_WIDTH):
            for y in range(DataStructer.CLASSROOM_HEIGHT):
                seat = self.seat_map[y][x]
                if seat.is_shadowed():
                    continue
                item = {'x': x, 'y': y,
                        'best': seat.get_best_choice_list(),
                        'soso': seat.get_soso_choice_list()}
                data_map.append(item)
        return {'data': data_map}

    def get_formatted_final_map(self):
        my_map = []
        for y in range(DataStructer.CLASSROOM_HEIGHT):
            row = []
            for x in range(DataStructer.CLASSROOM_WIDTH):
                seat = {}
                if self.seat_map[y][x].is_shadowed():
                    seat['shadowed'] = True
                else:
                    seat['shadowed'] = False
                    for item in self.final_result:
                        if item['x'] == x and item['y'] == y:
                            seat['name'] = item['name']
                            break
                row.append(seat)
            my_map.append(row)
        return my_map

    @staticmethod
    def refresh():
        new_singleton = DataStructer()
        DataStructer.singleton = new_singleton
