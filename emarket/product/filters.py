import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    min_price = django_filters.filters.NumberFilter(field_name ='price', lookup_expr= 'gte')
    max_price = django_filters.filters.NumberFilter(field_name ='price', lookup_expr= 'lte')
    class Meta:
        model = Product
        fields = ['price', 'category']