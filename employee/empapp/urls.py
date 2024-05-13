"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from empapp import views
app_name="empapp"


urlpatterns = [
    path('',views.home,name="home"),
    path('add/', views.add, name="add"),
    path('view/', views.view, name="view"),
    path('detail/<int:n>', views.detail, name="detail"),
    path('delete/<int:n>', views.delete, name="delete"),
    path('edit/<int:n>', views.edit, name="edit"),

]
