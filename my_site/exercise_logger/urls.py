from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name='exercise-home'),
    path(route='about/', view=views.about, name='exercise-about')
]
