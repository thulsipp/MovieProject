"""
URL configuration for movie project.

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
from app1 import views
app_name = "app1"

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.MovieList.as_view(),name="home"),
    # path('addmore',views.addmore,name="addmore"),
    path('addmore/',views.Movieadd.as_view(),name="addmore"),
    # path('details/<int:p>',views.details,name="details"),
    path('m/<int:pk>',views.MovieDetail.as_view(),name="details"),
    # path('update/<int:p>', views.update, name="update"),
    path('update/<int:pk>',views.Movieupdate.as_view(),name="update"),
    # path('delete/<int:p>', views.delete, name="delete"),
    path('delete/<int:pk>',views.Moviedelete.as_view(),name="delete"),
]
