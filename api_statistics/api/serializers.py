from rest_framework import serializers

from .models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = Statistics
        fields = (
            'date',
            'views',
            'clicks',
            'cost',
            'cpc',
            'cpm',
        )

    def get_cpc(self, data):
        return data.cost / data.clicks

    def get_cpm(self, data):
        return data.cost / data.views * 1000
