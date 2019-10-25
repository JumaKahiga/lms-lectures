from app.tests.factories.lecture_factory import (
    LectureFactory, ReviewFactory)
from app.tests.test_base import BaseTest


class TestLectureModel(BaseTest):
    def setUp(self):
        super(TestLectureModel, self).setUp()
        self.lecture = LectureFactory()

    def test_lecture_has_non_nullable_fields(self):
        self.assertTrue(self.lecture.title)
        self.assertTrue(self.lecture.type)
        self.assertTrue(self.lecture.excerpt)
        self.assertTrue(self.lecture.slug)
        self.assertTrue(self.lecture.author)
        self.assertTrue(self.lecture.content)


class TestReviewModel(BaseTest):
    def setUp(self):
        super(TestReviewModel, self).setUp()
        self.review = ReviewFactory()

    def test_review_has_non_nullable_fields(self):
        self.assertTrue(self.review.reviewed_lecture)
        self.assertTrue(self.review.user)
