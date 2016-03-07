from flask import Flask
from flask import render_template
from seatmap import SeatMap

CLASSROOM_WIDTH = 19
CLASSROOM_HEIGHT = 9

app = Flask(__name__)
seatmap = SeatMap(CLASSROOM_WIDTH, CLASSROOM_HEIGHT)
# seatmap.get_seat(2, 3).set_shadowed()


def format_seat_map(seatmap):
    myMap = []
    for y in range(CLASSROOM_HEIGHT):
        row = []
        for x in range(CLASSROOM_WIDTH):
            seat1 = {}
            seat2 = seatmap.get_seat(x, y)
            if seat2.is_shadowed():
                seat1['shadowed'] = 1
            else:
                seat1['shadowed'] = 0
                seat1['best'] = seat2.get_best_choice_list()
                seat1['soso'] = seat2.get_soso_choice_list()
            row.append(seat1)
        myMap.append(row)
    return myMap


@app.route('/')
def hello_world():
    global seatmap
    sm = format_seat_map(seatmap)
    return render_template('app.html', seatmap=sm)


if __name__ == '__main__':
    app.run()
