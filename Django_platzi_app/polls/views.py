from django.shortcuts import render # Para retornar las templates.
from django.shortcuts import get_object_or_404 # PAra hacer una peticion y sino la encuentra retorna el error 404
from django.http import HttpResponse # Para realizar peticiones HTTP
from django.http import HttpResponseRedirect # Para realizar peticiones con redireccion y no se envien los datos del formulario dos veces
from django.views import generic # Para generar Generic Views al tener funciones que comparten atributos 
from django.urls import reverse # Forma de usar la etiqueta url y evitar hard code
from django.utils import timezone

from .models import Question, Choice 


# def index(request): # Funcion Index que recibe como parametro una peticion 
#     latest_question_list = Question.objects.all() # A la variable latest_question_list le vas a asignar todos los objetos que tiene Question
#     return render(request, "polls/index.html",{           # render(peticion HTTP, Carpeta_donde_esta_el_template/template, {       
#         "latest_question_list": latest_question_list      // Variables que pueden ser usadas en el templates en un diccionario} )
#     })


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)  # Busca en el modelo Question una primary key y lo almacena en la variable question
#     return render(request, "polls/detail.html", {             # Sino lo encuentra eleva el error 404 Not Found
#         "question": question
#     })

# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/result.html", {
#         "question": question
#     })


# Para enviarte a la pagina principal se usa el IndexView
class IndexView(generic.ListView): 
    template_name = "polls/index.html"  # Template a retornar
    context_object_name = "latest_question_list"    # Variable que se utiliza en el template
    
    def get_queryset(self):
        """ Return the latest five published questions """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# Ver los detalles 
class DetailView(generic.DetailView):
    model = Question    # Es igual a question = get_object_or_404(Question, pk=question_id)
    template_name = "polls/detail.html"

# Ver los resultados 
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"  
    
# Votar por un curso, maestro o escuela de patzi
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste unas respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))

