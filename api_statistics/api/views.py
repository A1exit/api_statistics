import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, filters, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Statistics
from .serializers import StatisticsSerializer, ViewStatisticsSerializer


class StatisticsViewSet(viewsets.ModelViewSet):
    """Allows you to create a record, get a list of records"""
    serializer_class = StatisticsSerializer
    http_method_names = ['get', 'post']
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    ordering_fields = ('date', 'views', 'clicks', 'cost')

    def get_queryset(self):
        start = self.request.query_params.get('from')
        stop = self.request.query_params.get('to')
        data = {'start': start,
                'stop': stop}
        serializer = ViewStatisticsSerializer(data=data)
        if serializer.is_valid():
            return Statistics.objects.filter(
                date__range=[start, stop])
        raise exceptions.ValidationError(
            'The time values are entered incorrectly'
        )


@api_view(['DELETE'])
def delete(request):
    """Deletes all records of the Statistics model"""
    Statistics.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
