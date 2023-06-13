from taller import views
from django.urls import path


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('lideres/', views.leerLideres, name="Lideres"),
    path('operarios/', views.leerOperarios, name="Operarios"),
    path('herramientas/', views.leerHerramientas, name="Herramientas"),
    path('consumibles/', views.leerConsumibles, name="Consumibles"),
    path('herramientaFormulario/', views.herramientasFormulario, name="Formulario"),
    path('liderForm/', views.liderFormulario, name='NuevoLider' ),
    path('OperarioForm/', views.operarioFormulario, name='NuevoOperario' ),
    path('buscaOperario/', views.buscar, name="BuscaOperario"),

]
