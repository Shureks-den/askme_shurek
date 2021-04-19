from django.urls import path, include

from app import views

urlpatterns = [
    path('hot/', views.hot_questions, name='hot'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('ask/', views.ask, name='ask'),
    path('question/<int:pk>/', views.one_question, name='one_question'),
    path('tag/<slug:tag>/', views.tag_search, name='tag_search'),
    path('', views.index, name='new_questions'),
]
