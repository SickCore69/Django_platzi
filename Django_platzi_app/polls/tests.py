import datetime

from django.test import TestCase
from .models import Question, Choice
from django.utils import timezone
from django.urls import reverse 


# To run testcase ii with command py manage.py test name_app
# Ex: py manage.py test polls
class QuestionModelTests(TestCase):
    def setUp(self):
        """ question_test is a object to make test in each case(future_question, past_question and present_question)"""
        self.question_test = Question(question_text="¿Estas es una pregunta de prueba?")
        
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for future question whose pub_date is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        self.question_test.pub_date = time
        #future_question = Question(question_text="¿Quien dijo?", pub_date=time)  
        self.assertFalse(self.question_test.was_published_recently())          # Both assertstatements are same
        self.assertIs(self.question_test.was_published_recently(), False)      #

    def test_was_published_recently_with_past_question(self):
        """ was_published_recently returns False for question published in the past """
        time = timezone.now() - datetime.timedelta(days=20)
        past_question = Question(question_text="¿Pregunta publicada hace tiempo?", pub_date=time)
        self.assertFalse(past_question.was_published_recently())

    def test_was_published_recently_with_present_question(self):
        """ was_published_recently returns True if a question was published today(23 hours, 59 minutes) """
        time = timezone.now() - datetime.timedelta(hours=24, minutes=0)
        present_question = Question(question_text = "¿Pregunta publicada el dia de hoy?", pub_date=time)
        self.assertTrue(present_question.was_published_recently())


class ChoiceModelTests(TestCase):
    def test_no_question(self):
        """ If doesn't exist a quiestion show a message """
        response = self.client.get(reverse("polls:index")) # self.client.get = request HTTP
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])