from api.models import Statistics
from rest_framework import status
from rest_framework.test import APITestCase


class Tests(APITestCase):
    def test_create_object(self):
        """
        Checking the creation of an object
        """
        data = {
            'date': '2020-11-11',
            'views': '10000',
            'clicks': '5000',
            'cost': '1000'
        }
        response = self.client.post('/statistics/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Statistics.objects.count(), 1)
        self.assertEqual(Statistics.objects.get().views, 10000)
        self.assertEqual(Statistics.objects.get().clicks, 5000)
        self.assertEqual(Statistics.objects.get().cost, 1000.0)
        self.client.delete('/statistics/delete/')
        self.assertEqual(Statistics.objects.count(), 0)

    def test_incorrect_date(self):
        """
        Checking for an error when entering an incorrect date in a GET request
        """
        response = self.client.get('/statistics/?from=2020&to=2020-11-13')
        self.assertEqual(response.data['detail'],
                         'Invalid format of the start date of the period, the '
                         'format should be YYYY-MM-DD'
                         )
