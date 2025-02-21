"""
URL configuration for Project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vege.views import * 

urlpatterns = [
    path('',home,name='home'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('add_recipe/<int:recipe_id>/', add_recipe, name='edit_recipe'),
    path('delete_recipe/<int:recipe_id>/', delete_recipe, name='delete_recipe'),
    path('update_recipe/<int:recipe_id>/', update_recipe, name='update_recipe'),
   
]