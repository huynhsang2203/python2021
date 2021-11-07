from django.urls import path
from .import views
from .views import LoginClass

urlpatterns = [
    path('login/', LoginClass.as_view(), name='page_login'),
    path('register/', views.register, name='register'),
    path('register-success/', views.register_success, name='register_success'),
    path('', views.page_home, name='page_home')
]
