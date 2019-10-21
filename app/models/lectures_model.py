from sqlalchemy.dialects.postgresql import JSON

from app import db


class Lecture(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    reviews = db.relationship('Review', backref='lecture_reviews', lazy=True)
    thumbnail_url = db.Column(db.String())
    type = db.Column(db.String(), nullable=False)
    excerpt = db.Column(db.String(275), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=db.func.now())
    pdf_download_url = db.Column(db.String())
    slug = db.Column(db.String(40), nullable=False)
    tags = db.Column(JSON)
    author = db.Column(
        db.Integer, db.ForeignKey('person_user.id'), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    title = db.Column(db.String(75), nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    added_at = db.Column(db.DateTime, default=db.func.now())
    user = db.Column(
        db.Integer, db.ForeignKey('person_user.id'), nullable=False)
    text = db.Column(db.Text())
    rating = db.Column(db.Integer())
    lecture = db.Column(
        db.Integer, db.ForeignKey('lecture.id'), nullable=False)
