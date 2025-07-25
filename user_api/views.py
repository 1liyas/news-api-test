from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from news.models import News
from .serializers import UserNewsSerializer

class NewsListAPIView(APIView):
    def get(self, request):
        cached_data = cache.get("user_news_list")
        if cached_data:
            return Response(cached_data)

        queryset = News.objects.filter(is_published=True).select_related("category").prefetch_related("tags")
        serializer = UserNewsSerializer(queryset, many=True)
        cache.set("user_news_list", serializer.data, timeout=300)  # кэш на 5 минут
        return Response(serializer.data)

class NewsUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(is_published=True).select_related("category").prefetch_related("tags")
    serializer_class = UserNewsSerializer
