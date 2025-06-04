from django.urls import path
from . import views

urlpatterns =[ 
    path('', views.home),
    path('registrarQueja/', views.registrarQueja),
    path('edicionQueja/<codigo>', views.edicionQueja),
    path('editarQueja/', views.editarQueja),
    path('eliminarQueja/<codigo>', views.eliminarQueja),
]