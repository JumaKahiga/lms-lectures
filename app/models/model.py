from app import db


class Entity(db.Model):
    __tablename__ = 'entities'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    def __init__(self, first_name):
        self.first_name = first_name

    def __repr__(self):
        return '<name {}>'.format(self.first_name)
