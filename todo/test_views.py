from django.test import TestCase

# Create your tests here.


class TestDjango(TestCase):
    # 'self' here refers to TestDjango class


    def test_this_thing_work(self):
        self.assertEqual(1, 0)