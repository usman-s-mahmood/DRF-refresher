# created manually!
from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home-index'),
    path('person/', views.people, name='home-people'),
]