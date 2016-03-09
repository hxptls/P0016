from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
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
    if x < 0 or y < 0 or not name:
        return 'fail'
    if seat_type == 'b':
        ds = DataStructer.get_data_structer()
        ds.add_best_choice(x, y, name)
        return 'ok'
    elif seat_type == 's':
        ds = DataStructer.get_data_structer()
        ds.add_soso_choice(x, y, name)
        return 'ok'
    else:
        return 'fail'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
