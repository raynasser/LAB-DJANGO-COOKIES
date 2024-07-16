from . import views
from django.urls import path


app_name = "main"


urlpatterns = [
    path('', views.home_view, name= 'home'),
    path('properties/', views.properties_view, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('toggle_theme/', views.toggle_theme, name='toggle_theme'),
]