from django.contrib import admin
from .models import Choice, Question # Importar el modelo que quieres que este disponible para editar en el administador django


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3   # Para crear 3 respuestas en uan pregunta

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]  # Orden en el cual aprarecen los campos en el admin
    inlines = [ChoiceInLine]
    list_display = ("question_text", "pub_date", "was_published_recently")   # Muestra estos campos en a parte superior para poder visualizar en donde puedes aplicar algun filtro.
    list_filter = ["pub_date"]  # Hace un filtro por fecha de publicacion
    search_fields = ["question_text"]   # Aplica una busqueda mediante el texto de la pregunta

admin.site.register(Question, QuestionAdmin) 
admin.site.register(Choice)
# admin.site.register([Question, Choice])   # es lo mismo importarlos en una lista o cada uno por separado 