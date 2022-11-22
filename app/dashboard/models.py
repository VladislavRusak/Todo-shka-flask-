from email.policy import default
from app import db


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90))
    visibility = db.Column(db.Boolean(default=True))
    # users = db.Column
    addresses = db.relationship('Addrdess', backref='board', lazy='dynamic')


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90))
    board_id = db.ForiengKey()


class Card(db.Model):
    pass
