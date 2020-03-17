from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login as auth_login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required 

# Import models
from .models import Article

@login_required(login_url='articles:login')
def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', { 'latest_articles_list': latest_articles_list })

@login_required(login_url='articles:login')
def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {"article": a, "comments": latest_comments_list})

@login_required(login_url='articles:login')
def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(author_name = request.user, comment_text = request.POST["text"], pub_date = timezone.now())

    return redirect('articles:detail', args = (a.id,)) # Just like {% url 'articles:detail' a.id %}

def login(request):

    if request.user.is_authenticated:
        return redirect('articles:index')
    else:
        context = {}

        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password=password) # Get user from db

            if user is not None:
                auth_login(request, user)
                return redirect('articles:index')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'authorization/login.html', context)

        return render(request, 'authorization/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('articles:login')

def register(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST) # Create new form to check validation
            if form.is_valid():
                form.save() # Create new User
                user = form.cleaned_data.get('username')
                messages.success(request, 'Аккаунт был создан ' + user)

                # return redirect("login")
                return redirect('articles:login')

        context = {'form': form}
        return render(request, 'authorization/register.html', context)