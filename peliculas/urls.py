
from django.urls import path
from peliculas import views


urlpatterns = [
   
    path('', views.peliculas, name='peliculas'),
    path('crear/', views.crear_pelicula, name='crear_pelicula'),
    path('<int:pelicula_id>/', views.pelicula_detalle, name='pelicula_detalle'),
    path('<int:pelicula_id>/eliminar', views.eliminar_pelicula, name='eliminar_pelicula'),
    
]
