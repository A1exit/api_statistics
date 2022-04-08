from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности адреса /statistics/"""
        response = self.guest_client.get('/statistics/')
        self.assertEqual(response.status_code, 200)
