from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from Blog.models import Article
from .serializers import BlogSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .permissions import IsStaffOrReadOnly,IsAuthorOrReadOnly



# class BlogList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = BlogSerializer
#     permission_classes = [IsAuthenticated]


# class BlogDetail(RetrieveUpdateDestroyAPIView):
#     model=Article
#     serializer_class = BlogSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         pk=self.kwargs['pk']
#         return get_object_or_404(Article,pk=pk)



class BlogViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = BlogSerializer
    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]