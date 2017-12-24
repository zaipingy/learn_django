from django.test import TestCase

# Create your tests here.
from myapp.models import Guest, Event

class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name='test1', status=True, limit=20,
                             address='NanJing', start_time='2017-12-23')
        Guest.objects.create(id=1, event_id=1, realname='guest_name', phone='123456',
                             email='test@qq.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='test1')
        self.assertEqual(result.address, 'NanJing')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(realname='guest_name')
        self.assertEqual(result.phone, '123456')
        self.assertFalse(result.sign)