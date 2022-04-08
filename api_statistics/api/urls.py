from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import StatisticsViewSet, delete

router = SimpleRouter()

router.register('statistics', StatisticsViewSet, basename='statistics')

urlpatterns = [
    path('statistics/delete/', delete),
    path('', include(router.urls)),
]
