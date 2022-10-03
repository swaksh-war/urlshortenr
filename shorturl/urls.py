from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('create/',views.create, name='create'),
    path('logout/', views.logout, name='logout'),
    path('<str:pk>', views.open, name='open')
]


