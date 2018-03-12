from django.urls import path
from second_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('users/', views.user, name='users'),
    path('form-details/', views.form_detail_view, name='form-details')
]