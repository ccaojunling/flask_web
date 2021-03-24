import uuid
from flask import Flask, request, json, Response
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(16), nullable=False)
    def __repr__(self):
        return '<userinfo:{}>'.format(self.username)


def check_user(username, password):
    art=User.query.filter(User.username==username, User.password==password).first()
    if art is None:
        return False
    return True


def insert_user(username, password):
    try:
        user_info=User(username=username, password=password)
        db.session.add(user_info)
        result = db.session.commit()
    except:
        return False
    else:
        return True

        


if __name__ == '__main__':
    a = insert_user(123456,123)
    print (a)
# db.create_all()

# print (art)
# abc=User(username='1234', password='123')
# db.session.add(abc)
# db.session.commit()