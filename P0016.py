# coding=utf-8
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from datastructer import DataStructer
import requests as rq

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    login = {'login': False}
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        url = 'https://account.tiaozhan.com/api/xjtucas/ajaxLogin'
        dic = {'netid': username, 'pwd': password, 'get_basic_info': 1}
        ret = rq.post(url, data=dic)
        if ret.status_code != rq.codes.ok:
            return u'登录失败.<a href="/login">点击</a>重试.'
        data = ret.json()
        if data['state'] != 0:
            return u'密码错误.<a href="/login">点击</a>重试.'
        cl = data['data']['class']
        if cl not in (u'少年班41', u'少年班42', u'少年班43', u'少年班44'):
            return u'你不是我们班的,不要企图浑水摸鱼!'
        login = {'login': True, 'name': data['data']['username']}
    ds = DataStructer.get_data_structer()
    sm = ds.formatted_seat_map()
    return render_template('app.html', seatmap=sm, login=login)


@app.route('/choose')
def wise_try():
    x = int(request.args.get('x', '-1'))
    y = int(request.args.get('y', '-1'))
    name = request.args.get('n', '')
    if x < 0 or y < 0 or not name:
        return jsonify({'status': -1})
    ds = DataStructer.get_data_structer()
    success = ds.add_choice(x, y, name)
    if not success:
        return jsonify({'status': -2})
    return jsonify({'status': 0, 'type': success})


@app.route('/login')
def knock_knock():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
