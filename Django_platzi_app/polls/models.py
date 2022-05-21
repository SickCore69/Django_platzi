import datetime # Para hacer uso de la fecha 
from django.db import models # Modulo models para hacer uso de la clase Model para crear las clases
from django.utils import timezone # Usar la zona horaria


# Tablas creadas en forma de clases para hacer uso de la base de datos
class Question(models.Model):
    """ Question 
    Para poder crear las preguntas dentro de la app polls
    Atributos: 
        - variable_donde_guarda_pregunta = Tipo de dato que almacena(longitud maxima que soporta)
        - variable_guarda_fecha_de_publicacion_de_pregunta = Campo de tipo DateTime("Nombre para saber de que se trata") """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        """ __str__
        Retorna el valor que tiene el objeto question_text o la pregunta creada
        Atributos:
            - question_text: models.CharField(max_length=200)
        Retorna: La pregunta """
        return self.question_text

    def was_published_recently(self):
        """ Fue publicado recientemente
        Muestra verdadero si la pregunta fue publicada con un dia de diferencia con respecto a la fecha actual
        Atributos:
            - pub_date:
        Retorna: True or False """
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """ Choice
    Para poder elegir entre las diferentes preguntas y respuestas que hay dentro de la app polls y votar por una respuesta
    Atributos:
        - question = tipo de dato llave_foranea que hace referencia a question_text(Llave_foranea es de Question, tipo de borrado=Casdada)
        -texto_de_respuesta= Tipo_Char(longitud maxima del texto)
        -votos = Tipo_Entero(valor_de_comienzo) """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """ __str__
        Muestra el contenido de la variable choice_text "La respuesta de la pregunta" 
        Atributo: 
            - choice_text: models.CharField(max_length=200)
        Retorna: La o las respuestas de cada pregunta"""
        return self.choice_text