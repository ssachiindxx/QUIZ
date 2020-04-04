from django.urls import path
from . import views

urlpatterns = [
    path('',views.qpage,name='index'),
    path('login/',views.login,name='login'),
    # path('quizapi/', views.qpage,name='qpage'),
]