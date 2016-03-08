from flask import Flask
from flask import render_template
from datastructer import DataStructer

app = Flask(__name__)


@app.route('/')
def hello_world():
    ds = DataStructer.get_data_structer()
    sm = ds.formatted_seat_map()
    return render_template('app.html', seatmap=sm)


if __name__ == '__main__':
    app.run()
