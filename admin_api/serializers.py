from rest_framework import serializers
from news.models import News, Category, Tag

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class NewsAdminSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )

    class Meta:
        model = News
        fields = [
            'id', 'title', 'slug', 'content', 'author', 'category',
            'tags', 'created_at', 'updated_at', 'is_published'
        ]

    def to_representation(self, instance):
        """Переопределение для отображения вложенных объектов (read)."""
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        rep['tags'] = TagSerializer(instance.tags.all(), many=True).data
        return rep

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        news = News.objects.create(**validated_data)
        news.tags.set(tags)
        return news

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if tags is not None:
            instance.tags.set(tags)
        return instance
