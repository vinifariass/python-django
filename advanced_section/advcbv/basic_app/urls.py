from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('schools/<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
]