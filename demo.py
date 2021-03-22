from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return render_template('index.html')
        return render_template('login.html')
    else:
        return render_template('login.html')


def valid_login(username, password):
    return True



