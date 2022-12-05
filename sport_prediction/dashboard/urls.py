from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('prediction/', views.prediction, name='dashboard-prediction'),
]