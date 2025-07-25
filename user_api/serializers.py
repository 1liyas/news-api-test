from rest_framework import serializers
from news.models import News

class UserNewsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = News
        fields = [
            'id', 'title', 'content', 'slug',
            'created_at', 'category', 'tags'
        ]
