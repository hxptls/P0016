from flask import Flask
from flask import render_template
from flask import request
from datastructer import DataStructer

app = Flask(__name__)


@app.route('/')
def hello_world():
    ds = DataStructer.get_data_structer()
    sm = ds.formatted_seat_map()
    return render_template('app.html', seatmap=sm)


@app.route('/choose')
def wise_try():
    seat_type = request.args.get('s', '')
    x = int(request.args.get('x', '-1'))
    y = int(request.args.get('y', '-1'))
    name = request.args.get('n', '')
    seat_type_set = {'b', 's'}
    if x < 0 or y < 0 or not name:
        return 'fail'
    if seat_type == 'b':
        ds = DataStructer.get_data_structer()
        ds.get_seat_map().get_seat(x, y).add_best_choice(name)
        return 'ok'
    elif seat_type == 's':
        ds = DataStructer.get_data_structer()
        ds.get_seat_map().get_seat(x, y).add_soso_choice(name)
        return 'ok'
    else:
        return 'fail'


if __name__ == '__main__':
    app.run()
