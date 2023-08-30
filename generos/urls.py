
from django.urls import path
from generos import views


urlpatterns = [
   
    
    path('', views.generos, name='generos' ),
    path('crear/', views.crear_genero, name='crear_generos'),
    path('<int:genero_id>/', views.genero_detalle, name='genero_detalle'),
    path('<int:genero_id>/eliminar/', views.eliminar_genero, name='eliminar_genero'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.salir, name='logout'),
    path('signin/', views.iniciar_sesion, name='signin'),
    

    
]