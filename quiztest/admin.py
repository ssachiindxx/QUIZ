from django.contrib import admin
from quiztest.models import Quiz

# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ('question',)

admin.site.register(Quiz)