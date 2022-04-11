import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, filters, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Statistics
from .serializers import StatisticsSerializer


class StatisticsViewSet(viewsets.ModelViewSet):
    """Позволяет создать запись, получить список записей"""
    serializer_class = StatisticsSerializer
    http_method_names = ['get', 'post']
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering_fields = ('date', 'views', 'clicks', 'cost')

    def get_queryset(self):
        start = self.request.query_params.get('from', None)
        stop = self.request.query_params.get('to', None)
        if start:
            if stop:
                try:
                    datetime.datetime.strptime(stop, '%Y-%m-%d')
                    try:
                        datetime.datetime.strptime(start, '%Y-%m-%d')
                        return Statistics.objects.filter(
                            date__range=[start, stop])
                    except ValueError:
                        raise exceptions.ParseError(
                            'Неверный формат даты начала периода, '
                            'формат должен быть YYYY-MM-DD'
                        )
                except ValueError:
                    raise exceptions.ParseError(
                        'Неверный формат даты окончания периода, '
                        'формат должен быть YYYY-MM-DD'
                    )
            raise exceptions.ParseError('Введите дату окончания периода')
        raise exceptions.ParseError('Введите дату начала периода')


@api_view(['DELETE'])
def delete(request):
    """Удаляет все записи модели Statistics"""
    Statistics.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
