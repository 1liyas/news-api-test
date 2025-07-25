import django_filters
from .models import News

class NewsFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name="category__id")
    tags = django_filters.AllValuesMultipleFilter(field_name="tags__id")
    is_published = django_filters.BooleanFilter()

    class Meta:
        model = News
        fields = ['category', 'tags', 'is_published']
