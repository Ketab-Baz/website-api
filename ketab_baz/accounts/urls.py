from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign-in', views.sign_in),
]
