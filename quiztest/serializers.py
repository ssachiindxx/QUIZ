from rest_framework import serializers
from quiztest.models import Quiz

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('question', 'option1', 'option2', 'option3', 'option4')