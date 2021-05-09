from rest_framework import serializers
from Blog.models import Article
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title",'slug','content']
