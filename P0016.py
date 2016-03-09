# coding=utf-8
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import session
from flask import redirect
from datastructer import DataStructer
import requests as rq
import time
import hashlib

app = Flask(__name__)
app.secret_key = b'\xc4\xe3\xea\xd7(\xf1\xd0\xe7]\x8c\xfeI\x93\t\xd9\xa8S\x13' \
                 b'\xeeM\x8c\x12\xb6\x9f'


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    ds = DataStructer.get_data_structer()
    if ds.get_system_status() == 'stop boarding':
        return redirect('/final')
    login = {'login': False}
    if 'username' in session:
        login = {'login': True, 'name': session['username']}
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
        username = data['data']['username']
        login = {'login': True, 'name': username}
        session['username'] = username
    sm = ds.formatted_seat_map()
    li = ds.get_lesson_info()
    si = ds.get_system_info()
    return render_template('app.html', seatmap=sm, login=login, lesson=li,
                           system=si)


@app.route('/choose')
def wise_try():
    x = int(request.args.get('x', '-1'))
    y = int(request.args.get('y', '-1'))
    name = request.args.get('n', '')
    if x < 0 or y < 0 or not name:
        return jsonify({'status': -1})
    ds = DataStructer.get_data_structer()
    status, action, my_type = ds.update_choice(x, y, name)
    if not status:
        return jsonify({'status': -2})
    return jsonify({'status': 0, 'type': my_type, 'action': action})


@app.route('/login')
def knock_knock():
    return render_template('login.html')


@app.route('/data')
def i_want_everything():
    ds = DataStructer.get_data_structer()
    return jsonify(ds.get_data_map())


@app.route('/stop')
def bye():
    secret_key = request.args.get('s', '')
    x1 = str(time.time() // 3600)
    x2 = hashlib.md5()
    x2.update(x1)
    if x2.hexdigest() == secret_key:
        pass
        # exit(0)  # Don't work.
    return '你想干什么!'


@app.route('/final')
def do_you_like_it():
    ds = DataStructer.get_data_structer()
    if ds.get_system_status() == 'boarding':
        return redirect('/')
    li = ds.get_lesson_info()
    si = ds.get_system_info()
    rs = ds.get_formatted_final_map()
    return render_template('result.html', result=rs, lesson=li, system=si)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
