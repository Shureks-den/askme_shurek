from django.shortcuts import render
from django.core.paginator import Paginator

questions = [
    {
        'title': 'title' + str(i),
        'id': i,
        'text': 'text' + str(i),
        'tag': 'helpme'
    } for i in range(10)
]

answers = [
    {
        'id': i,
        'text': 'you should do' + str(i+1),
        'tag': 'helpme'
    } for i in range(10)
]

def index(request):
    paginator = Paginator(questions, 3)
    page = request.GET.get('page')
    pag_questions = paginator.get_page(page)
    return render(request, 'index.html', {'page': page, 'questions': pag_questions})


def hot_questions(request):
    paginator = Paginator(questions, 4)
    page = request.GET.get('page')
    pag_questions = paginator.get_page(page)
    return render(request, 'hot_questions.html', {'page': page, 'questions': pag_questions})


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def settings(request):
    return render(request, 'settings.html', {})


def ask(request):
    return render(request, 'ask.html', {})


def one_question(request, pk):
    question = questions[pk]
    paginator = Paginator(answers, 3)
    page = request.GET.get('page')
    pag_ans = paginator.get_page(page)
    return render(request, 'question.html', {"question": question, 'page': page, 'answers': pag_ans})

