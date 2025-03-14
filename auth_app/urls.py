from django.urls import path

from auth_app.views import LoginView, confirm_view, forgot_password, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('confirm/<str:token>/', confirm_view, name='confirm'),
    path('forgot-password/', forgot_password, name='forgot-password'),
]