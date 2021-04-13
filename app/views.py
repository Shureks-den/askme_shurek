from django.shortcuts import render
from django.core.paginator import Paginator

questions = [
    {
        'title': 'title' + str(i),
        'id': i,
        'text': 'text' + str(i),
        'tag': 'Helpme'
    } for i in range(10)
]

answers = [
    {
        'id': i,
        'text': 'you should do' + str(i + 1),
    } for i in range(10)
]


def tag_search(request, tag):
    object_list = []
    for question in questions:
        if question['tag'] == str(tag):
            object_list.append(question)
    val = paginate(object_list, 3, request)
    return render(request, 'tag_search.html', {'page': val[0], 'questions': val[1], 'tag': tag})


def paginate(data, num, request):
    val = []
    paginator = Paginator(data, num)
    page = request.GET.get('page')
    pag_questions = paginator.get_page(page)
    val.append(page)
    val.append(pag_questions)
    return val


def index(request):
    val = paginate(questions, 3, request)
    return render(request, 'index.html', {'page': val[0], 'questions': val[1]})


def hot_questions(request):
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
    question = questions[pk]
    val = paginate(answers, 3, request)
    return render(request, 'question.html', {"question": question, 'page': val[0], 'answers': val[1]})
