from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from Blog.models import Article
from .serializers import BlogSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class BlogList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]


class BlogDetail(RetrieveAPIView):
    model=Article
    serializer_class = BlogSerializer
    def get_object(self):
        pk=self.kwargs['pk']
        return get_object_or_404(Article,pk=pk)