from django.shortcuts import render, redirect
from articles.forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

@login_required
# 아래에 있는 함수를 실행하기 전에 위의 함수를 먼저 실행해 주세요.
# login이 안 되면 아래의 함수가 실행 X
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # form.save()
            # 유저데이터를 넣어줘야하는데 인자 하나를 빼먹었기 때문에 저장이 안될 것
            article = form.save(commit=False) # db에 바로 저장하지 말고 기다려
            article.user = request.user # 지금 로그인하고 있는 사람의 정보를 가져와서 article에 필요한 컬럼(.user)에 값을 넣어줌
            article.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def detail(request, id):
    article = Article.object.get(id=id)
    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)