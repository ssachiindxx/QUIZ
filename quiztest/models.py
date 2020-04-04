from django.db import models

class Quiz(models.Model):
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 20,null = True)
    option2 = models.CharField(max_length = 20,null = True)
    option3 = models.CharField(max_length = 20,null = True)
    option4 = models.CharField(max_length = 20,null = True)
    answer = models.CharField(max_length = 20,null = True)