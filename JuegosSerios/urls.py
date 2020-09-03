from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('juegos_serios/', views.juegos_serios, name='juegos_serios'),
    path('<int:juego_serio_id>/', views.detalles, name='detalles'),
    path('sugerencias/', views.sugerencias, name='sugerencias'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('resultados/', views.resultados, name='resultados'),
]