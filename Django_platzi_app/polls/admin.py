from django.contrib import admin
from .models import Choice, Question # Importar el modelo que quieres que este disponible para editar en el administador django


admin.site.register([Question, Choice]) 
# admin.site.register(Choice) es lo mismo importarlos en una lista o cada uno por separado 
