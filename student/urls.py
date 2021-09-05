from django.urls import path,include
from student import views

# app_name = "student"
urlpatterns = [
    path('index/', views.index)
]