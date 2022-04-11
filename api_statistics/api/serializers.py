from datetime import datetime

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
        try:
            return data.cost / data.clicks
        except ZeroDivisionError:
            return 'На 0 делить нельзя'

    def get_cpm(self, data):
        try:
            return data.cost / data.views * 1000
        except ZeroDivisionError:
            return 'На 0 делить нельзя'

    def validate_date(self, value):
        now = datetime.now().date()
        if value > now:
            raise serializers.ValidationError('Такая дата еще не наступила')
        return value

    def validate_clicks(self, value):
        if value <= -1:
            raise serializers.ValidationError(
                'Проверьте введенное значение количества кликов, '
                'оно не может быть отрицательным')
        return value

    def validate_cost(self, value):
        if value <= -1:
            raise serializers.ValidationError(
                'Проверьте введенное значение стоимости кликов, '
                'оно не может быть отрицательным')
        return value

    def validate_views(self, value):
        if value <= -1:
            raise serializers.ValidationError(
                'Проверьте введенное значение количества показов, '
                'оно не может быть отрицательным')
        return value
