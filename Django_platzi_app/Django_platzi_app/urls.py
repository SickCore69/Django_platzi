"""Django_platzi_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from django.urls import include # Para incluir todas las rutas que tiene una direccion("url") 

urlpatterns = [
    path('admin/', admin.site.urls),
    # El nombre de la ruta debe ser el mismo de la app para que sea representativo
    # Con la ruta "polls/", incluye dentro de la app polls en el modelo urls.py todas las urls y usalas
    path("polls/", include("polls.urls")) # path("endpoint_para_el_url/", include("nombre_app.nombre_archivo_urls"))
]                                         
