from django.urls import path # Para hacer uso de keyword path
from . import views # De esta carpeta(polls) importa views 

# Para crear una app en el proyecto py manage.py startapp nombre_app
app_name = "polls" 
urlpatterns = [     # Variable que guarda todas las urls en una lista 
    # Ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # Ex: /polls/15/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # Ex: /polls/26/result
    path("<int:pk>/result", views.ResultView.as_view(), name="result"),
    # Ex: /polls/8/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
]