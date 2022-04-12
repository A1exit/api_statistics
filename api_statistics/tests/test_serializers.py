import pytest
from api.serializers import StatisticsSerializer


def test_negative_value_views():
    """" checking the creation of an object with negative values """
    data = {
        'date': '2025-11-11',
        'views': '-10000',
        'clicks': '-5000',
        'cost': '-1000'
    }
    mm = StatisticsSerializer(data=data)

    assert mm.is_valid() == False
    assert mm.errors['views'][0] == 'views cannot be negative'
    assert mm.errors['clicks'][0] == 'clicks cannot be negative'
    assert mm.errors['cost'][0] == 'cost cannot be negative'
    assert mm.errors['date'][0] == 'such a date has not yet come'


@pytest.mark.django_db(transaction=True)
def test_zero_division_error():
    """ Checking the error output when dividing by 0 """
    data = {
        'date': '2021-11-11',
        'views': '0',
        'clicks': '0',
        'cost': '0'
    }
    mm = StatisticsSerializer(data=data)

    assert mm.is_valid() == True
    mm.save()
    assert mm.data['cpc'] == 'It cannot be divided by 0'
