from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u'Название статьи неуникально'
                    return render(request, 'create_post.html', {'form': form})
                else:
                    # если поля заполнены без ошибок
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})

    else:
        raise Http404


def create_user(request):
    if request.method == 'POST':
        form = {
            'login': request.POST["login"], 'email': request.POST["email"], 'pass': request.POST["pass"]
        }
        if form['login'] and form['email'] and form['pass']:
            try:
                User.objects.get(username=form['login'])
                form['errors'] = u"Пользователь с таким логином уже существует"
                form['login'] = ''
            except User.DoesNotExist:
                User.objects.create_user(form['login'], form['email'], form['pass'])
                form['login'] = ''
                form['email'] = ''
                form['pass'] = ''
                form['errors'] = u'Пользователь успешно зарегистрирован'
                return render(request, 'create_user.html', {'form': form})
        else:
            form['errors'] = u"Не все поля заполнены"
        return render(request, 'create_user.html', {'form': form})
    else:
        return render(request, 'create_user.html')

def auth_user(request):
    if request.method == 'POST':
        form = {
            'login': request.POST['login'], 'pass': request.POST['pass']
        }
        if form['login'] and form['pass']:
            user = authenticate(username=form['login'], password=form['pass'])
            if user:
                login(request, user)
                form['errors'] = u'Пользователь успешно авторизован'
            else:
                form['errors'] = u'Данного аккаунта не существует'
            return render(request, 'auth_user.html', {'form': form})
        else:
            form['errors'] = u'Не все поля заполнены'
            return render(request, 'auth_user.html', {'form' : form})
    else:
        return render(request, 'auth_user.html')