from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.page_login, name='page_login'),
    path('register/', views.register, name='register'),
    path('register-success/', views.register_success, name='register_success'),
    path('', views.page_home, name='page_home')
]
