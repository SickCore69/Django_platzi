from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from django.http import HttpResponse # Para realizar peticiones HTTP
from django.http import HttpResponseRedirect # Para realizar peticiones con redireccion
from django.views import generic 
from django.urls import reverse

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request, "polls/index.html",{
#         "latest_question_list": latest_question_list
#     })


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, "polls/detail.html", {
#         "question": question
#     })

# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/result.html", {
#         "question": question
#     })


# Para enviarte a la pagina principal se usa el IndexView
class IndexView(generic.ListView): 
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """ Return the latest fice published questions """
        return Question.objects.order_by("-pub_date")[:5]

# Ver los detalles 
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# Ver os resultados 
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"  
    
# Votar por un curso, maestro o escuela en patzi
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
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))

