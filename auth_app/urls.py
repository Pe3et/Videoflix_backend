from django.urls import path

from auth_app.views import login_view, register_view

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
]