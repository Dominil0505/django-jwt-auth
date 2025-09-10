from django.urls import path

from .views import UserRegisterView, AllUserView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('auth/register', UserRegisterView.as_view(), name="register"),
    path('all-user', AllUserView.as_view(), name='all_user'),
        
    path('auth/token', MyTokenObtainPairView.as_view(), name='token'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
]

