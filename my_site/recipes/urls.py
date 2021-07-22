from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('<int:pk>/', views.details, name="recipe-details"),
    path('new-recipe/', views.add_recipe, name="recipe-add"),
    path('delete-recipe/<int:pk>/', views.delete_recipe, name="recipe-delete"),
    path('about/', views.about, name="recipes-about"),
    path('contact/', views.contact, name="recipes-contact")
]
