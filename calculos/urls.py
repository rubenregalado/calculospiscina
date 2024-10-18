from django.urls import path
from . import views

urlpatterns = [
    path('calcular-dosificacion/', views.calcular_dosificacion, name='calcular_dosificacion'),
]