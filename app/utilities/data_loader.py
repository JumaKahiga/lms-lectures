import os
import json

from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import IntegrityError, DatabaseError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# 'postgresql://postgres@database/lms_db'
engine = create_engine(os.getenv('DATABASE_URL', 'postgresql://postgres@database/lms_db'))
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)

session = Session()

metadata = MetaData()


class DataLoadContextManager:
    def __init__(self, file):
        self.file = file
        self.message = ''

    def __enter__(self):
        data = self.file.read()
        jsondata = json.loads(data)
        lectures = jsondata['lectures']

        count = 0

        for lecture in lectures:
            count += 1

            lecture_table = Base.classes.lecture()
            user_table = Base.classes.person_user()
            review_table = Base.classes.review()

            author = lecture['author']

            user_table = self.add_to_table(user_table, author)
            user_table = self.get_or_create_user(user_table)

            lecture_table = self.add_to_table(lecture_table, lecture)
            lecture_table.author = user_table.id

            if type(lecture_table.author) == int and lecture_table.title:
                self.save_to_db(lecture_table)

            reviews = lecture.get('reviews')

            if lecture_table.id and reviews:
                for review in reviews:
                    user = review.get('user')

                    user_table = Base.classes.person_user()

                    setattr(user_table, 'email', user)

                    user_table = self.get_or_create_user(user_table)

                    review_table = self.add_to_table(review_table, review)

                    review_table.user = user_table.id
                    review_table.reviewed_lecture = lecture_table.id

                    self.save_to_db(review_table)

        self.message = 'Seed data successfully loaded to database'

        return self.message

    def __exit__(self, *args):
        session.close()

    def add_to_table(self, table, data_obj):
        for key, value in data_obj.items():
            setattr(table, key, value)
        return table

    def save_to_db(self, table):
        try:
            session.add(table)
            session.commit()
        except (IntegrityError, DatabaseError) as e:
            self.message = f'Something went wrong, {str(e)}'
            return self.message

    def get_or_create_user(self, table):
        result = None
        if table.email:
            result = session.execute(
                "SELECT id FROM person_user WHERE email='{}'".format(
                    table.email))
            result = result.fetchone()
        elif table.name:
            result = session.execute(
                "SELECT id FROM person_user WHERE name='{}'".format(
                    table.name))
            result = result.fetchone()

        if not result:
            session.add(table)
            session.commit()
        else:
            table.id = result[0]

        return table


# For loading data on the Docker container
if __name__ == '__main__':
    file = open('app/utilities/data.json')
    with DataLoadContextManager(file):
        print('Seed data loaded successfully')
