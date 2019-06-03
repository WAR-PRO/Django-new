from .models import Article
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def title_is_unique(title):
    for i in range(Article.objects.latest('id').id):
        article_id = i + 1
        post = Article.objects.get(id=article_id)
        if post.title == title:
            return False
    return True

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
             'text': request.POST["text"],
             'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок

                if not title_is_unique(form["title"]):
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})

                article = Article.objects.create(
                 text=form["text"],
                 title=form["title"],
                 author=request.user
                )
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

def username_is_unique(username):
    try:
        User.objects.get(username=username)
        # если юзер существует, то ошибки не произойдет и
        # программа удачно доберется до следующей строчки
        return False
    except User.DoesNotExist:
        return True

def register(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
         'username': request.POST["username"],
         'email': request.POST["email"],
         'password': request.POST["password"]
        }
        # в словаре form будет храниться информация, введенная пользователем
        if form["username"] and form["email"] and form["password"]:
            # если поля заполнены без ошибок

            if not username_is_unique(form["username"]):
                form['errors'] = u"Пользователь с таким именем уже существует"
                return render(request, 'register.html', {'form': form})

            User.objects.create_user(form["username"], form["email"], form["password"])

            return redirect('archive')
        else:
            # если введенные данные некорректны
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'register.html', {})

def auth_login(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
         'username': request.POST["username"],
         'password': request.POST["password"]
        }
        # в словаре form будет храниться информация, введенная пользователем
        if form["username"] and form["password"]:
            # если поля заполнены без ошибок

            user = authenticate(username=form["username"], password=form["password"])

            if user is None:
                form['errors'] = u"Неверное имя пользователя или пароль"
                return render(request, 'login.html', {'form': form})

            login(request, user)

            return redirect('archive')
        else:
            # если введенные данные некорректны
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'login.html', {})
