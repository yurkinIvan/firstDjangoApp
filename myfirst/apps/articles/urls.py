from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logoutUser, name = 'logoutUser'),
    path('register/', views.register, name = 'register'),
    path('loadArticles/', views.loadArticles, name = 'loadArticles'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment')
]