from django.urls import path, include,re_path
from rest_framework import routers
from .views import BlogViewSet

app_name = "api"


router = routers.SimpleRouter()
router.register('blog',BlogViewSet)

urlpatterns = [
    # path("list", BlogList.as_view(), name="blog_list"),
    # path("article/<int:pk>/", BlogDetail.as_view(), name="article_detail"),
    path('',include(router.urls))

]

