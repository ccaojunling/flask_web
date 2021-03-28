from flask import Flask, render_template, redirect, url_for, jsonify
from flask import request

from database_msql import check_user, insert_user, app


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    template = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            if request.form["role"] == '0':
                template = render_template('index.html')
            else:
                response_data = {
                    "code": 200,
                    "message": "成功",
                    "username": request.form['username'],
                    "password": request.form['password'],
                }
                template = jsonify(response_data)
        else:
            if request.form["role"] == '0':
                template = render_template('login.html')
            else:
                response_data = {
                    "code": -100,
                    "message": "失败",
                    "username": request.form['username'],
                    "password": request.form['password'],
                }
                template = jsonify(response_data)
    else:
        template = render_template('login.html')
    return template






@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        status = insert_user(request.form['username'], request.form['password'])
        if status:
            return redirect(url_for('login'))
        else:
            return render_template('register.html')
    else:
        return render_template('register.html')


def valid_login(username, password):
    status = check_user(username, password)
    return status


if __name__ == '__main__':
    app.run()

