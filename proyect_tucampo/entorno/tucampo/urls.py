
from django.contrib import admin
from django.urls import path
from usuarios.views import *
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',Home, name="home"),
    path('home1',Home1, name="home1"),
    path('frutas/',frutas, name="frutas"),
    path('verduras/',verduras, name="verduras"),
    path('granos/',granos, name="granos"),
    path('leguminosas/',leguminosas, name="leguminosas"),
    path('granos/',granos, name="granos"),
    path('carnes/',carnes, name="carnes"),
    path('abarrotes/',abarrotes, name="abarrotes"),
    path('lacteos/',lacteos, name="lacteos"),
    path('l_lacteos/',l_lacteos, name="l_lacteos"),
    path('l_abarrotes/',l_abarrotes, name="l_abarrotes"),
    path('l_carnes/',l_carnes, name="l_carnes"),
    path('l_leguminosas/',l_leguminosas, name="l_leguminosas"),
    path('l_granos/',l_granos, name="l_granos"),
    path('l_verduras/',l_verduras, name="l_verduras"),
    path('l_frutas/',l_frutas, name="l_frutas"),
    path('vender/',vender, name="vender"),
    path('comprar/',comprar, name="comprar"),
    path('quien/',quien, name="quien"),
    path('productor/',productor, name="productor"),
    path('cliente/',cliente, name="cliente"),
    path('conductor/',conductor, name="conductor"),
    path('ofertas/',ofertas , name="ofertas"),
    path('ayuda/',ayuda, name="ayuda"),
    path('registro_manual/',registro_manual, name="registro_manual"),
    path('agregar_cond/',agregar_cond, name="agregar_cond"),
    path('agregar_usuario/',agregar_usuario, name="agregar_usuario"),
    path('validacion_manual/',validacion_manual, name="validacion_manual"),
    path('logueo_manual/',logueo_manual, name="logueo_manual"),
    path('logueo_exitosos/',logueo_exitosos, name="logueo_exitosos"),
    path('registro_func/',registro_func, name="registro_func"),
    path('soporte/',soporte, name="soporte"),
    path('salir/',salir, name="salir"),
    path('buscador/',buscador, name="buscador"),
    path('registro_productos/',registro_productos, name="registro_productos"),
    path('list_tusproductos/',list_tusproductos, name="list_tusproductos"),
    path('listas/',listas, name="listas"),
   
    
    
    ]       
