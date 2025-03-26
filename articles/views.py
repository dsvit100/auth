from django.shortcuts import render, redirect
from articles.forms import ArticleForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

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