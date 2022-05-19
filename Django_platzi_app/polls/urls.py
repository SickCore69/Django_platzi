from django.urls import path

from . import views

urlpatterns = [
    # Ex: /polls/
    path("", views.index, name="index"),
    # Ex: /polls/15/
    path("<int:question_id>/", views.detail, name="detail"),
    # Ex: /polls/26/result
    path("<int:question_id>/result", views.result, name="result"),
    # Ex: /polls/8/vote
    path("<int:question_id>/vote", views.vote, name="vote"),
]