from flask import Flask, render_template, redirect, url_for
from flask import request

from database_msql import check_user, insert_user, app


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'], request.form['password'])
        print(valid_login(request.form['username'], request.form['password']))
        if valid_login(request.form['username'], request.form['password']):
            return render_template('index.html')
        return render_template('login.html')
    else:
        return render_template('login.html')


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

