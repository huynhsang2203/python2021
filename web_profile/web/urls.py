from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.page_login, name='page_login'),
    path('register/', views.register, name='register'),
    path('', views.page_home, name='page_home')
]
