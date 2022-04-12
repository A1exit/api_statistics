from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_url(self):
        """ Checking address availability /statistics/"""
        response = self.guest_client.get('/statistics/?from=2020-11-11&'
                                         'to=2020-11-23')
        self.assertEqual(response.status_code, 200)
