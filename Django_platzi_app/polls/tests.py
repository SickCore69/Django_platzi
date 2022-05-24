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

def create_question(question_text, days):
    """ Create a question to make test, in the parameters days will puts numbers positive to create a question 
    in the future and negative numbers to question published in the past """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        """ If doesn't exist a quiestion show a message """
        response = self.client.get(reverse("polls:index")) # self.client.get = request HTTP
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question(self):
        """ Questions with a pub_date in the future aren't displayed  on the index page """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """ Question with a pub_date in the past aren't displayed on the index page """
        question = create_question("Past question", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

    def test_future_and_past_question(self):
        """ In this test just be displayed the past questions """ 
        past_question=create_question("This is a past question", days=-15)
        future_question=create_question("This is a future question", days=60)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question])
        
    def test_two_past_question(self):
        """ It'll publish all questions createds in the past """
        past_question1 = create_question("Past question one", days=-4)
        past_question2 = create_question("Past question two", days=-82)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question1, past_question2]
            )
    
    def test_two_future_question(self):
        """ This test should show status code 200 because the two future question pasts well."""
        future_question_1= create_question("Future question one", 65)
        future_question_2= create_question("Future question two", 14)
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        """ Don't allowed show questions whose pub_date is in the future anda then show a error 404 """
        future_question=create_question("This is a future question", 66)
        url = reverse("polls:detail", args=(future_question.pk,))
        response = self.client.get(url)     # response = self.clinet.get(revese("polls:detail"))       
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """ You can see all past question """
        past_question=create_question("This is a past question", -13)
        response = self.client.get(reverse("polls:detail", args=(past_question.id,))) # polls:detail viene del nombre escrito en el modulo url.py
        self.assertContains(response, past_question.question_text)   # Verifica si en response existe el texto de la past_question      # polls es el nombre de la app y detail el nombre que se le da a la url
        