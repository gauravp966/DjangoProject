from django.urls import path
from django_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('static_image/', views.img, name='image')
]