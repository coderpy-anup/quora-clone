from django.urls import path
from apps.core.views import *
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('logout/',sign_out, name='logout'),
    path('register/', register, name='register'),
    path('questions/', question_list, name='question_list'),
    path('question/new/', post_question, name='post_question'),
    path('question/<int:pk>/', question_detail, name='question_detail'),
    path('question/<int:pk>/answer/', post_answer, name='post_answer'),
    path('answer/<int:answer_id>/like/', like_answer, name='like_answer'),
    path('question/<int:question_id>/like/', like_question, name='like_question'),
    path('question/<int:pk>/delete/', delete_question, name='delete_question'),
    path('answer/<int:pk>/delete/', delete_answer, name='delete_answer'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]