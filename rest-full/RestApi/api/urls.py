from django.urls import path, include
from .views import BlogList

app_name = "api"

urlpatterns = [
    path("list", BlogList.as_view(), name="blog_list"),
]

