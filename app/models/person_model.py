from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declared_attr
from werkzeug.security import generate_password_hash, check_password_hash


from app import db
from app.models.lectures_model import Lecture, Review


class Person(db.Model):
    __abstract__ = True

    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(75), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def authenticate_password(self, password):
        return check_password_hash(self.password_hash, password)

    @declared_attr
    def __tablename__(cls):
        return 'person_' + (cls.__name__).lower()

    def __repr__(self):
        return '<email {}>'.format(self.email)


class Admin(Person):
    id = db.Column(db.Integer(), primary_key=True)
    is_admin = db.Column(db.Boolean(), default=True)


class User(Person):
    id = db.Column(db.Integer(), primary_key=True)
    is_author = db.Column(db.Boolean(), default=False)
    bio = db.Column(db.Text())
    company = db.Column(db.String(128))
    avatar_url = db.Column(db.String())
    social_urls = db.Column(JSON)
    lectures = db.relationship(Lecture, backref='author_lectures', lazy=True)
    reviews = db.relationship(Review, backref='user_reviews', lazy=True)
