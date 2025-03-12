from django.urls import path
from rest_framework.authtoken import views

from auth_app.views import LoginView, confirm_view, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('confirm/<str:token>/', confirm_view, name='confirm'),
]