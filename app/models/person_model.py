from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declared_attr
from werkzeug.security import generate_password_hash, check_password_hash


from app.models import db
from app.models.lectures_model import Lecture, Review


class Person(db.Model):
    __abstract__ = True

    name = db.Column(db.String(75))
    email = db.Column(db.String(75), unique=True)
    password_hash = db.Column(db.String(128), default="12345")
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        return self.password_hash

    def authenticate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @declared_attr
    def __tablename__(cls):
        return 'person_' + (cls.__name__).lower()

    def __str__(self):
        return f'{self.email}'

    def __repr__(self):
        return f'<email {self.email}>'


class Admin(Person):
    id = db.Column(db.Integer(), primary_key=True)
    is_admin = db.Column(db.Boolean(), default=True)


class User(Person):
    id = db.Column(db.Integer(), primary_key=True)
    is_author = db.Column(db.Boolean(), default=False)
    bio = db.Column(db.Text())
    company = db.Column(db.String())
    avatar_url = db.Column(db.String())
    social_urls = db.Column(JSON)
    lectures = db.relationship(Lecture, backref='author_lectures', lazy=True)
    reviews = db.relationship(Review, backref='user_reviews', lazy=True)
