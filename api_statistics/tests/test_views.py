from api.models import Statistics
from rest_framework import status
from rest_framework.test import APITestCase


class Tests(APITestCase):
    def test_create_object(self):
        """
        Проверка создания объекта
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

    def test_delete_object(self):
        """
        Проверка удаления объекта
        """
        data = {
            'date': '2020-11-11',
            'views': '10000',
            'clicks': '5000',
            'cost': '1000'
        }
        request = self.client.post('/statistics/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Statistics.objects.count(), 1)
        self.client.delete('/statistics/delete/')
        self.assertEqual(Statistics.objects.count(), 0)

    def test_incorrect_date(self):
        """
        Проверка получения ошибки при вводе неверной даты в GET запросе
        """
        response = self.client.get('/statistics/?from=2020&to=2020-11-13')
        self.assertEqual(response.data['detail'],
                         'Неверный формат даты начала периода, '
                         'формат должен быть YYYY-MM-DD'
                         )
