from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from app import models


def paginate(data, num, request):
    paginator = Paginator(data, num)
    page = request.GET.get('page')
    pag_questions = paginator.get_page(page)
    return page, pag_questions


def tag_search(request, tag):
    tag = get_object_or_404(models.Tag.objects, tag=tag)
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    questions = tag.questions()
    val = paginate(questions, 3, request)
    return render(request, 'tag_search.html', {'page': val[0], 'questions': val[1], 'tag': tag, 'tags': tags, 'profiles': profiles})


def index(request):
    questions = models.Question.objects.new_questions()
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    val = paginate(questions, 4, request)
    return render(request, 'index.html', {'page': val[0], 'questions': val[1], 'tags': tags, 'profiles': profiles})


def hot_questions(request):
    questions = models.Question.objects.hot_questions()
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    val = paginate(questions, 4, request)
    return render(request, 'hot_questions.html', {'page': val[0], 'questions': val[1], 'tags': tags, 'profiles': profiles})


def login(request):
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    return render(request, 'login.html', {'tags': tags, 'profiles': profiles})


def signup(request):
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    return render(request, 'signup.html', {'tags': tags, 'profiles': profiles})


def settings(request):
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    return render(request, 'settings.html', {'tags': tags, 'profiles': profiles})


def ask(request):
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    return render(request, 'ask.html', {'tags': tags, 'profiles': profiles})


def one_question(request, pk):
    question = get_object_or_404(models.Question.objects, pk=pk)
    tags = models.Tag.objects.all()[0:8]
    profiles = models.Profile.objects.all()[0:5]
    answers = question.answers()
    val = paginate(answers, 3, request)
    return render(request, 'question.html', {"question": question, 'page': val[0], 'answers': val[1], 'tags': tags, 'profiles': profiles})
