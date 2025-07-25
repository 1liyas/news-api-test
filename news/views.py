from rest_framework import viewsets, filters
from .models import News
from .serializers import NewsSerializer
from django_filters.rest_framework import DjangoFilterBackend

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['category__name', 'tags__name']
