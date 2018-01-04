from django.test import TestCase

from ..models import Leave, User


class SafeDeleteFunctionalityCheck(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='robinhood', email='robin@the-wild.com', password='123qwe')
        cls.leave_obj = Leave.objects.create(
            type=Leave.SICK_LEAVE,
            user=cls.user
        )

    def test_latest_works(self):
        Leave.objects.latest('type')
        Leave.objects.latest('pk')

    def test_earliest_works(self):
        Leave.objects.earliest('type')
        Leave.objects.earliest('pk')
