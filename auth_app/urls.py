from django.urls import path

from auth_app.views import LoginView, confirm_view, forgot_password_view, register_view, reset_password_redirect_view, reset_password_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('confirm/<str:token>/', confirm_view, name='confirm'),
    path('forgot-password/', forgot_password_view, name='forgot-password'),
    path('reset-password/<str:token>/', reset_password_redirect_view, name='reset-password-redirect'),
    path('reset-password/', reset_password_view, name='reset-password'),  
]