from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('packages/', views.packages_list, name='packages_list'),
    path('activities/', views.activities_list, name='activities_list'),
    path('about/', views.about_us, name='about_us'),
    path('package/<int:pk>/', views.travel_package_detail, name='travel_package_detail'),
]
