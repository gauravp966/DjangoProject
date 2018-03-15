from django.urls import path
from second_app import views

app_name = 'second_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('users/', views.user, name='users'),
    path('form-details/', views.form_detail_view, name='form-details'),
    path('relative/', views.relative, name='relative')
]