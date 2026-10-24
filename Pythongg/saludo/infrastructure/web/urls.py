from django.urls import path
from . import views

urlpatterns = [
    path("saludar/", views.saludar_post, name="saludar_post"),
    path("saludar/<str:nombre>/", views.saludar_get, name="saludar_get"),
]