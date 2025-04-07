from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from apps.core.models import Question,Answer
from apps.core.forms import QuestionForm,AnswerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def error_404_view(request,exception):
    site    = get_current_site(request).domain
    context = {'site':site, 'title': 'Home | Error 404'}
    return render(request, 'errors/page_404.html',context)

def error_500_view(request, *args, **argv):
    site    = get_current_site(request).domain
    context = {'site':site, 'title': 'Home | Error 500'}
    return render(request, 'errors/page_500.html',context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    questions   = Question.objects.all().order_by('-created_at')
    paginator   = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    return render(request, 'home.html', {'questions': page_obj})

def question_list(request):
    questions       = Question.objects.all().order_by('-created_at')
    paginator       = Paginator(questions, 10)
    page_number     = request.GET.get('page')
    page_obj        = paginator.get_page(page_number)
    return render(request, 'question_list.html', {'questions': page_obj})

@login_required
def post_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.user = request.user
        question.save()
        return redirect('core:home')
    return render(request, 'post_question.html', {'form': form})

@login_required
def post_answer(request, pk):
    question    = get_object_or_404(Question, pk=pk)
    form        = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()
    return redirect('core:question_detail', pk=pk)

def question_detail(request, pk):
    question    = get_object_or_404(Question, pk=pk)
    answers     = question.answers.all()
    form        = AnswerForm()
    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect('core:question_detail', pk=answer.question.pk)

def sign_out(request):
    logout(request)
    return redirect('core:home')

@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk, user=request.user)
    if request.method == "POST":
        question.delete()  # This will also delete related answers if you set on_delete=models.CASCADE
        messages.success(request, "Question deleted successfully.")
        return redirect('core:question_list')  # or 'core:question_list' if you use that name
    return redirect('core:home')