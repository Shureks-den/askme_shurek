from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from app import models


def tag_search(request, tag):
    tag = get_object_or_404(models.Tag.objects, tag=tag)
    questions = tag.questions()
    val = paginate(questions, 3, request)
    return render(request, 'tag_search.html', {'page': val[0], 'questions': val[1], 'tag': tag})


def paginate(data, num, request):
    paginator = Paginator(data, num)
    page = request.GET.get('page')
    pag_questions = paginator.get_page(page)
    return page, pag_questions


def index(request):
    questions = models.Question.objects.new_questions()
    val = paginate(questions, 3, request)
    return render(request, 'index.html', {'page': val[0], 'questions': val[1]})


def hot_questions(request):
    questions = models.Question.objects.hot_questions()
    val = paginate(questions, 4, request)
    return render(request, 'hot_questions.html', {'page': val[0], 'questions': val[1]})


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def settings(request):
    return render(request, 'settings.html', {})


def ask(request):
    return render(request, 'ask.html', {})


def one_question(request, pk):
    question = get_object_or_404(models.Question.objects, pk=pk)
    answers = question.answers()
    val = paginate(answers, 3, request)
    return render(request, 'question.html', {"question": question, 'page': val[0], 'answers': val[1]})
