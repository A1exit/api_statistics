import pytest
from api.serializers import StatisticsSerializer


def test_negative_value_views():
    data = {
        'date': '2025-11-11',
        'views': '-10000',
        'clicks': '-5000',
        'cost': '-1000'
    }
    mm = StatisticsSerializer(data=data)

    assert mm.is_valid() == False
    assert mm.errors['views'][0] == 'Проверьте введенное значение ' \
                                    'количества показов, оно не может быть ' \
                                    'отрицательным'
    assert mm.errors['clicks'][0] == 'Проверьте введенное значение ' \
                                     'количества кликов, оно не может быть ' \
                                     'отрицательным'
    assert mm.errors['cost'][0] == 'Проверьте введенное значение ' \
                                   'стоимости кликов, оно не может быть ' \
                                   'отрицательным'
    assert mm.errors['date'][0] == 'Такая дата еще не наступила'


@pytest.mark.django_db(transaction=True)
def test_zero_division_error():
    data = {
        'date': '2021-11-11',
        'views': '0',
        'clicks': '0',
        'cost': '0'
    }
    mm = StatisticsSerializer(data=data)

    assert mm.is_valid() == True
    mm.save()
    assert mm.data['cpc'] == 'На 0 делить нельзя'
