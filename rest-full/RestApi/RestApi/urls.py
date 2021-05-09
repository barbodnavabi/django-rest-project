from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework_simplejwt import views as jwt_views
from dj_rest_auth.views import PasswordResetConfirmView
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('api/', include('api.urls')),
    path('rest/auth/', include('dj_rest_auth.urls')),
    path('rest/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^account/confirm/email/(?P<key>[-:\w]+)/$', TemplateView.as_view(template_name='registration/confirm_email.html'),
        name='account_confirm_email'),

]
