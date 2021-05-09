from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('api/', include('api.urls')),
    path('rest/auth/', include('dj_rest_auth.urls')),
    path('rest/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
