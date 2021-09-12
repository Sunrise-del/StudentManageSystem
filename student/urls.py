from django.urls import path,include
from student import views


urlpatterns = [
    path('index/', views.index),
    path('sign_up/', views.sign_up),
    path('login/', views.login),
    path('logout/', views.logout),
    path('add/', views.add),
    path('delete/', views.delete),
    path('select/', views.select),
    path('update/', views.update),
]

# app_name = "student"