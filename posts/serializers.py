from rest_framework import serializers
from users.serializers import ProfileSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)  # nested serializer

    class Meta:
        model = Post
        fields = (
            "pk",
            "profile",
            "title",
            "body",
            "image",
            "published_date",
            "like",
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "category",
            "body",
            "image",
        )
        
    
