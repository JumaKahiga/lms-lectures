from sqlalchemy.dialects.postgresql import JSON

from app.models import db


class Lecture(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    reviews = db.relationship('Review', backref='lecture_reviews', lazy=True)
    thumbnail_url = db.Column(db.String())
    type = db.Column(db.String(), nullable=False)
    excerpt = db.Column(db.Text(), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=db.func.now())
    pdf_download_url = db.Column(db.String())
    slug = db.Column(db.String(), nullable=False)
    tags = db.Column(JSON)
    author = db.Column(
        db.Integer, db.ForeignKey('person_user.id'), nullable=False)
    content = db.Column(db.Text())
    transcript = db.Column(db.Text())
    title = db.Column(db.String(), nullable=False)
    video_url = db.Column(db.String())

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class Review(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    added_at = db.Column(db.DateTime, default=db.func.now())
    user = db.Column(
        db.Integer, db.ForeignKey('person_user.id'), nullable=False)
    text = db.Column(db.Text())
    rating = db.Column(db.Integer())
    reviewed_lecture = db.Column(
        db.Integer, db.ForeignKey('lecture.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
