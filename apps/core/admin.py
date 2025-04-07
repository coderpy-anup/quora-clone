from django.contrib import admin
from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','get_user_id','title','created_at','updated_at']
    list_filter  = ['id','user','created_at','updated_at']

    def get_user_id(self,obj):
        return obj.user.name


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id','get_question_id','get_user_id', 'created_at', 'updated_at']
    list_filter  = ['id', 'question', 'user', 'created_at', 'updated_at']

    def get_question_id(self,obj):
        return obj.question.id

    def get_user_id(self, obj):
        return obj.user.name