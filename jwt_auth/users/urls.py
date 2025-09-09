from django.urls import path

from .views import UserRegisterView, AllUserView

urlpatterns = [
    path('auth/register', UserRegisterView.as_view(), name="register"),
    path('all-user', AllUserView.as_view(), name='all_user')
]