from django.shortcuts import render
from django.http import HttpResponse
from quiztest.models import Quiz
from .serializers import UserSerializer
from rest_framework import viewsets

from rest_framework.generics import ListCreateAPIView


def qpage(request):
    questions = Quiz.objects.all()
    return render(request, 'quiz.html', {'questions': questions})

def login(request):
    return render(request, 'username.html')


class PostListCreateAPIView(ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = Quiz.objects.all()
        