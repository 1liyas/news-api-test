from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction
from django.core.cache import cache

from news.models import News, Category, Tag
from .serializers import NewsAdminSerializer, CategorySerializer, TagSerializer, NewsSerializer
from news.filters import NewsFilter


# Пользовательская авторизация с токеном
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })


# Пользовательский ViewSet для новостей
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = NewsFilter
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        cache.delete("user_news_list")

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("user_news_list")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("user_news_list")


# Админский ViewSet для новостей
class NewsAdminViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsAdminSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title', 'is_published']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        cache.delete("user_news_list")

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("user_news_list")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("user_news_list")


# Админский ViewSet для категорий
class CategoryAdminViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        data = request.data
        many = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TagAdminViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer