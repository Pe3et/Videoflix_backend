from django.urls import path

from auth_app.views import confirm_view, login_view, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('confirm/<str:token>/', confirm_view, name='confirm')
]