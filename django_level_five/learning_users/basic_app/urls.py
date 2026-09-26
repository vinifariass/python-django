from django.urls import path
from basic_app import views

# TEMPLATE URLS

app_name = 'basic_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('special/', views.special, name='special'),
    path('logout/', views.user_logout, name='logout'),
]