from django_filters import rest_framework as filters
from admin_api.models import News

class NewsAdminFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    is_published = filters.BooleanFilter()

    class Meta:
        model = News
        fields = ['title', 'is_published']
