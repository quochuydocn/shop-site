
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Home, name= 'home'),
    path('up/', views.Up_sp, name= 'up'),
]
