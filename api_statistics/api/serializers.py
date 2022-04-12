from datetime import datetime

from rest_framework import serializers

from .models import Statistics


class ViewStatisticsSerializer(serializers.Serializer):
    start = serializers.DateField()
    stop = serializers.DateField()


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
        try:
            return data.cost / data.clicks
        except ZeroDivisionError:
            return 'It cannot be divided by 0'

    def get_cpm(self, data):
        try:
            return data.cost / data.views * 1000
        except ZeroDivisionError:
            return 'It cannot be divided by 0'

    def validate_date(self, value):
        now = datetime.now().date()
        if value > now:
            raise serializers.ValidationError('such a date has not yet come')
        return value

    def validate_clicks(self, value):
        if value <= -1:
            raise serializers.ValidationError(
                'clicks cannot be negative')
        return value

    def validate_cost(self, value):
        if value <= -1:
            raise serializers.ValidationError(
                'cost cannot be negative')
        return value

    def validate_views(self, value):
        if value <= -1:
            raise serializers.ValidationError(
                'views cannot be negative')
        return value
