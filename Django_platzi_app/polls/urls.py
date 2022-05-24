from django.urls import path # Para hacer uso de keyword path
from . import views # De esta carpeta(polls) importa views 

# Para crear una app en el proyecto py manage.py startapp nombre_app
app_name = "polls"  # Variable que contine el nombre de la app 

urlpatterns = [     # Variable que guarda todas las urls en una lista 
    # Ex: /polls/
    # views. llama a la clase IndexView como una vista con el metodo as_view() 
    # <int:pk> es el parametro que recibe la clase para saber a que pregunta corresponde cada respuesta y a que pregunta se esta llamando
    path("", views.IndexView.as_view(), name="index"),  
    # Ex: /polls/1/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # Ex: /polls/2/result
    path("<int:pk>/result", views.ResultView.as_view(), name="result"),
    # Ex: /polls/3/vote
    # views. llama a la funcion vote
    path("<int:question_id>/vote", views.vote, name="vote"),
]