from django.shortcuts import render, redirect
from articles.forms import ArticleForm, CommentForm
from .models import Article, Comment
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
    article = Article.objects.get(id=id)
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'detail.html', context)

# 로그인 하지 않으면 사용할 수 없게끔 @ 이후를 붙여줌
@login_required
def comment_create(request, article_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False) # 빼먹은 정보가 있으니 잠시 기다려줘 (아래에 작성)
        
        # 객체를 저장하는 경우
        # comment.user = request.user # user정보...???
        # article = Article.objects.get(id=article_id)
        # comment.article = article

        # id값을 저장하는 경우 (db 안에 있는 컬럼을 이용)
        comment.user_id = request.user.id
        comment.article_id = article_id # 이 article_id는 함수 인자로 넣은 article_id

        comment.save()
        
        return redirect('articles:detail', id=article_id)

@login_required
def delete(request, id):
    article = Article.objects.get(id=id)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


@login_required
def update(request, id):
    article = Article.objects.get(id=id)
    
    if request.user != article.user:
        return redirect('articles:index')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) # 기존 정보를 앞에 있는 새정보로 덮어쓰기
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)

    else:
        form = ArticleForm(instance=article) # 기존에 쓴 내용이 들어간 빈 종이
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


@login_required
def comment_delete(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
    # request.user = 현재 접속한 사람
    # user = 뭐라고햇디
        comment.delete()
    return redirect('articles:detail', id=article_id)