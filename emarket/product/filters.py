import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    # min_price = 

    class Meta:
        model = Product
        fields = ['price', 'category']