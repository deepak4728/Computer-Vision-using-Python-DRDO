from django.urls import path
from . import views

urlpatterns = [
    path('', views.edge_detection_view, name='edge_detection_view'),
]
