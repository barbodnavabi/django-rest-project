from django.urls import path, include
from .views import BlogList,BlogDetail

app_name = "api"

urlpatterns = [
    path("list", BlogList.as_view(), name="blog_list"),
    path("article/<int:pk>/", BlogDetail.as_view(), name="article_detail"),
]

