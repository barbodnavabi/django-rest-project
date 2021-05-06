from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from Blog.models import Article
from .serializers import BlogSerializer
from django.contrib.auth.models import User


class BlogList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
