import django_filters
from .models import Stocks

class StocksFilter(django_filters.FilterSet):
    class Meta:
        model = Stocks
        fields = ['item_name']
